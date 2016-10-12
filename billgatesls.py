# Need to implement grab and inv

from billgatesdef import *

os.system('cls')

floor = 1
item = 0

hero_name = raw_input("What is your name? > ")

if floor == 0:
    gamestart(hero_name, floor)
    floor += 1
    prompter(floor)
else:
    prompter(floor)    