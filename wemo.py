from subprocess import call
k=['128.237.125.45','128.237.230.120']
for i in range(0, 2):
	call("newwemo " + k[i] + " GETFRIENDLYNAME > output2.txt", shell=True)
	call("newwemo " + k[i] + " GETALL > output.txt", shell=True)
	f1 = open('output2.txt','r')
        j1 = f1.readline()
	f = open('output.txt','r')
        j = f.readline()
   	lis = j.split("|")
	j1=j1.strip()
	print j1+" | IP address:", k[i] + " | State:",lis[0]+" | currentmw:",lis[7]
	
	pfile = open("testing-1.txt", "ab")
	pfile.write(j1 + " | IP address:"+ k[i] + " | State:" + lis[0] + " | currentmw:" + lis[7] + "\n");
	pfile.close()

	qfile = open("testing-2.txt", "ab")
	qfile.write(j1 + " | State:" + lis[0] + " | lastchange: "+lis[1] + " | onfor:"+ lis[2] + " | ontoday:" + lis[3] + " | ontotal:" + lis[4] + " | timeperiod:" + lis[5] + " | _x:" + lis[6] + " | currentmw:" + lis[7] + " | todaymw:" + lis[8] + " | totalmw:" + lis[9] + " | powerthreshold:" + lis[10]);
	qfile.close()

	
