#import hashlib

#sha = hashlib.sha1(b'Hi Niall!').hexdigest()

import passlib
import json

from passlib.context import CryptContext

pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)
# Password123!
logged_in = False
attempts = 0
max_attempts = 3

### SECRET PASSWORD FUNCTIONS ###

def encrypt_password(pwd):
    return pwd_context.hash(pwd)

def verify_encrypted_password(pwd, enc_pwd):
    return pwd_context.verify(pwd, enc_pwd)

def set_password():
	pwd = input('Enter a new Password: \n')
	encrypted_pwd = encrypt_password(pwd)
	f = open("res/enc_pwd.txt", "w")
	f.write(encrypted_pwd)
	f.close

def read_password():
	
	f = open("res/enc_pwd.txt", "r")
	enc_pwd = f.read()
	f.close
	return enc_pwd

def enter_password():
	pwd = input('Please enter your Password: \n')
	print("Checking pasword.....")
	return verify_encrypted_password(pwd, read_password())

### SERVICES ###

def get_services():
    with open('res/services.txt') as file:
        services = json.load(file)
        return services

def get_services_list(services):
	return services.keys()

def get_password_for_service(services, service):
	try:
		return services[service]
	except:
		return('error retrieveing password for ' + service)


def add_service(services, service, password):
	# Add additional Checks
	try:
		if service in services.keys():
			overwrite = False 
			ans = input('Service already exists, do you want to overwrite (yes/no)')
			if ans.lower() == 'yes':
				services[service] = password
				print('Password changed succesfully')
			else:
				print('Password change unsuccesfull')
		
		else:
			services[service] = password
			print('Password changed succesfully')

	except:
		return('error adding service ' + service)

def remove_service(services, service):
	try:
		del services[service]
	except:
		return('error removing service ' + service)

def write_updated_services(updated_services):
	print('updated file: ', end=' ')
	print(updated_services)
	with open('res/services.txt', 'w') as file:
		file.write(json.dumps(updated_services))

# def encrypt_password(service, decrypted_password):
#

# def decrypt_password(service, encrypted_password):
#

if __name__ == "__main__":
	
	print("Working....")

	while attempts < max_attempts and not logged_in:

		if enter_password():
			logged_in  = True
			print('We are in!')

			while(logged_in):
				
				action = input('What do you want to do? (getservices/addservice/removeservice/getpassword/quit)')
				services = get_services()

				if action == 'getservices':
					services_list = get_services_list(services)
					for key in services_list:
						print(key)
					
				if action == 'addservice':
					add_service(services, 'facebook', 'Hit me Mark!!!')
					write_updated_services(services)

				if action == 'removeservice':
					remove_service(services, 'gmail')
					write_updated_services(services)
					
				if action == 'getpassword':
					print(get_password_for_service(services,'facebook'))

				if action == 'quit':
					logged_in = False
					print('Bye for now! :D')

		else:
		
			print('Incorrect Password')
			attempts += 1

	if attempts==max_attempts: print('Fuck off you hacker!!!')
#	while attempts < max_attempts and not succesful_login:

#	if enter_password():
#		succesful_login  = True
#		print('We are in!')

		
#	else:
		
#		print('Incorrect Password')
#		attempts += 1

#	if not succesful_login: print('Fuck off you hacker!!!')













#set_password()
# IMPORTANT

