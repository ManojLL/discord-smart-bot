import pyautogui as pg
import random
import time
from essential_generators import DocumentGenerator

gen = DocumentGenerator()

print(pg.size())
print(pg.position())

pg.click(385, 1010)

# arr = ["uncovered gonna be a hit", "uncovered FTW",
# "GG!", "LFG", "support uncovered", "yo!", "haha", "lets go to the moon",
# "we are going to the moooon!", "lets make this project a hit", "love this art works tho",
# "this is gonna be a lit community ppl", "uncovered !!!", "NFT foreverrr", "WOW", "I love this project", "WAGMI",
# "boom!", "fantastic ppl", "let's grind baby", "GRINDDD", "let's grind ppl", "haha", "niceee", "want this", "I want this sooo bad", "mint is here",
# "need this so bad", "dont stop ppl", "we can do this", "keep going", "up up up", "looks dope tho", "LVL10", "lessgooo",
# "we can do this", "moooooon", "mooooon", "moon", "GL reaching LVL10", "keep grinding ppl!", "we can do this", "server is mad rn!", "you guys rock!",
# "gooooooooo", "to the moooooooon", "server is live af", "love this server", "the hype is real", "uncocvred project is awesome",
# "fasted growing community ever", "lets go fam!", "really hope I to get in touch with 1/1", "love these sneak peak", "this is an awesome project", "just keep grinding"]

arr = ["this is gonna be a hit", "LFG", "lets make this project a hit", "love this art works tho", "I love this project", "WAGMI", "let's grind baby", "GRINDDD", "let's grind ppl", "I want this sooo bad", "niceee", 
"dont stop ppl", "we can do this", "keep going", "yeah, it looks dope tho", "LVL20 here I come", "lessgooo", "keep grinding ppl!", "we can do this", "server is mad rn!", "you guys rock!", "we can hit the moon",
"mooooon", "gooooooooo ppl we can do this", "server is live af", "love this server", "the hype is real", "uncocvred project is awesome", "lets go fam!", "love these sneak peak", "this is an awesome project",
"just keep grinding", "this is gonna be a hella community", "imagine if you can hold a NFT helment, damn!", "that's nice tho", "i really Like that idea", "keep going, you can do this my friend", "hey newbie, wassup?"]

random.seed(0)
limit = 1000

def getRandomTime():
    timeArr = [5, 6, 7]
    return random.choice(timeArr)

for i in range(0, limit):
    localtime = time.localtime()

    timeStamp = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
    randomWrd = random.choice(arr)
    randomTime = getRandomTime()

    # randomGen = gen.sentence()
    pg.typewrite(randomWrd, 0.1)
    pg.press("enter")

    print(f"{str(i).zfill(3)} - {randomTime}s - {timeStamp} - {randomWrd}")
    time.sleep(randomTime)

print("\nALL DONE!")