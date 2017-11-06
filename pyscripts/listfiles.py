import subprocess
import sys, os

# To list the directory
print ''
user_input = raw_input("Please enter the path to list directory: ")
check_path = os.path.isdir(user_input)
print ''

if check_path:
	try:
		usage = subprocess.Popen('ls', stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd = user_input)
		output, err = usage.communicate()
		print output
	except:
		print 'Please check the command and run again'
else:
	print 'Please check the path you entered'
