from subprocess import call
k=['128.237.125.45','128.237.230.120']
for i in range(0, 2):
	call("newwemo " + k[i] + " GETFRIENDLYNAME > output222.txt", shell=True)
	call("newwemo " + k[i] + " GETALL > output111.txt", shell=True)
	f1 = open('output222.txt','r')
        j1 = f1.readline()
	print j1
	f = open('output111.txt','r')
        j = f.readline()
   	lis = j.split("|")
	print "IP address:", k[i],"| State:",lis[0],"| currentmw:",lis[7]
	
	



	qfile = open("testing-111.txt", "ab")
	qfile.write("lastchange: "+lis[1] + " | onfor:"+lis[2] + " | ontoday:" + lis[3] + " | ontotal:" + lis[4] + " | timeperiod:" + lis[5] + " | _x:" + lis[6] + " | todaymw:" + lis[8] + " | totalmw:" + lis[9] + " | powerthreshold:" + lis[10]);
	qfile.close()

	pfile = open("testing-222.txt", "ab")
	pfile.write( "IP address:"+ k[i] + " | State:" + lis[0] + " | currentmw:" + lis[7] + "\n");
	pfile.close()































	#print "State(off-0; on-1; on but load is off-8):",lis[0]
	#print "lastchange:",lis[1]	
	#print "onfor(sec):",lis[2]
	#print "ontoday(sec):",lis[3]
	#print "ontotal(sec):",lis[4]
	#print "timeperiod(sec):",lis[5]
	#print "_x:",lis[6]
	#print "currentpower(mw):",lis[7]
	#print "todaypower(mw):",lis[8]
	#print "totalpower(mw):",lis[9]
	#print "powerthreshold:",lis[10]

#import psyco
#psyco.full()
