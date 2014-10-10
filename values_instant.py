#!/usr/local/bin/python

from subprocess import call
import sys
import subprocess
import time

call("newwemo 128.237.230.120 GETALL > output.txt" , shell=True)
f = open('output.txt','r')
i = f.readline()
lis = i.split("|")
#print "State:",lis[0]
#print "lastchange:",lis[1]	
#print "onfor:",lis[2]
#print "ontoday:",lis[3]
#print "ontotal:",lis[4]
#print "timeperiod:",lis[5]
#print "_x:",lis[6]
print "currentmw:",lis[7]
print "todaymw:",lis[8]
print "totalmw:",lis[9]
print "powerthreshold:",lis[10]
