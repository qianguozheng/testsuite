import os, sys
import time

#CMD check process name
CMD_PS="ps"
CMD_GITLAB_RUNNER="gitlab_runner"
#process = os.system(CMD_PS)

#print (process)
#print (process.find("runnerserver"))

result = os.popen(CMD_PS)
info = result.readlines()

found = 0
while True:
	for line in info:
		line = line.strip('\r\n')
		print line
		if (line.find("gitlab_runnerxx") >= 0):
			global found
			found = 1
			break;
	
	if (1 == found):
		time.sleep(1)
		print("Found gitlab_runner")
	else:
		os.system("netstat -luntp") 
		time.sleep(1)
