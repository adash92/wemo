import subprocess
import time
from subprocess import call
k=['128.237.125.45','128.237.230.120']
while True:
	for i in range(0, 2):
		f1 = subprocess.check_output("newwemo " + k[i] + " GETFRIENDLYNAME", shell=True)
		f1 = f1.strip()	
		f = subprocess.check_output("newwemo " + k[i] + " GETALL ", shell=True)
		lis = f.split("|")
		y= time.strftime("%H:%M:%S")
		z= time.strftime("%d/%m/%Y")
		print y ,z ,f1 , "State:",lis[0], "lastchange:",lis[1], "onfor:",lis[2], "currentmw:",lis[7], "todaymw:",lis[8], "totalmw:",lis[9] ,"powerthreshold:",lis[10]
		#print "ontoday:",lis[3]
		#print "ontotal:",lis[4]
		#print "timeperiod:",lis[5]
		#print "_x:",lis[6]
		


