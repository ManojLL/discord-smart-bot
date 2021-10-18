from pickle import dump
from time import sleep

def store():
    email = input("\nEnter discord E-mail address: ")
    passwd = input("Enter password: ")
    fwobj = open("./login/credentials.dat","wb")
    dump((email,passwd),fwobj)
    fwobj.close()
    print("\nCredentials stored successfully")
    sleep(1)

if __name__ == '__main__':
  store()