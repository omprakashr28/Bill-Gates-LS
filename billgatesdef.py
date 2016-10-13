# Adjust Start class timer values
# 
# 
import time, os

commands    = ['help', 'h', 'survey', 's', 'look', 'l', 'grab', 'g', 'inv',
            'i']

inventory   = [] 

enemyname = 'Desk Jockey'

class Start():
    
    def __init__(self):
        
        self.health = 10
        self.attack = 2

        self.heroname  = raw_input(str("What's your name? >  "))

        self.hero       = (self.heroname, health, attack)

        self.intro()
        
    def intro(self):
        
        # Opening Bill Gates dialouge. Will definitely be changed later.
        print billgates1 % (self.heroname, self.heroname, self.heroname)

        raw_input("\nWhat do you think of that? > ")
    
        print "\nOkay then, if you want to do it the hard way."
        print "\nWelcome to Hell %s." % self.heroname
        
        #time.sleep()
        os.system('cls')
        pass
        #self.splash()
        
    #def splash(self):
        # Splash stuff. May change splash time to 10 and adjust spacing.
        #print splash
        #splashTime = 10
        #print "This splash will end in: ",
        #while range (0, splashTime):
            #print str(splashTime) + ' ',
            #splashTime -= 1
            #time.sleep(1)      
            
class Combat(object):

    def __init__(self, Start, floor, enemyname):
        
        #self.hero         = Start.hero
        self.enemyname    = enemyname
        self.floor        = floor
        
    def spawn(self, enemyname):
        
        enemies         = {'Reanimated Keyboard' : (2,1),
                           'Wire Basillisk' : (3,2),
                           'Desk Jockey' : (5,1)}
        
        enemyhealth     = enemies[enemyname][0]
        enemyattack     = enemies[enemyname][1]
        enemy           = (enemyname, enemyhealth, enemyattack)
        
        return enemy
    
    def prompt(self, hero, enemy):

        enemyname       = enemy[0]
        
        os.system('cls')
        print "You're being attacked by a %s!\n" % enemyname
    
        command = raw_input(">  ")
        if command == "help" or command == "h":
            print combathelp
            self.prompt(self, hero, enemy)
        elif command == 'stats' or command == 's':
            self.stats(self, hero, enemy)
            self.prompt(self, hero, enemy)
        elif command == "attack" or command == 'a':
            pass
    
    def stats(self, hero, enemy):
        
        enemyname       = enemy[0]
        enemyhealth     = enemy[1]
        enemyattack     = enemy[2]
        
        heroname        = hero[0]
        herohealth      = hero[1]
        heroattack      = hero[2]
        
        print combatstats % (enemyname, heroname, enemyhealth, herohealth,
                                 enemyattack, heroattack)

def prompter(floor):
    
    # This is definitely one of the most complicated parts of the entire
    # program. Think about more simplification.
    
    # Takes user input and splits it.
    prompt_pass = (raw_input('\n>  ').split())
    if len(prompt_pass) == 0:
        print "\nTry entering a command."
        prompter(floor)
    
    # Defines command and item variables.
    command = prompt_pass[0]
    
    if len(prompt_pass) == 1:
        pass
    elif len(prompt_pass) == 2:
        item = prompt_pass[1]
    else:
        print "Command not recognized."
        prompter(floor)
    
    # help and h
    # define a function later w/ more interactive help.
    if command == commands[0] or command == commands[1]:
        print helpmenu
        prompter(floor)
    
    # survey and s ; basically done.
    elif command == commands[2] or command == commands[3]:
        survey(floor)
        prompter(floor)
    
    # look and l
    elif commands[4] in command or command == commands[5]:
        if len(prompt_pass) == 1:
            print "\nWhat item are you looking at?"
            prompter(floor)
        else:
            look(floor, item)
            prompter(floor)
    
    # grab and g
    elif commands[6] in command or command == commands[7]:
        if len(prompt_pass) == 1:
            print "\nWhat item are you grabbing?"
            prompter(floor)
        else:
            grab(floor, item)
            prompter(floor)
    
    # inventory and i FIX INV REDUNDENCIES
    # same as stated with help menu.
    elif command == commands[8] or command == commands[9]:
        print inventory
        prompter(floor)
        
    else:
        print "Command not recognized."
        prompter(floor)

def survey(floor):
    # will add more if statements for other floors.
    if floor == 1:
        print survey1
    else:
        pass

