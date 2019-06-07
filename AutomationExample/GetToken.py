#!/usr/bin/env python

import sys
sys.path.append('/home/MonitoringEXOTools/KerberosPythonWrapper/')

#from krbauth import *
import krbauth

from cryptography.fernet import Fernet
filep = open('pass', 'rb')
password = filep.read()
filep.close()
filek = open('key.key', 'rb')
key = filek.read()
filek.close()
f = Fernet(key)
decrypted = f.decrypt(password)

res = krbauth.krbauth('jruizalv@CERN.CH', decrypted)
if res:
    krbauth.log('Succesfully Logged in!', False)
else:
    krbauth.log('Incorrect Login!', False)
