import getpass
import sys
import telnetlib

HOST = raw_input("Enter your host name: ")
user = raw_input("Enter your remote account: ")
port = raw_input("Enter your port: ")
password = getpass.getpass()

try:
	tn = telnetlib.Telnet(HOST,port)
	tn.read_until("login: ")
	tn.write(user + "\n")
	if password:
	    tn.read_until("Password: ")
	    tn.write(password + "\n")

	tn.write("ls\n")
	tn.write("exit\n")
	print tn.read_all()

except:
	print 'Please check your connection/credentials'
