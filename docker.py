#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess
import cgi

form = cgi.FieldStorage()
osname = form.getvalue('x')
os = form.getvalue('y')

output = subprocess.getstatusoutput("sudo docker run -d -i -t --name {0} {1}".format(osname, os))
status = output[0]
out = output[1]

if status == 0:
    print("Os Launched named:  " + osname)
else: 
    print("Error, Could'nt start docker..")