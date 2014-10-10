from subprocess import call

import sys
import subprocess
import time

k=['128.237.125.45','128.237.230.120']
while True:
	for i in range(0, 2):
		print("Wemo",i)
		j = subprocess.check_output("newwemo " + k[i] + " GETALL ", shell=True)
	        lis = j.split("|")
		y= time.strftime("%H:%M:%S")
		z= time.strftime("%d/%m/%Y")
	  	print z + " | "+ y +" | "+" | IP address:", k[i] + " | State:",lis[0]+" | currentmw:",lis[7]
	
