#!/usr/bin/env python3
## Moving files with SFTP

##import paramiko so we can talk SSH
import paramiko
import os

## where to connect to

t = paramiko.Transport("10.10.2.3", 22) ## IP and port

## how to connect (see other labs on using id_rsa private / public keypairs)

t = paramiko.Transport(username="bender", password="alta3")

## Make an sftp connection object

sftp = paramiko.SFTPClient.from : 
