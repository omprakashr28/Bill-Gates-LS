# Need to implement grab and inv

from billgatesdef import *

os.system('cls')

floor   =   0
item    =   0
health  =   10

hero_name = raw_input("What is your name? > ")

if floor == 0:
    gamestart(hero_name, floor)
    floor += 1
    prompter(floor)
else:
    prompter(floor)    
