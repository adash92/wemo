from subprocess import call
import time
k=['128.237.125.45','128.237.230.120']
while True:
	for i in range(0, 2):
		call("newwemo " + k[i] + " GETFRIENDLYNAME > output2.txt", shell=True)
		call("newwemo " + k[i] + " GETALL > output.txt", shell=True)
		call("newwemo " + k[i] + " GETMANU > output3.txt", shell=True)	
		f1 = open('output2.txt','r')
        	j1 = f1.readline()
		j1 = j1.strip()		
		f = open('output.txt','r')
        	j = f.readline()
   		lis = j.split("|")
		
	
		f2 = open('output3.txt','r')
        	j2 = f2.readline()
   		lis2 = j2.split(";")
						
		y= time.strftime("%H:%M:%S")
		z= time.strftime("%d/%m/%Y")

		print z + " | "+ y +" | "+ j1+" | IP address:", k[i] + " | State:",lis[0]+" | currentmw:",lis[7]
	
		pfile = open("testing-1.txt", "ab")
		pfile.write(z + " | "+ y + " | "+ j1 + " | IP address:"+ k[i] + " | State:" + lis[0] + " | currentmw:" + lis[7] + "\n");
		pfile.close()

		qfile = open("testing-2.txt", "ab")
		qfile.write(z + " | "+ y + " | "+ j1 + " | State:" + lis[0] + " | lastchange: "+lis[1] + " | onfor:"+ lis[2] + " | ontoday:" + lis[3] + " | ontotal:" + lis[4] + " | timeperiod:" + lis[5] + " | _x:" + lis[6] + " | currentmw:" + lis[7] + " | todaymw:" + lis[8] + " | totalmw:" + lis[9] + " | powerthreshold:" + lis[10] + " | PF: " + lis2[52][0:len(lis2[52])-3] + " | iRMS: " + lis2[48][0:len(lis2[48])-3] + " | vRMS: " + lis2[40][0:len(lis2[40])-3] + " | Frequency: " + lis2[56][0:len(lis2[56])-3] + "\n \n");
		qfile.close()


