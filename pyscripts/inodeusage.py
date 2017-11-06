import subprocess

try:
	# To check the inide usage
	usage = subprocess.check_output(['df', '-i'])
	print usage

except:
	print 'Please check the command and run again'
	