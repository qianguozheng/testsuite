#coding: utf-8
import os, sys
import time
import smtplib
from email.mime.text import MIMEText

#CMD check process name
CMD_PS="ps -aux"
CMD_GITLAB_RUNNER="su gitlab_ci_runner -c 'cd $HOME/gitlab-ci-runner ; bundle exec ./bin/runner' &"
CMD_NEWFILE="ls -alh /var/www/html/firmware | wc -l"

#mailto_list= ["richard@focalcrest.com", "wendy@focalcrest.com", "jimmy@focalcrest.com", "sam@focalcrest.com"]
mailto_list = ["richard@focalcrest.com"]
mail_host = "mail.focalcrest.com"
mail_user="richard"
mail_pass="xxxxxx"
mail_postfix="focalcrest.com"


def send_mail(to_list, sub, content):
	me = "Gitlab CI inform new firmware generated"+"<"+mail_user+mail_postfix+">"
	msg = MIMEText(content, _subtype='html', _charset='gb2312')
	msg['Subject'] = sub #设置主题
	msg['From'] = me
	msg['To'] = ";".join(to_list)
	try:
		s = smtplib.SMTP()
		s.connect(mail_host)
		s.login(mail_user, mail_pass)
		s.sendmail(me, to_list, msg.as_string())
		s.close()
		return True
	except Exception, e:
		print (str(e))
		return (False)
		
#if __name__ == '__main__':
#	if send_mail(mailto_list, "新的固件生成啦", "New firmware file generated, please check http://192.168.202.40 "):
#		print("Send OK !")
#	else:
#		print("Send Failed")

#process = os.system(CMD_PS)

#print (process)
#print (process.find("runnerserver"))

fileno = os.popen(CMD_NEWFILE)
fileinfo = fileno.readlines()

while True:
	#Judge whether process exist or not
	result = os.popen(CMD_PS)
	info = result.readlines()
	
	fileno = os.popen(CMD_NEWFILE)
	fileinfonew = fileno.readlines()
	
	found = 0
	for line in info:
		line = line.strip('\r\n')
		print line
		if (line.find("gitlab_ci_runner -c cd ") >= 0):
			global found
			found = 1
			break;
	
	if (1 == found):
		time.sleep(1)
		print("Found gitlab_runner")
	else:
		os.system(CMD_GITLAB_RUNNER)
		print("Need start gitlab runner")
		time.sleep(1)

	#Judge whether new firmware generated
	print(fileinfo)
	if ((fileinfo) == (fileinfonew)):
		print("No new file generated")
		time.sleep(1)
	else:
		fileinfo = fileinfonew
		print("####New firmware generated####")
		time.sleep(1)
		send_mail(mailto_list, "新的固件生成啦", "New firmware file generated, please check http://192.168.202.40/firmware")
		
	time.sleep(60)
	
	
