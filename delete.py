import subprocess
from subprocess import call
import time
import threading
k=['128.237.125.45','128.237.230.120']
y= time.strftime("%H:%M:%S")
z= time.strftime("%d/%m/%Y")


def wemo():
	while True:
		for i in range(0, 2):
			f1 = subprocess.check_output("wemocopy " + k[i] + " GETFRIENDLYNAME", shell=True)
			f1 = f1.strip()	
		
	
			f = subprocess.check_output("wemocopy " + k[i] + " GETALL ", shell=True)
			lis = f.split("|")
		
			f2 = subprocess.check_output("wemocopy " + k[i] + " GETMANU ", shell=True)
			lis2 = f2.split(";")		
				
	
			print z + " | "+ y +" | "+ f1 +" | "+" IP address:", k[i] + " | State:",lis[0]+" | currentmw:",lis[7]
			
			
		
threads = []
for l in range(1):
	t = threading.Thread(target=wemo)
	threads.append(t)
	t.start()		
		
		#pfile = open("testing-10.txt", "ab")
		#pfile.write(z + " | "+ y + " | "+ f1 + " | IP address:"+ k[i] + " | State:" + lis[0] + " | currentmw:" + lis[7] + "\n");
		#pfile.close()

		#qfile = open("testing-20.txt", "ab")
		#qfile.write(z + " | "+ y + " | "+ f1 + " | State:" + lis[0] + " | lastchange: "+lis[1] + " | onfor:"+ lis[2] + " | ontoday:" + lis[3] + " | ontotal:" + lis[4] + " | timeperiod:" + lis[5] + " | _x:" + lis[6] + " | currentmw:" + lis[7] + " | todaymw:" + lis[8] + " | totalmw:" + lis[9] + " | powerthreshold:" + lis[10] + " | PF: " + lis2[52][0:len(lis2[52])-3] + " | iRMS: " + lis2[48][0:len(lis2[48])-3] + " | vRMS: " + lis2[40][0:len(lis2[40])-3] + " | Frequency: " + lis2[56][0:len(lis2[56])-3] + "\n \n");
		#qfile.close()



