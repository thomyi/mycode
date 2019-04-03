#!/usr/bin/env python3

import paramiko
import os
import getpass

t = paramiko.Transport("10.10.2.3", 22)

t.connect(username="bender", password=getpass.getpass("What is your password? "))
  
sftp = paramiko.SFTPClient.from_transport(t)

for x in os.listdir("/home/student/mycode/filestocopy"):
    if not os.path.isdir("/home/student/mycode/filestocopy" +x):
        sftp.put("/home/student/mycode/filestocopy/"+x, "/tmp/"+x)
        print("You copied {} using sftp".format(x))
sftp.close()
t.close()
