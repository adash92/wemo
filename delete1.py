import subprocess
from subprocess import call
import time
k=['128.237.125.45','128.237.230.120']

for i in range(0, 2):

	f = subprocess.check_output("newwemo " + k[i] + " GETALL ", shell=True)
	lis = f.split("|")
	
	f1 = subprocess.check_output("wemocopy " + ip + " GETFRIENDLYNAME", shell=True)
	f1 = f1.strip()	
	
	y= time.strftime("%H:%M:%S")
	z= time.strftime("%d/%m/%Y")

	print z + " | "+ y +" | "+f1+" | "+" | "+" | "+" IP address:", k[i] + " | State:",lis[0]+" | currentmw:",lis[7]
	
		



