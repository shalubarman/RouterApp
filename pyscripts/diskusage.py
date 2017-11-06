#!/usr/local/bin/python

import subprocess

try:
	# To check the disk usage
	usage = subprocess.Popen('df', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output, err = usage.communicate()
	print output

except:
	print 'Please check the command and run again'



