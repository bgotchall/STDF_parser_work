# for now, just list all of the commands to run.  Eventually this should read the contents of an "input" directory
# and process as needed.


import subprocess



print("starting to convert hardcoded list of stdf files.  Enter to continue")
a=input()


print ("Running now: " )
# stdf2text SS_D5_115C.stdf > out.text     
subprocess.run(["ls", "-lrt"])
#subprocess.run(["stdf2text", "SS_D5_115C.stdf > out.text"])





print ("Done." )  