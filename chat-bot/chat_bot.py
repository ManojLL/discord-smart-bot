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
import utils.login.discord_login as discord_login
from bot_init import train_bot
from pickle import load
from time import sleep
import random
import requests
import time

def create_gif_collection(search_terms, limits):
    print("\Searching for GIFs...\n")
    # collection of tenor gifs
    gif = []

    # set the apikey and limit
    apikey = "HO0RLZ3VG2F4"
    
    for i in range(len(search_terms)):
        # search for the term
        r = requests.get("https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (i, apikey, limits))
        if r.status_code == 200:
            # get the json
            json = r.json()
            # get the url
            url = json["results"][0]["media"][0]["gif"]["url"]
            # append the url to the list
            gif.append(url)   
        else:
            print("Error: " + str(r.status_code))
            
    return gif


def retrieve_credentials():
    try:
        frobj = open("../utils/login/credentials.dat", "rb")
        details = load(frobj)
        frobj.close()
        return details
    except:
        return None

def clearscreen():
    system('cls' if osname == 'nt' else 'clear')
    print("\n", "-"*25, "DISCORD CHAT BOT", "-"*25, "\n")

# Opening link and logging in
def login(link, email, passwd):
    # Initialising/Installing Chromedriver
    global driver, flag, templink
    if (flag == False):
        driver = webdriver.Chrome(ChromeDriverManager().install(), service_log_path = None)
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
        flag = True
    sleep(1)
    clearscreen()

# Create spam logs
def create_logs(logs):
    localtime = time.localtime()
    timeStamp = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
    
    with open(f'logs/{timeStamp}.txt', 'w') as file:
        for log in logs:
            file.write(log)
            file.write("\n")

# Starting chat
def chat(n, intervals, chatbot, gif_collection):
    logs = []
    
    print("\nBot Launching...\n")
    with alive_bar(n, title='Chatting', bar='classic2', spinner='classic') as bar:
        for i in range(n):
            token = random.randint(1, 6)
            print(f"token - {token}")
    
            localtime = time.localtime()
            time_stamp = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
    
            random_time = random.choice(intervals)
            random_gif = random.choice(gif_collection)
            
            while True:
                thread = driver.find_elements_by_class_name('messageContent-2qWWxC')
                try:
                    while not thread[-1] == None:
                        break
                    break
                except Exception as e:
                    print(e)
                    pass

            actions = ActionChains(driver)
            
            if (token == 1 or token == 5):
                response = random_gif
            else: 
                response = chatbot.get_response(thread[-1].text)
                
            actions.send_keys(response.text)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            bar()
            sleep(random_time)
            
            logs.append(f'{str(i).zfill(3)} - {random_time}s - {time_stamp} - {response}')
    print("\nAll Messages Sent")
    create_logs(logs)

# Menu
def main():
    global flag
    flag = False
    intervals = []
    gif_words = []
    time_interval = ""

    details = retrieve_credentials()
    chatbot = train_bot()
    
    if (details != None):
        email, passwd = details
    else:
        discord_login.store()
        main()

    try:
        while True:
            clearscreen()
            link = input("\nEnter link to channel: ")

            num_of_msg = int(input("Enter number of messages: "))
            while True:
                time_interval = input("Enter time interval between messages (in seconds): ")
                if (time_interval == "q"):
                    break
                intervals.append(int(time_interval))
                
            num_of_gifs = int(input("Enter number of gifs: "))
            while True:
                related_gif_words = input("Enter related gif words: ")
                if (related_gif_words == "q"):
                    break
                gif_words.append(related_gif_words)
            
            login(link, email, passwd)
            gif_collection = create_gif_collection(gif_words, num_of_gifs)
            chat(num_of_msg, intervals, chatbot, gif_collection)
            
            choice = input("\nDo you want to send more messages (y/n): ")
            if (choice == "n" or choice == "q"):
                break
    except Exception as e:
        print(e)

if __name__ == '__main__':
    driver = ''
    templink = ''
    main()