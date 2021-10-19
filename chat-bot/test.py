import os
import sys

# Restructure path to the script
sys.path.append(os.path.realpath('..'))

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

from os import system, name as osname
from alive_progress import alive_bar
import utils.discord_login as discord_login
from bot_init import train_bot
from pickle import load
from time import sleep
import random
import time


def retrieve_credentials():
    try:
        frobj = open(f"{os.path.abspath('credentials.dat')}", "rb")
        details = load(frobj)
        frobj.close()
        return details
    except:
        return None

def clearscreen():
    system('cls' if osname == 'nt' else 'clear')
    print("\n", "-"*25, "DISCORD SPAM BOT", "-"*25, "\n")

# Opening link and logging in
def login(link, email, passwd):
    # Initialising/Installing Chromedriver
    global driver, flag, templink
    if (flag == False):
        driver = webdriver.Chrome(ChromeDriverManager().install())
    if (link != templink):
        print("\nLoading Discord...\n")
        driver.get(link)
        templink = link
    if (flag == False):
        clearscreen()
        myElem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, 'email')))
        print("\nLogging in...")
        driver.find_element_by_name('email').send_keys(email)
        driver.find_element_by_name('password').send_keys(passwd)
        driver.find_element_by_name('password').send_keys(Keys.RETURN)
        sleep(5)
        print("\nLogged in successfully")
        
        messages = driver.find_element_by_class_name('slateTextArea-1Mkdgw').send_keys("test msg", Keys.ENTER)
        posts = driver.find_elements_by_class_name('messageContent-2qWWxC')
        nextMsg = len(posts)
        
        while True:
            posts = driver.find_elements_by_class_name('messageContent-2qWWxC')
            try:
                while not posts[nextMsg] == None:
                    break
                break
            except Exception as e:
                pass
        response = posts[nextMsg].text
        driver.find_element_by_class_name('slateTextArea-1Mkdgw').send_keys(response, Keys.ENTER)
    sleep(1)

# Menu
def main():
    global flag
    flag = False
    intervals = []
    time_interval = ""

    details = retrieve_credentials()
    
    if (details != None):
        email, passwd = details
    else:
        discord_login.store()
        main()

    try:
        while True:
            link = input("\nEnter link to channel: ")
            login(link, email, passwd)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    driver = ''
    templink = ''
    main()