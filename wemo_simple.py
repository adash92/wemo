from subprocess import call
import sys
import subprocess
import time

y= time.strftime("%H:%M:%S")
z= time.strftime("%d/%m/%Y")

while True:
	j = subprocess.check_output("newwemo 128.237.230.120 GETALL " , shell=True)
	print y,z,j
	i = subprocess.check_output("newwemo 128.237.125.45 GETALL " , shell=True)
	print y,z,i
