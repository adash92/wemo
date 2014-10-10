import thread 
import time
import subprocess
from subprocess import call
#script for extraction of data from wemo
f1 = None
f2 = None

def wemonew(threadname,ip):
	while True:
		currenttime= time.strftime("%H:%M:%S")
		currentdate= time.strftime("%d/%m/%Y")
                #time.sleep(0)
		#function for calling friendlyname of the wemo		
		f1 = subprocess.check_output("wemocopy " + ip + " GETFRIENDLYNAME", shell=True)
		f1 = f1.strip()	
		#function for calling all parameters of wemo
		f = subprocess.check_output("wemocopy " + ip + " GETALL ", shell=True)
		lis = f.split("|")
		#function for calling all manufacturing details of wemo
		f2 = subprocess.check_output("wemocopy " + ip + " GETMANU ", shell=True)
		lis2 = f2.split(";")
		#printing the important parameters 
		print currentdate+" | "+currenttime+" | "+ f1 +" | "+" IP address:", ip + " | State:",lis[0]+" | currentmw:",lis[7]
		
		#exporting data to a file for summary info
                pfile = open("summary.txt", "ab")
		pfile.write(currentdate + " | "+ currenttime + " | "+ f1 + " | IP address:"+ ip + " | State:" + lis[0] + " | currentmw:" + lis[7] + "\n");
		pfile.close()
		
		#exporting data to a file for other details
		qfile = open("details.txt", "ab")
		qfile.write(currentdate + " | "+ currenttime + " | "+ f1 + " | State:" + lis[0] + " | lastchange: "+lis[1] + " | onfor:"+ lis[2] + " | ontoday:" + lis[3] + " | ontotal:" + lis[4] + " | timeperiod:" + lis[5] + " | _x:" + lis[6] + " | currentmw:" + lis[7] + " | todaymw:" + lis[8] + " | totalmw:" + lis[9] + " | powerthreshold:" + lis[10] + " | PF: " + lis2[52][0:len(lis2[52])-3] + " | iRMS: " + lis2[48][0:len(lis2[48])-3] + " | vRMS: " + lis2[40][0:len(lis2[40])-3] + " | Frequency: " + lis2[56][0:len(lis2[56])-3] + "\n \n");
		qfile.close()

#error handling part
try:
	thread.start_new_thread(wemonew,("","128.237.125.45"))
	thread.start_new_thread(wemonew,("","128.237.230.120"))
	
except:
	print "Error:unable to start"
while True:
	pass
	

        
