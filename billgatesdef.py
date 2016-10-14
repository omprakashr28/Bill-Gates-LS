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

        self.floor = 0 
        
        
        self.intro()
        
    def intro(self):
        
        # Opening Bill Gates dialouge. Will definitely be changed later.
        print billgates1 % (self.heroname, self.heroname, self.heroname)

        raw_input("\nWhat do you think of that? > ")
    
        print "\nOkay then, if you want to do it the hard way."
        print "\nWelcome to Hell %s." % self.heroname
        
        time.sleep(2)
        self.floor = 1
        os.system('clear')
        #self.splash()
        
    def splash(self):
        #Splash stuff. May change splash time to 10 and adjust spacing.
        print splash
        splashTime = 10
        print "This splash will end in: ",
        while range (0, splashTime):
            print str(splashTime) + ' ',
            splashTime -= 1
            time.sleep(1)
                 
class Prompter():

    def __init__(self, floor, c, s):
        
        self.floor = s.floor
        self.dooropen = False
        
        self.commands    = ['help', 'h', 'survey', 's', 'look', 'l', 'grab', 
                            'g', 'inv', 'i', 'use', 'u']
        
        self.item   = ''
        self.item2  = ''
        
        self.inventory   = []
        
        self.health      = c.herohealth
        self.attack      = c.heroattack
        
        self.terminal()
        
    def terminal(self):

        self.prompt_pass = (raw_input('\n>  ').split())
        
        if len(self.prompt_pass) == 0:
            print "\nTry entering a command."
            self.terminal()
            
        # Defines command and item variables.
        self.command = self.prompt_pass[0]
        
        if len(self.prompt_pass) == 1:
            pass
        elif len(self.prompt_pass) >= 2:
            self.item   = self.prompt_pass[1]
        elif len(self.prompt_pass) == 3:
            self.item2  = self.prompt_pass[2]
        else:
            print "Command not recognized."
            self.terminal()
        
        self.redirect()
        
    def redirect(self):
        
        if (self.command == self.commands[0] or
            self.command == self.commands[1]):
            
            print helpmenu
            self.terminal()
    
        # survey and s ; basically done.
        elif (self.command == self.commands[2] or
             self.command == self.commands[3]):
            
            self.survey()
            self.terminal()
        
        # look and l
        elif (self.commands[4] in self.command or
             self.command == self.commands[5]):
            
            if len(self.prompt_pass) == 1:
                print "\nWhat item are you looking at?"
                self.terminal()
            else:
                self.look()
                self.terminal()
        
        # grab and g
        elif (self.commands[6] in self.command or
             self.command == self.commands[7]):
            
            if len(self.prompt_pass) == 1:
                print "\nWhat item are you grabbing?"
                self.terminal()
            else:
                self.grab()
                self.terminal()
        
        # inventory and i FIX INV REDUNDENCIES
        # same as stated with help menu.
        elif (self.command == self.commands[8] or
             self.command == self.commands[9]):
            
            self.inventorygui()
            self.terminal()
         
        elif (self.command == self.commands[10] or
              self.command == self.commands[11]):
          
            self.use()
            #self.terminal()
        
        else:
            print "Invalid command."
            self.terminal()
            
    def survey(self):
        
        if self.floor == 1:
            print survey1
        else:
            self.terminal()
            
    def look(self):
        # Has to be an easier way to organize these rather than
        # the nesting.
        if self.floor == 1:
            if self.item == "DESK":
                print look1desk
                self.terminal()
            elif self.item == "FIRES":
                print look1fires
            elif self.item == "DOOR":
                if self.dooropen == False:
                    print look1door0
                    self.terminal()
                else:
                    print "It's a trap!"
                    Combat.spawn('Desk Jockey') 
                    print "The door is opened!"
            
    def grab(self):
        
        if self.floor == 1:
            if self.item == 'KEY':
                self.inventory.append(self.item)
                print "You grab the %s." % self.item
            else:
                print "\nYour hand slips."
            
    def inventorygui(self):
      
        self.invcount = 0
        
        print "Your stats:"
        print "Health:\t %r" % self.health
        print "Attack:\t %r" % self.attack
        
        print "\nYour inventory:"
        for item in self.inventory:
            print (str(self.invcount + 1) + '.\t' + self.inventory[self.invcount])
            
        if len(self.inventory) == 0:
            print "You have no items in your inventory."
        else:
            pass

    def use(self):
        
        if self.floor == 1 and self.item == 'KEY' and self.item2 == 'DOOR':
            self.dooropen == True
            self.item = 'DOOR'
            self.look()
        else:
            "You can't use that."
            self.terminal()
            

class Combat():

    def __init__(self, floor, enemyname, s):
        
        self.floor        = floor
        
        self.hero        = s.hero
        self.heroname    = s.hero[0]
        self.herohealth  = s.hero[1]
        self.heroattack  = s.hero[2]
        
        self.enemyname    = enemyname
        self.enemyhealth = 0
        self.enemyattack = 0
        
    def spawn(self):

        enemies         = {'Reanimated Keyboard' : (2,1),
                           'Wire Basillisk' : (3,2),
                           'Desk Jockey' : (5,1)}
        
        self.enemyhealth     = enemies[enemyname][0]
        self.enemyattack     = enemies[enemyname][1]
        
        #os.system('clear')
        
        self.prompt()
    
    def prompt(self):
        
        print "You're being attacked by a %s!\n" % self.enemyname
    
        command = raw_input(">  ")
        if command == "help" or command == "h":
            print combathelp
            self.prompt()
        elif command == 'stats' or command == 's':
            self.stats()
            self.prompt()
        elif command == "attack" or command == 'a':
            pass
    
    def stats(self):
        
        print combatstats % (self.enemyname, self.heroname, self.enemyhealth, 
                        self.herohealth, self.enemyattack, self.heroattack)
    
    def attack(self):
        
        if self.enemyhealth != 0:
            self.enemyhealth -= self.heroattack
            print "You hit the  %s  for  %r  HP! It now has  %r  HP." % (
                self.enemyname, self.heroattack, self.enemyhealth)
            
            if self.enemyhealth == 0:
                print "You have slayed a %s! 1" % self.enemyname
            
            else:
                self.herohealth -= self.enemyattack
                print "The %s hits you for %r HP! You now have %r HP." % (
                    self.enemyname, self.enemyattack, self.herohealth)
                
        else:
            print "You have slayed a %s! 0" % self.enemyname
   
                
                
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
Health:\t\t %r \t %r
Attack:\t\t %r \t %r
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

look1desk        = """
The desk is cluttered with a few tattered papers on top. After you rummage
around it like a good detective, you find a KEY in one of the open drawers.
Under the desk you find a damaged picture of Bill Gates. The frame appears very
ornate and possible gold, but the glass is shattered. On top of the desk there
is an apparently (apparently because of the bullet holes in it) non functional
computer hooked up to a seemingly punched monitor."""

look1fires       = """
There are many fires blazing around the room. Some of them are burning BODIES
that fill the room with an awful stench. Some of the fires however are,
somewhat curiously, localized to ELECTRONICS."""

look1door0       = """
The door says "Staff Only" and is locked. Maybe there is a key around!"""

look1door1      = "Please write an look statement for unlocked door."
