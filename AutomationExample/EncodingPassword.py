import GetPassword #Safely parsing the username and password 
LoginArgs=GetPassword.main(True,False) 
Password=LoginArgs.password.value

print Password

import cryptography
from cryptography.fernet import Fernet
key = Fernet.generate_key()
file = open('key.key', 'wb')
file.write(key)
file.close()
message = Password.encode()
f = Fernet(key)
encrypted = f.encrypt(message)
file = open('pass', 'wb')
file.write(encrypted)
file.close()
