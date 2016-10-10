# REMINDERS:
# 1. Change the start level timer back to 15.
# 2. 
#
#
import time, os
def dscreaders(rlines):
    with open("descriptions.txt") as f:
        content = f.readlines()
    
        
def gamestart(hero_name, level):

    print """\n\tWell hello there, %s. I've been waiting for you - watching you, for
a while now %s. You may be wondering where this voice is coming from.
I'm in your head %s. I have many names, some of them older than others.
But I have a feeling that you may know me best as Bill Gates.""" % (hero_name,
        hero_name, hero_name)

    raw_input("\nWhat do you think of that? > ")

    print "\nOkay then, if you want to do it the hard way."
    print "\nWelcome to Hell %s." % hero_name

    time.sleep(2)
    os.system('cls')

    # Just look at this splash oh my goodness
    print """
     (    (     (                                  (
   (   )\ ) )\ )  )\ )   (        (       *   )      )\ )
 ( )\ (()/((()/( (()/(   )\ )     )\    ` )  /( (   (()/(
 )((_) /(_))/(_)) /(_)) (()/(  ((((_)(   ( )(_)))\   /(_))
((_)_ (_)) (_))  (_))    /(_))_ )\ _ )\ (_(_())((_) (_))
 | _ )|_ _|| |   | |    (_)) __|(_)_\(_)|_   _|| __|/ __|
 | _ \ | | | |__ | |__    | (_ | / _ \    | |  | _| \__ \\
 |___/|___||____||____|    \___|/_/ \_\   |_|  |___||___/
    """
    print " *  ~  o ~ + L I T E R A L L Y  S A T A N + ~ o  ~  * "
    print """\n\n\t\t     DISCLAIMER:\n
This game is completely free of charge, unlike most Microsoft
products. All proceeds will be generously donated to the Bill
and Melinda Gates foundation.\n"""
    splashTime = 10
    print "This splash will end in:   ",
    for i in range (0, splashTime):
        print str(splashTime),
        splashTime -= 1
        time.sleep(1)
        if i == 1:
            level += 1
    os.system('cls')

    pass
def prompter(level):
    prompt_pass = (raw_input('\n>  ').split())
    
    if len(prompt_pass) == 1:
        command = prompt_pass[0]
    elif len(prompt_pass) == 2:
        item = prompt_pass[1]
        command = prompt_pass[0]
    else:
        prompter(level)
    
    print prompt_pass
    
    if command == commands[0] or command == commands[1]:
        print "Commands:", commands
        prompter(level)
    elif command == commands[2] or command == commands[3]:
        survey(level)
        prompter(level)
    elif commands[4] in command or commands[5] in command:
        item = prompt_pass[1]
        inspect(level, item)
        prompter(level)
    else:
        print "I don't recognize that command, sorry."
        prompter(level)
def survey(level):
    if level == 1:
        print """
        You're surrounded by towering onyx pillars rising high into the
        ceiling of a technological palace. There is a welcome DESK without an
        employee behind it, which isn't a surprise, because the room is sprayed
        with blood. The lighting is sparse, it's night out and only a few 
        scattered FIRES burning on the tile flooring provide any light to the
        room. On the wall a hundred feet from you there is a DOOR marked 
        "Staff Only." There are a few BODIES on the floor.
        """
    else:
        pass
def inspect(level, item):
    if level == 1:
        if item == "DESK":
            print """
The desk is cluttered with a few tattered papers on top. After you rummage
around it like a good detective, you find a KEY in one of the open drawers.
Under the desk you find a damaged picture of Bill Gates. The frame appears very
ornate and possible gold, but the glass is shattered. On top of the desk there
is an apparently (apparently because of the bullet holes in it) non functional
computer hooked up to a seemingly punched monitor.
            """
            prompter(1)
        elif item == "FIRES":
            pass
        elif item == "DOOR":
            #if dooropen == false:
            print 'The door says "Staff Only" and is locked.'
            prompter()
            #elif open == true:
            #else:
                #pass
###############################################################################
      
os.system('cls')

commands = ['help', 'h', 'survey', 's', 'inspect', 'i']

level = 1
item = 0

hero_name = raw_input("What is your name? > ")
dscreaders(4)
if level == 0:
    gamestart(hero_name, level)
    level += 1
    prompter(level)
else:
    prompter(level)    
