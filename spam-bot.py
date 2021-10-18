from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from os import system, name as osname
from progress.bar import ChargingBar
from login import credentials
from pickle import load
from time import sleep
import random
import json

def retrieve_credentials():
    try:
        frobj = open("login/credentials.dat","rb")
        details = load(frobj)
        frobj.close()
        return details
    except:
        return None
    
def clearscreen():
    system('cls' if osname == 'nt' else 'clear')
    print("-"*20, "DISCORD SPAM BOT", "-"*20)

## Opening link and logging in
def login(link,email,passwd):
    ## Initialising/Installing Chromedriver
    global driver, flag, templink
    if (flag == False):
        driver = webdriver.Chrome(ChromeDriverManager().install())
    if (link != templink):
            print("\nLoading Discord...")
            driver.get(link)
            templink = link
    if (flag == False):
        clearscreen()
        myElem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME , 'email')))
        print("\nLogging in...")
        driver.find_element_by_name('email').send_keys(email)
        driver.find_element_by_name('password').send_keys(passwd)
        driver.find_element_by_name('password').send_keys(Keys.RETURN)
        sleep(5)
        print("\nLogged in successfully")
        flag = True
    sleep(1)
    clearscreen()
    
# Retrieve data from the JSON file    
def retrieve_messages():
    with open('phrases/random_phrase.json') as json_file:
        data = json.load(json_file)
    return data

## Starting spam
def spam(n, data):
    timeArr = [3, 4, 5]
    
    with ChargingBar('\nSending Messages', max=n) as bar:
        bar.suffix = '%(percent).1f%% [ %(index)d / %(max)d ]'
        for i in range(n):
            random.shuffle(data)
            random.shuffle(timeArr)
            actions = ActionChains(driver)
            actions.send_keys(random.choice(data))
            actions.send_keys(Keys.ENTER)
            actions.perform()
            bar.next()
            sleep(random.choice(timeArr))
    print("\nAll Messages Sent")

## Menu
def main():
    global flag
    flag = False
    details = retrieve_credentials()
    data = retrieve_messages()
    if (details != None):
        email,passwd = details
    else:
        credentials.store()
        main()
    while True:
        clearscreen()
        link = input("\nEnter link to channel: ")
        n = int(input("Enter number of messages: "))
        login(link,email,passwd)
        spam(n, data)
        choice = input("\nDo you want to send more messages (y/n): ")
        if (choice == "n"):
            break

if __name__ == '__main__':
    driver = ''
    templink = ''
    main()