from subprocess import call
k=['128.237.125.45','128.237.230.120']
while True:
	for i in range(0, 2):
		call("newwemo " + k[i] + " GETFRIENDLYNAME", shell=True)
		call("newwemo " + k[i] + " GETALL > output.txt", shell=True)
		f = open('output.txt','r')
        	j = f.readline()
		lis = j.split("|")
		print "IP address:", k[i],"| State:",lis[0],"| currentmw:",lis[7]
		print "lastchange:",lis[1], "| onfor:",lis[2], "| ontoday:",lis[3], "| ontotal:",lis[4], "| timeperiod:",lis[5], "| _x:",lis[6],"| todaymw:",lis[8], "| totalmw:",lis[9], "| powerthreshold:",lis[10]
		


