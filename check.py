import subprocess
from subprocess import call
import time
k = ['128.237.125.45','128.237.230.120']
m = ['128.237.125.45:Wemo Insight89','128.237.230.120:Wemo Insight74']
while True:
	for i in range(0, 2):
		f = subprocess.check_output("newwemo " + k[i] + " GETALL ", shell=True)
		lis = f.split("|")
	
		f2 = subprocess.check_output("newwemo " + k[i] + " GETMANU ", shell=True)
		lis2 = f2.split(";")		
		
		y= time.strftime("%H:%M:%S")
		z= time.strftime("%d/%m/%Y")
	
		

		print z + " | "+ y +" | "+ m[i] +" | "+" IP address:", k[i] + " | State:",lis[0]+" | currentmw:",lis[7]
	
		pfile = open("testing-100.txt", "ab")
		pfile.write(z + " | "+ y + " | "+ m[i] + " | IP address:"+ k[i] + " | State:" + lis[0] + " | currentmw:" + lis[7] + "\n");
		pfile.close()

		qfile = open("testing-200.txt", "ab")
		qfile.write(z + " | "+ y + " | " + m[i] + " | State:" + lis[0] + " | lastchange: "+lis[1] + " | onfor:"+ lis[2] + " | ontoday:" + lis[3] + " | ontotal:" + lis[4] + " | timeperiod:" + lis[5] + " | _x:" + lis[6] + " | currentmw:" + lis[7] + " | todaymw:" + lis[8] + " | totalmw:" + lis[9] + " | powerthreshold:" + lis[10] + " | PF: " + lis2[52][0:len(lis2[52])-3] + " | iRMS: " + lis2[48][0:len(lis2[48])-3] + " | vRMS: " + lis2[40][0:len(lis2[40])-3] + " | Frequency: " + lis2[56][0:len(lis2[56])-3] + "\n \n");
		qfile.close()


