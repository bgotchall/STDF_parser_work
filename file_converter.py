# for now, just list all of the commands to run.  Eventually this should read the contents of an "input" directory
# and process as needed.
# the useage of stdf2text is # stdf2text SS_D5_115C.stdf > out.text    


import subprocess
import sys      
import glob

orig_stdout=sys.stdout


print("starting to convert hardcoded list of stdf files.  Enter to continue")
a=input()


print ("Running now: " )
# stdf2text SS_D5_115C.stdf > out.text     
#subprocess.run(["ls", "-lrt"])  #works
#subprocess.run(["ls *.stdf", "-lrt"])   #does not
#subprocess.run(["ls *.stdf", "-lrt"])
#subprocess.run(["stdf2text", "SS_D5_115C.stdf > out.text"])

if(0):              #reference code graveyard.  
    subprocess.run(["ls", "-lrt"])  #works
    cmd = ['ls', '-lrt', ]
    subprocess.run(cmd)             #also works


    #######################
    cmd = ['stdf2text', 'SS_D5_115C.stdf' ]                     #this is just a list of things that go in the "arg" part of subprocess.run
    result=subprocess.run(cmd,capture_output=True, text=True)

    #print(result.stdout)               # this works to print to screen

    with open('SS_D5_115C.atdf', 'w') as sys.stdout:
        print(result.stdout)

    sys.stdout.close
    ############################


    #######################
    cmd = ['stdf2text', 'demofile.stdf' ]                     #this is just a list of things that go in the "arg" part of subprocess.run
    result=subprocess.run(cmd,capture_output=True, text=True)

    #print(result.stdout)               # this works to print to screen

    with open('demofile.atdf', 'w') as sys.stdout:
        print(result.stdout)

    sys.stdout.close
    ############################

    #reset stdout to screen
    #with open(sys.stdout) as sys.stdout:
    #    print("Done.")

    sys.stdout= orig_stdout
    print("Done.")

if (0):     #this all works, but is limited.

    file_list=['SS_D5_115C.stdf','demofile.stdf']


    for  this_file in file_list:
        sys.stdout= orig_stdout
        out_file=this_file.replace("stdf","atdf")
        print("Processing ",this_file, " into ", out_file)
        
        cmd = ['stdf2text', this_file ]                     #this is just a list of things that go in the "arg" part of subprocess.run
        result=subprocess.run(cmd,capture_output=True, text=True)
        with open(out_file, 'w') as sys.stdout:
            print(result.stdout)
        sys.stdout.close

if(1):
    file_list= glob.glob("../../FT_datalogs/stdf_to_process/*.stdf.gz")

    for  this_file in file_list:
        sys.stdout= orig_stdout
        in_file_unzip=this_file.replace(".gz","")           #the name of the .stdf file without the .gz
        out_file=in_file_unzip.replace("stdf","atdf")       #the name of the .atdf target file
        print("Processing ",this_file, " into ", out_file)
        
        if(1):
            #unzip the stdf
            
            print("unzipping ",this_file)
            cmd = ['gzip','-d' , this_file ]                     #this is just a list of things that go in the "arg" part of subprocess.run
            subprocess.run(cmd)

            cmd = ['stdf2text', in_file_unzip ]                     
            result=subprocess.run(cmd,capture_output=True, text=True)
            with open(out_file, 'w') as sys.stdout:
                print(result.stdout)
            sys.stdout.close

            #now attempt to zip the atdf:
            sys.stdout= orig_stdout
            print("zipping ",out_file)
            cmd = ['gzip', out_file ]                    
            subprocess.run(cmd)

            #re-zip the input .stdf file:
            print("zipping ",in_file_unzip)
            cmd = ['gzip', in_file_unzip ]                     
            subprocess.run(cmd)

###################################################################
#wrap up and exit:
sys.stdout= orig_stdout
print("Done.")
###################################################################