from cryptography.fernet import Fernet

key = Fernet.generate_key()

f = Fernet(key)

def encrypt():
	with open('mykey.txt','wb') as mykey:
		mykey.write(key)
	with open('test.webp','rb') as encr:
		filedata = encr.read()
	encrdata = f.encrypt(filedata)
	with open('en_test.webp','wb') as newfile:
		newfile.write(encrdata)
		
encrypt()

def decrypt():
	with open('mykey.txt','rb') as keydata:
		key = keydata.read()
	
	f = Fernet(key)
	with open('en_test.webp','rb') as encr:
		filedata = encr.read()
	decryptdata = f.decrypt(filedata)
	with open('de_test.webp','wb') as newfile:
		newfile.write(decryptdata)
		
decrypt()
	

