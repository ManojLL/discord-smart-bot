import pyautogui as pg
import random
import time
import json

print(f'Screen - {pg.size()}')
print(f'Mouse  - {pg.position()}')

pg.click(385, 1010)

random.seed(0)
limit = 1000

with open('random_phrase.json') as json_file:
    data = json.load(json_file)

def getRandomTime():
    # timeArr = [30, 45, 60]
    timeArr = [3, 4, 5]
    random.shuffle(timeArr)
    return random.choice(timeArr)

for i in range(0, limit):
    localtime = time.localtime()
    timeStamp = time.strftime('%Y-%m-%d %H:%M:%S', localtime)

    random.shuffle(data)
    randomWrd = random.choice(data)
    randomTime = getRandomTime()

    # pg.typewrite(randomWrd, 0.1)
    # pg.press("enter")

    print(f"{str(i).zfill(3)} - {randomTime}s - {timeStamp} - {randomWrd}")
    time.sleep(randomTime)

print("\nALL DONE!")