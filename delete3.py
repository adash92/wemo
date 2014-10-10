import threading 
import time
import subprocess
from subprocess import call
#script for extraction of data from wemo



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

threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread("","128.237.125.45")
#thread2 = myThread("","128.237.230.120")

# Start new Threads
thread1.start()
#thread2.start()

# Add threads to thread list
#threads.append(thread1)
#threads.append(thread2)

# Wait for all threads to complete
#for t in threads:
 #   t.join()
