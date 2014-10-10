from subprocess import call
import sys
import subprocess
import time

while True:
	call("newwemo 128.237.230.120 GETALL > output25.txt" , shell=True)
    	f = open('output25.txt','r')
    	i = f.readline()
    	lis = i.split("|")
	y= time.strftime("%H:%M:%S")
	z= time.strftime("%d/%m/%Y")
	#print "State:",lis[0]
	#print "lastchange:",lis[1]	
	print "onfor:",lis[2]
	#print "ontoday:",lis[3]
	#print "ontotal:",lis[4]
	#print "timeperiod:",lis[5]
	#print "_x:",lis[6]
	print y
	print z
	print "currentmw:",lis[7]
	print "todaymw:",lis[8]
	print "totalmw:",lis[9]
	print "\n"
	#print "powerthreshold:",lis[10]


