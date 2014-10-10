import threading 
import time
import subprocess
from subprocess import call
#script for extraction of data from wemo

while True:
	class myThread (threading.Thread):
	    def __init__(self,threadname,ip):
		threading.Thread.__init__(self)
		self.threadname = threadname
		self.ip = ip

	    def run(self):
		# Get lock to synchronize threads
		threadLock.acquire()
		wemonew(self.threadname, self.ip)
		# Free lock to release next thread
		threadLock.release()

	def wemonew(threadname,ip):
		currenttime= time.strftime("%H:%M:%S")
		currentdate= time.strftime("%d/%m/%Y")
	
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

	threadLock = threading.Lock()
	threads = []

	# Create new threads
	thread1 = myThread("","128.237.125.45")
	thread2 = myThread("","128.237.230.120")

	# Start new Threads
	thread1.start()
	thread2.start()

	# Add threads to thread list
	threads.append(thread1)
	threads.append(thread2)

	# Wait for all threads to complete
	for t in threads:
	    t.join()