def look(floor, item):
    # Has to be an easier way to organize these rather than
    # the nesting.
    if floor == 1:
        if item == "DESK":
            print look1desk
            prompter(1)
        elif item == "FIRES":
            print look1fires
        elif item == "DOOR":
            #if dooropen == false:
            print look1door0
            prompter(1)
            #elif open == true:
            #else:
                #pass
            pass

def grab(floor, item):
    if floor == 1:
        if item == 'KEY':
            addinv(inventory, 'KEY')
            print "You grab the %s." % item
        else:
            print "\nYour hand slips."   

def addinv(inventory, item):
        inventory.append(item)

# Below are variable definitions for the look statmeents and 
# survey statments. These WILL be added to and may eventaully have
# their own file.

commands    = ['help', 'h', 'survey', 's', 'look', 'l', 'grab', 'g', 'inv',
            'i']

inventory   = [] 

floor   =   0
health  =   10
attack  =   2
enemyname = 'Desk Jockey'

billgates1      = """
Well hello there, %s. I've been waiting for you - watching you, for
a while now %s. You may be wondering where this voice is coming from.
I'm in your head %s. I have many names, some of them older than others.
But I have a feeling that you may know me best as Bill Gates."""

splash          = """
     (    (     (                                  (
   (   )\ ) )\ )  )\ )   (        (       *   )      )\ )
 ( )\ (()/((()/( (()/(   )\ )     )\    ` )  /( (   (()/(
 )((_) /(_))/(_)) /(_)) (()/(  ((((_)(   ( )(_)))\   /(_))
((_)_ (_)) (_))  (_))    /(_))_ )\ _ )\ (_(_())((_) (_))
 | _ )|_ _|| |   | |    (_)) __|(_)_\(_)|_   _|| __|/ __|
 | _ \ | | | |__ | |__    | (_ | / _ \    | |  | _| \__ \\
 |___/|___||____||____|    \___|/_/ \_\   |_|  |___||___/\n
 *  ~  o ~ + L I T E R A L L Y  S A T A N + ~ o  ~  * 
\n\n\t\t     DISCLAIMER:\n
This game is completely free of charge, unlike most Microsoft
products. All proceeds will be generously donated to the Bill
and Melinda Gates foundation.\n"""

combathelp      = """
+ help (h)\t: Shows this menu.
\t\t  >  help

+ stats (s)\t: Shows your stats and the enemy's stats.
\t\t  >  stats

+ attack (a)\t: Attack the enemy.
\t\t  >  attack

You have a chance to dodge after you attack the enemy! Press 'd' to dodge!
"""

combatstats     = """
Name:\t %s \t %s
Health:\t %r \t %r
Attack:\t %r \t %r
"""

helpmenu        = """
You can type the full command or letter abbreviation.
Examples of use are below the command.

+ help (h)\t: Shows this menu
\t\t  >  help
    
+ survey (s)\t: Survey your environemnt
\t\t  >  survey
    
+ look (l)\t: Look at specific objects
\t\t  >  look DESK
    
+ grab (g)\t: Grab specific objects.
\t\t  >  grab KEY
    
+ inv (i)\t: View inventory screen.
\t\t  >  inv
"""

survey1         = """
 You're surrounded by towering onyx pillars rising high into the
ceiling of a technological palace. There is a welcome DESK without an
employee behind it, which isn't a surprise, because the room is sprayed
with blood. The lighting is sparse, it's night out, and only a few 
scattered FIRES burning on the tile flooring provide any light to the
room. On the wall across the room from you there is a DOOR marked 
"Staff Only." There are a few BODIES on the floor."""

look1desk    	= """
The desk is cluttered with a few tattered papers on top. After you rummage
around it like a good detective, you find a KEY in one of the open drawers.
Under the desk you find a damaged picture of Bill Gates. The frame appears very
ornate and possible gold, but the glass is shattered. On top of the desk there
is an apparently (apparently because of the bullet holes in it) non functional
computer hooked up to a seemingly punched monitor."""

look1fires   	= """
There are many fires blazing around the room. Some of them are burning BODIES
that fill the room with an awful stench. Some of the fires however are,
somewhat curiously, localized to ELECTRONICS."""

look1door0   	= """
The door says "Staff Only" and is locked. Maybe there is a key around!"""

look1door1      = "Please write an look statement for unlocked door."
