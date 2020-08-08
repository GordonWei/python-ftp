#!/usr/bin/env python3
# -*- coding: utf8 -*-

#author   GordonWei
#date   07/31/2020
#comment  connect ftp and get file

from ftplib import FTP


filterName = input('Pls Enter The FileName:' )
filterName = filterName + '*.*'

ftp = FTP()
ftp.connect(<ip>,<port>)

ftp.login(<loginuser>, <userpasswd>)

def get_File(filterName):
  ftp.cwd('/change/to/target/folder')
  fileList = ftp.nlst(filterName)
  for name in fileList :
    path = '/file/save/path/' + name
    f = open(path, 'wb')
    filename = 'RETR ' + name
    ftp.retrbinary(filename, f.write)
    
get_File(filterName)
ftp.quit()
