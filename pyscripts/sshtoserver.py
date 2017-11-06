import subprocess
import sys
COMMAND="ls"

HOST = raw_input("Enter your host name: ")
user = raw_input("Enter the command: ")
port = raw_input("Enter your port: ")

try:
	ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
	                   shell=False,
	                   stdout=subprocess.PIPE,
	                   stderr=subprocess.PIPE)
	result = ssh.stdout.readlines()
	if result == []:
	    error = ssh.stderr.readlines()
	    print >>sys.stderr, "ERROR: %s" % error
	else:
	    print result

except:
	print 'Please check your connect/credentials'