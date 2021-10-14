import pyautogui as pg
import random
import time
from essential_generators import DocumentGenerator

gen = DocumentGenerator()

print(pg.size())
print(pg.position())

pg.click(385, 1010)

arr = ["hi guys!", "how are you guys?", "uncovered gonna be a hit", "wassup?", "uncovered FTW", "love from Asia",
"GG!", "I wanna get into the WL so bad", "LFG", "support uncovered", "yo!", "haha", "lets go to the moon", "this is the NFT era",
"we are going to the moooon!", "I want WL", "WLLLL!", "WLL!", "WL!", "hello!", "lets make this project a hit", "love this art works tho",
"follow, follow, follow", "this is gonna be a lit community ppl", "uncovered !!!", "NFT foreverrr", "WOW", "I love this project", "WAGMI",
"boom!", "fantastic ppl", "let's grind baby", "GRINDDD", "let's grind ppl", "haha", "niceee", "want this", "I want this sooo bad", "mint is coming",
"need this so bad", "dont stop ppl", "we can do this", "keep going", "up up up", "looks dope tho", "LVL10", "lessgooo", "we may have a chance to get into the WL",
"we can do this", "moooooon", "mooooon", "moon", "I want LVL10", "grind so haaard!", "we can do this", "server gone mad!", "you guys rock!",
"gooooooooo", "to the moooooooon", "server is live af", "so many ppl active rm", "damn", "love this server"]

localtime = time.localtime()
random.seed(0)

limit = 1000

for i in range(0, limit):
    result = time.strftime("%I:%M:%S %p", localtime)
    randomWrd = random.choice(arr)
    # randomGen = gen.sentence()
    pg.typewrite(randomWrd, 0.1)
    pg.press("enter")

    print(f"Index {limit - i} -> {result} - {randomWrd}")
    time.sleep(3)

print("\nALL DONE!")