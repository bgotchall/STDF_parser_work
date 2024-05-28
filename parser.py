from pystdf.IO import Parser
from pystdf.V4 import pir, ptr, prr
import pandas
import numpy as np
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(12,8))

#Note for Bob.  I basically abandonded this because the command line stdf2text works for all I need.




#help(ptr)
print("hi")

 
class DataFrameSink(object):
    def __init__(self):
        self.index_tuples = []
        self.series = []
        self.test_nums = []
        self.results = []
        self.limits = {}
        self.data = None
    
    def before_send(self, source, data):
        rectype, fields = data
        if rectype == pir:
            self.on_pir(fields)
        elif rectype == ptr:
            self.on_ptr(fields)
        elif rectype == prr:
            self.on_prr(fields)
    
    def on_pir(self, fields):
        '''Part Information Record'''
        self.test_nums = []
        self.results = []

    def on_ptr(self, fields):
        '''Parametric Test Record'''
        self.test_nums.append(fields[ptr.TEST_NUM])
        self.results.append(fields[ptr.RESULT])
        self.limits[fields[ptr.TEST_NUM]] = [fields[ptr.LO_LIMIT], fields[ptr.HI_LIMIT]]
 
    def on_prr(self, fields):
        '''Part Result Record'''
        if self.results:
            self.series.append(pandas.Series(self.results, self.test_nums))
            self.index_tuples.append((int(fields[prr.PART_ID]), fields[prr.SITE_NUM]))
        
    def after_complete(self, source):
        names = ['part', 'site']
        index = pandas.MultiIndex.from_tuples(self.index_tuples, names=names)
        self.data = pandas.DataFrame(self.series, index=index)
        self.data.columns.name = 'test'
        self.limits = pandas.DataFrame(sink.limits, index=['low', 'high']).T
        self.limits.index.name = 'test'


print("hello")

f = open('demofile.stdf', 'rb')
parser = Parser(inp=f)
sink = DataFrameSink()
parser.addSink(sink)
parser.parse()
f.close()
data = sink.data  # data is a pandas DataFrame holding stdf test data
limits = sink.limits  # limits is also a DataFrame, it holds the test limits