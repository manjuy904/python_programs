#Password manager!

from cryptography.fernet import Fernet

#key = Fernet.generate_key()
#f = Fernet(key)
#token = f.encrypt(b"my dark scret")
#token
#b'........'
#f.decrypt(token)
#b"my dark scret"

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
      key_file.write(key)'''
      
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

#master_pwd = input("What is the master password: ")
#key = load_key() + master_pwd.encode()
key = load_key()
fer = Fernet(key)


def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
#            print(line.rstrip())
             data = line.rstrip()
             user, passw = data.split("|")
             print("User: ", user, "| Password: ", fer.decrypt(passw.encode()).decode())
             
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
 
    with open("password.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("would you like to add a new password or view existing ones (view, add), press q to quit: ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue