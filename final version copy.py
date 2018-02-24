from math import *
from random import *
import time
## player stats
playerhealth = 5000
playerattack = 100
name = ""

## xp points
playerxpgreen = 0
playerxpred = 0
playerxpblue = 0

##gold
playergold = 10

## level of stuff
playerarmourlevel = 0
nameplayerarmourlevel = "basic"
playerswordlevel = 0
nameplayerswordlevel = "basic"

## non specific stats
room = 0

## special abilites
heal = 0
rangedattack = 0

##physical atributes
speedlevel = 0
strength = 0
sworddamageability = 0


def myRoundingFunction(x, n):
    return math.ceil(x * math.pow(10, n)) / math.pow(10, n)

def clearscreen():
    clearscreen = 4
    while clearscreen != 0:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        clearscreen = clearscreen - 2


def battle():
    global playerhealth
    global playerattack
    global name
    global playerxpgreen
    global playerxpred
    global playerxpblue
    global playergold
    global playerarmourlevel
    global playerswordlevel
    global room
    global heal
    global rangedattack
    global speedlevel
    global strength
    global sworddamageability

    ## generating monster stats

    if room <= 5:
        enemyhealth = randint(300, 500)
        enemydamage = randint(50, 100)

    elif 5 < room <= 10:
        enemyhealth = randint(500, 1000)
        enemydamage = randint(150, 200)

    elif 10 <= room <= 15:
        enemyhealth = randint(1000, 2000)
        enemydamage = randint(200, 3020)

    else:
        enemyhealth = 3, 500
        enemydamage = 300

    ## possibly add some more intros into the random generator
    ## random room intro generator
    roomintro = ["as you enter the door slames closed behind you then from knowhere you hear",
                 "you cautiously aproach the middle of the room expecting something to be there and \nyou were right from behind you hear",
                 "as you enter the room you find yourself drawn towards the shining gem in the middle \nbut it dissapears and you realise that it was all a trap you hear behind you",
                 "as you enter you see along the walls the skulls of previous adverturers  \nyou then see the massive beast lurking in the corner it says",
                 "the room shakes violently and from the ground rises a monster it shouts at you",
                 "you enter the room and imediatly spy the most hideous monster you have every seen \nit screams at you",
                 "you find as you enter the room slopes down and you start to fall \nafter about 10 seconds of falling \nyou enter another room but this time there is a massive monster inside it says"]
    shuffle(roomintro)
    intro1 = roomintro[0]

    ## random name generator
    monstername = ['Afrit', 'Alfar', 'Amphisbaena', 'Ananta', 'Anka', 'Anthropophagus', 'Ant-Lion', 'Arimaspians',
                   'Aspidoceleon', 'Astomi', 'Barnacle-Goose', 'Basilisk', 'Bean Sidh', 'Blemiyeh', 'Brownie',
                   'Bucentaur', 'Caladrius', 'Callitrice', 'Canocephalus', 'Capricorn', 'Caristae', 'Catoblepas',
                   'Cecrops', 'Centaur', 'Cerberus', 'Charadrius', 'Cheiron', 'Chemosit', 'Chimera', 'Cinamon Bird',
                   'Criosphinx', 'Crocotta', 'Cockatrice', 'Cyclops', 'Cynocephali', 'Dhampir', 'Djinni', 'Djinniyeh',
                   'Domovoi', 'Dragon', 'Dragonhorse', 'Dryad', 'Dwarf', 'Echeneis', 'Echidna', 'Elf', 'Ekimmu',
                   'Ercinee', 'Ettin', 'Faun ', 'Fenris Wolf', 'Frost-Giant', 'Gargoyle', 'Garm', 'Garuda', 'Ghul',
                   'Glaistig', 'Hamadryad']
    shuffle(monstername)
    monster = monstername[0]

    ## random monster intro generator
    ## add more at later date
    monsterintro = ["your destroyer", "you will die at my hands"]
    shuffle(monsterintro)
    intro = monsterintro[0]
    print("\n")
    print("#############################################################################################")
    print(intro1, " \nI am", monster, intro)
    print("#############################################################################################")
    print("\n")

    ##  pause
    time.sleep(5)

    ## printing the description of the monster
    ## room 0-5
    if room <= 5:
        if enemyhealth <= 400:
            health = "low"
        else:
            health = "high"

        if enemydamage <= 75:
            attack = "low"

        else:
            attack = "high"
            ## room 5-10
    elif 5 < room <= 10:
        if enemyhealth <= 750:
            health = "low"
        else:
            health = "high"

        if enemydamage <= 175:
            attack = "low"

        else:
            attack = "high"

            ## room 10-15
    elif 10 < room <= 15:
        if enemyhealth <= 1500:
            health = "low"
        else:
            health = "high"

        if enemydamage <= 200:
            attack = "low"

        else:
            attack = "high"

    print("\n")
    print("#############################################################################################")
    print("you study the monster carefully and you think that it has", health, "health and", attack, "attack")
    print("#############################################################################################")
    print("\n")

    ## pause
    time.sleep(3)

    ## more info about monster possibly
    print("\n")
    print("#############################################################################################")
    print("would you like to learn more about the monster (yes) (no) ")
    print("#############################################################################################")
    print("\n")
    question1 = input("").lower()
    x = 1
    y = 0

    if question1 == "yes":
        print("\n")
        print("#############################################################################################")
        print("this will cost 1 gold are you sure (yes) (no) ")
        print("#############################################################################################")
        print("\n")
        question4 = input("").lower
        if question4 == "no":
            question2 = 0
            question3 = 100
            x = 0
            y = 0
        elif playergold != 0:
            print("\n")
            print("#############################################################################################")
            print("chose a number between 15 and 0 ")
            print("#############################################################################################")
            print("\n")
            question2 = int(input(""))

        elif playergold == 0:
            print("\n")
            print("#############################################################################################")
            print("this will cost 1 gold are you sure (yes) (no) ")
            print("#############################################################################################")
            print("\n")

        question3 = randint(0, 15)
        if question2 <= question3 and playergold != 0:
            print("\n")
            print("#############################################################################################")
            print("you were succesfull at working out the monster stats")
            print("the monster has", enemyhealth, "health and", enemydamage, "damadge")
            print("press enter to continue")
            print("#############################################################################################")
            y = 1
            playergold = playergold - 1
            print("\n")
            question6 = input("")

        elif question3 <= question2:
            print("\n")
            print("#############################################################################################")
            print("unfortunatly you were unable to work out the monsters stats")
            print("press enter to contiune")
            print("#############################################################################################")
            print("\n")
            playergold = playergold - 1
            question6 = input("")



            ## main fight
            ## display health of you or monster
    b = 0
    a = 0
    c = 0
    while playerhealth != 0 and enemyhealth != 0 and b != 1:

        x = x + 1
        if x >= 5:
            x = 5
        z = 0
        e = 0
        d = 0

        clearscreen()
        print("\n")
        print("#############################################################################################")
        print("you have", playerhealth, "health and", playerattack, "attack")
        if y == 1:
            print("the monster has", enemyhealth, "health and", enemydamage, "attack")
        else:

            ## room 0-5
            if room <= 5:
                if enemyhealth <= 400:
                    health = "low"
                else:
                    health = "high"

                if enemydamage <= 75:
                    attack = "low"

                else:
                    attack = "high"
                    ## room 5-10
            elif 5 < room <= 10:
                if enemyhealth <= 750:
                    health = "low"
                else:
                    health = "high"

                if enemydamage <= 175:
                    attack = "low"

                else:
                    attack = "high"

                    ## room 10-15
            elif 10 < room <= 15:
                if enemyhealth <= 1500:
                    health = "low"
                else:
                    health = "high"

                if enemydamage <= 200:
                    attack = "low"

                else:
                    attack = "high"
            print("the monster has", health, "health and", attack, "attack")
        print("#############################################################################################")
        print("\n")

        ## choice of attack

        print("\n")
        print("#############################################################################################")
        print("what would you like to do")
        print("type ? if you don't know what to type")
        print("#############################################################################################")
        print("\n")

        question5 = input("")

        if question5 == "?":
            print("\n")
            print("#############################################################################################")
            print("type attack to attack the monster")
            print("type special ability to use a special ability")
            print("type run to attempt to run away ")
            print("type block to attempt to block the attack")
            print("type auto to have the battle fought for you")
            print("press enter when done")
            print("#############################################################################################")
            print("\n")
            e = 1
            question6 = input("")

        if question5 == "attack":

            if sworddamageability == 1:
                times = 1.5
            if sworddamageability == 2:
                times = 2
            else:
                times = 1

            if c == 1:
                times = times + 1.5

            actualattack = playerattack * times

            percentage = randint(50, 100)

            actualattack2 = percentage / actualattack
            actualattack2 = actualattack2 * 100
            actualattack2 = myRoundingFunction(actualattack2, 0)
            enemyhealth = enemyhealth - actualattack2

            print("\n")
            print("#############################################################################################")
            print("you attack the monster you deal", actualattack2, "damage")
            print("press enter to continue")
            print("#############################################################################################")
            print("\n")

            question6 = input("")

        if question5 == "special":
            if x == 5:
                print("\n")
                print("#############################################################################################")
                print("which special move would you like to make (heal) or (ranged attack)")
                print("#############################################################################################")
                print("\n")

                question7 = input("")

                if question7 == "heal":
                    if playerhealth < 5000:
                        playerhealth = playerhealth + 500
                    print("\n")
                    print(
                        "#############################################################################################")
                    print("you now have", playerhealth)
                    print("press enter when done")
                    print(
                        "#############################################################################################")
                    print("\n")
                    quesiton6 = input("")

                if question7 == "ranged attack":

                    z = 1

                    if sworddamageability == 1:
                        times = 1.5
                    if sworddamageability == 2:
                        times = 2
                    else:
                        times = 1
                    actualattack = playerattack * times

                    percentage = randint(50, 100)

                    actualattack2 = percentage / actualattack

                    actualattack2 = myRoundingFunction(actualattack2, 0)

                    enemyhealth = enemyhealth - actualattack2

                    print("\n")
                    print(
                        "#############################################################################################")
                    print("you deal", actualattack2)
                    print("press enter when done")
                    print(
                        "#############################################################################################")
                    print("\n")
                    quesiton6 = input("")
            else:

                print("\n")
                print(
                    "#############################################################################################")
                time1 = 5 - x
                print("you have to weight for", time1, "turns")
                print(
                    "#############################################################################################")
                print("\n")

        if question5 == "run":

            if a != 1:
                e = 1
                a = 1
                print("\n")
                print("#############################################################################################")
                print("you attempt to run away")
                question8 = randint(0, 100)
                if speedlevel == 0:
                    time.sleep(2)
                    if question8 >= 90:
                        print("you were unsucesfull at running away")
                    else:
                        print("you succesfully run away")
                        b = 1

                if speedlevel == 1:
                    time.sleep(2)
                    if question8 >= 80:
                        print("you were unsucesfull at running away")
                    else:
                        print("you succesfully run away")
                        b = 1

                if speedlevel == 2:
                    time.sleep(2)
                    if question8 >= 60:
                        print("you were unsucesfull at running away")
                    else:
                        print("you succesfully run away")
                        b = 1

                if speedlevel == 3:
                    time.sleep(2)
                    if question8 >= 50:
                        print("you were unsucesfull at running away")
                    else:
                        print("you succesfully run away")
                        b = 1
                print("press enter when done")
                print("#############################################################################################")
                print("\n")

                question6 = input("")

        if question5 == "block":
            d = 1

        if question5 == "auto":
            print("\n")
            print("#############################################################################################")
            print("the auto attack will simply bash it out with the monster using no special abilitys")
            print("are you sure that you want to do this? (yes) or (no)")
            print("#############################################################################################")
            print("\n")
            question9 = input("")

            if question9 == "yes":

                while playerhealth != 0 or enemyhealth != 0:

                    if sworddamageability == 1:
                        times = 1.5

                    if sworddamageability == 2:
                        times = 2

                    else:
                        times = 1

                    actualattack = playerattack * times

                    percentage = randint(50, 100)

                    actualattack2 = percentage / actualattack

                    actualattack2 = actualattack * 100

                    actualattack2 = myRoundingFunction(actualattack2, 0)

                    enemyhealth = enemyhealth - actualattack2

                    print("you deal", actualattack2)

                    if y == 1:

                        print("the monster has", enemyhealth, "health and", enemydamage, "attack")

                    else:

                        ## room 0-5
                        if room <= 5:
                            if enemyhealth <= 400:
                                health = "low"
                            else:
                                health = "high"

                            if enemydamage <= 75:
                                attack = "low"

                            else:
                                attack = "high"
                                ## room 5-10
                        elif 5 < room <= 10:
                            if enemyhealth <= 750:
                                health = "low"
                            else:
                                health = "high"

                            if enemydamage <= 175:
                                attack = "low"

                            else:
                                attack = "high"

                                ## room 10-15
                        elif 10 < room <= 15:
                            if enemyhealth <= 1500:
                                health = "low"
                            else:
                                health = "high"

                            if enemydamage <= 200:
                                attack = "low"

                            else:
                                attack = "high"

                        print("the monster has", health, "health and", attack, "attack")

                    percentage = randint(50, 100)

                    enemydamage1 = percentage / enemydamage

                    enemydamage1 = enemydamage1 * 100

                    enemydamage1 = myRoundingFunction(enemydamage1, 0)

                    playerhealth = playerhealth - enemydamage1

                    print("the monster deals", enemydamage1)
                    print("you now have", playerhealth)

            else:
                e = 1

        if e != 1:
            print("\n")
            print("#############################################################################################")
            print("it is the monsters turn to attack")

            if z == 1:
                print("the monster misses it attack")

            elif d == 1:
                percentage1 = randint(0, 50)

                percentage = randint(50, 100)

                damage1 = percentage / enemydamage

                damage1 = damage1 / percentage1

                damage1 = damage1 * 100

                damage1 = myRoundingFunction(damage1, 0)

                playerhealth = playerhealth - damage1

                c = 1

                print("the monster deals", damage1, "to you")

            else:

                percentage = randint(50, 100)

                damage1 = percentage / enemydamage

                damage1 = damage1 * 100

                damage1 = myRoundingFunction(damage1, 0)

                playerhealth = playerhealth - damage1

                print("the monster deals", damage1)

            print("press enter when done")
            print("#############################################################################################")
            print("\n")
            quesiton6 = input("")

    print("\n")
    print(
        "#############################################################################################")
    print("you have sucessfully killed the monster", monstername)
    if room <= 5:
        playerxpgreen = playerxpgreen + 3
        xptype = "green"

    elif 5 < room <= 10:
        playerxpred = playerxpred + 3
        xptype = "red"

    elif 10 <= room <= 15:
        playerxpblue = playerxpblue + 3
        xptype = "blue"
    print("you have gained 3", xptype, "xp")
    print(
        "#############################################################################################")
    print("\n")


def armourlevel():
    global playerarmourlevel
    global playergold
    global playerxpgreen
    global playerxpred
    global playerxpblue
    global nameplayeramourlevel

    print("\n")
    print(
        "#############################################################################################")
    print("the armour level is linked to both strength and speed")
    if playerarmourlevel == 3:
        print("your armour is already maxed ")
        print("press enter when done")
    else:
        print("your armour level is currently", playerarmourlevel)
        print("would you like to upgrade it (yes) or (no)")
    print(
        "#############################################################################################")
    print("\n")
    question1 = input("")

    if question1 == "yes" and playerarmourlevel != 3:
        if playerarmourlevel == 0 and playergold >= 10 and playerxpgreen >= 2:
            playergold = playergold - 10
            playerxpgreen = playerxpgreen - 2
            playerarmourlevel = playerarmourlevel + 1
            nameplayerarmourlevel = "leaves"

        if playerarmourlevel == 1 and playergold >= 20 and playerxpred >= 2:
            playergold = playergold - 20
            playerxpred = playerxpred - 2
            playerarmourlevel = playerarmourlevel + 1
            nameplayerarmourlevel = "iron"

        if playerarmourlevel == 2 and playergold >= 40 and playerxpblue >= 2:
            playergold = playergold - 20
            playerxpblue = playerxpblue - 2
            playerarmourlevel = playerarmourlevel + 1
            nameplayerarmourlevel = "diamond"

        print("\n")
        print(
            "#############################################################################################")
        print(" you have upgraded you speed skill it is now level", speedlevel)
        print(
            "#############################################################################################")
        print("\n")
    elif question1 == "yes":

        print("\n")
        print(
            "#############################################################################################")
        print("you do not have the requried levels/resources")
        print(
            "#############################################################################################")
        print("\n")


def sworddamage():
    global sworddamageability
    global strength
    global speedlevel
    global playerxpred
    print("\n")
    print(
        "#############################################################################################")
    print(" the sword damgae ability is linked to both strength and sword skill")
    if sworddamageability == 2:
        print("you are already maxed on this skill")
        print("press enter when done")
    else:
        print(" your current sword damgae ability is level", sworddamageability, )
        print("would you like to upgrade that ability (yes) (no)")
    print(
        "#############################################################################################")
    print("\n")

    quesiton12 = input("")

    if quesiton12 == "yes" and speedlevel >= 1 and strength >= 1 and playerxpred >= 2:
        sworddamageability = sworddamageability + 1
        print("\n")
        print(
            "#############################################################################################")
        print("your sword skill is now level", sworddamageability, )
        print(
            "#############################################################################################")
        print("\n")

    elif quesiton12 == "yes" and speedlevel >= 2 and strength >= 2 and playerxpblue >= 2:
        sworddamageability = sworddamageability + 1
        print("\n")
        print(
            "#############################################################################################")
        print("your sword skill is now level", sworddamageability, )
        print(
            "#############################################################################################")
        print("\n")

    elif quesiton12 == "yes":

        print("\n")
        print(
            "#############################################################################################")
        print("you don't have the level/resources")
        print(
            "#############################################################################################")
        print("\n")



def shop():
    global playerhealth
    global playerattack
    global name
    global playerxpgreen
    global playerxpred
    global playerxpblue
    global playergold
    global playerarmourlevel
    global playerswordlevel
    global room
    global heal
    global rangedattack
    global speedlevel
    global strength
    global sworddamageability
    global nameplayerswordlevel
    global nameplayerarmourlevel

    ## creates a villager name
    villagername = ['Sophia', 'Emma', 'Olivia', 'Isabella', 'Ava', 'Lily', 'Zoe', 'Chloe', 'Mia', 'Madison', 'Emily',
                    'Ella', 'Madelyn', 'Abigail', 'Aubrey', 'Addison', 'Avery', 'Layla', 'Hailey', 'Amelia', 'Hannah',
                    'Charlotte', 'Kaitlyn', 'Harper', 'Kayle', 'Sophie', 'Mackenzie', 'Peyton', 'Riley', 'Grace',
                    'Brooklyn', 'Sarah', 'Aaliyah', 'Anna', 'Arianna', 'Ellie', 'Natalie', 'Isabelle', 'Lillian',
                    'Evelyn', 'Elizabeth', 'LylaLucy', 'Claire', 'Makayla', 'Kylie', 'Audrey', 'Maya', 'Leah',
                    'Gabriella', 'Annabelle', 'Savannah', 'Nora', 'Reagan', 'Scarlett', 'Samantha', 'Alyssa', 'Allison',
                    'Elena', 'Stella', 'Alexis', 'Victoria', 'Aria', 'Molly', 'Maria', 'Bailey', 'Sydney', 'Bella',
                    'Mila', 'Taylor', 'Kayla', 'Eva', 'Jasmine', 'Gianna', 'Alexandra', 'Julia', 'Eliana', 'Kennedy',
                    'Brianna', 'Ruby', 'Lauren', 'Alice', 'Violet', 'Kendall', 'Morgan', 'Caroline', 'Piper', 'Brooke',
                    'Elise', 'Alexa', 'Sienna', 'Reese', 'Clara', 'Paige', 'Kate', 'Nevaeh', 'Sadie', 'Quinn', 'Isla',
                    'Eleanor']
    shuffle(villagername)
    name = villagername[0]

    ## creates a shop introduction
    ## possibly add more
    shopintro = [
        'As you enter the cave \nyou find a young shopkeeper, sitting behind a long wooden table with a brightly painted sign',
        'As you enter the cave \nyou see a little old person sitting behind a counter with a vast display of items',
        'As you enter the room \nyou see a young shopkeeper standing behind a counter \non the counter there are some bottles with mysterious looking liquids inside, and some armour']
    shuffle(shopintro)
    intro = shopintro[0]

    ## prints the introduction

    print("\n")
    print("#############################################################################################")
    print(intro)
    print("#############################################################################################")
    print("\n")

    time.sleep(4)

    print("\n")
    print("#############################################################################################")
    print("hello im", name, "i run the shop")
    ## aks what they want

    x = 1
    y = 1
    while x != 0:

        if y >= 1:

            print("how can i help? ")
            print("type ? if you don't know what to type")
            print("#############################################################################################")
            print("\n")
            y = 0



        elif y == 0:
            print("\n")
            print("#############################################################################################")
            print("how can i help you ?")
            print("type ? if you don't know what to type")
            print("#############################################################################################")
            print("\n")

        question1 = input("")
        clearscreen()

        if question1 == "?":
            print("\n")
            print("#############################################################################################")
            print("you can type inventory to see your gold and xp points armour level and other things")
            print("you can type xp tree to see the xp tree and spend/convert you points")
            print("you can type armour or sword to buy armour and swords")
            print("you can type heal to heal")
            print("you can type end to leave the shop")
            print("#############################################################################################")
            print("\n")
            question4 = input("press enter when you are done")
            clearscreen()

        if question1 == "inventory":
            print("\n")
            print("#############################################################################################")
            print("you have", playerhealth, "health")
            print("you deal", playerattack, "damage")
            print("you have", playergold, "gold")
            print("you have", playerxpgreen, "green xp points")
            print("you have", playerxpred, "red xp points")
            print("you have", playerxpblue, "blue xp points")
            print("your armour is level", playerarmourlevel)
            print("you sword is level", playerswordlevel)
            print("#############################################################################################")
            print("\n")
            question4 = input("press enter when you are done")
            clearscreen()

        if question1 == "xp tree":
            x = 1
            while x != 0:
                print("\n")
                print("#############################################################################################")
                print("would you like to (spend) or (convert) your coins or (end)")
                print("#############################################################################################")
                print("\n")
                question2 = input("")

                if question2 == "convert":

                    print("\n")
                    print(
                        "#############################################################################################")
                    print("what xp type would you like to convert (red) or (blue)")
                    print(
                        "#############################################################################################")
                    print("\n")
                    question3 = input("")

                    print("\n")
                    print(
                        "#############################################################################################")
                    print("how much of the", question3, "xp would you like to convert")
                    print("you currently have", playerxpgreen, "green xp points")
                    print("you currently have", playerxpred, "red xp points")
                    print("you currently have", playerxpblue, "blue xp points")
                    print(
                        "#############################################################################################")
                    print("\n")
                    question5 = int(input(""))

                    if question3 == "red":
                        if playerxpred >= question5:
                            print("\n")
                            print(
                                "#############################################################################################")
                            print("you have converted", question5, "red xp points")
                            while playerxpred != 0 and question5 != 0:
                                question5 = question5 - 1
                                playerxpred = playerxpred - 1
                                playerxpgreen = playerxpgreen + 2

                            print("you now have", playerxpgreen, "green xp points")
                            print(
                                "#############################################################################################")
                            print("\n")
                        else:
                            print("\n")
                            print(
                                "#############################################################################################")
                            print("sorry you don't have enough")
                            print(
                                "#############################################################################################")
                            print("\n")

                    if question3 == "blue":
                        print("\n")
                        print(
                            "#############################################################################################")
                        print("would you like to convert the blue xp points to either (red) or (green) xp points")
                        print(
                            "#############################################################################################")
                        print("\n")

                        question6 = input("")

                        if question6 == "Red":
                            if playerxpblue >= question5:
                                print("\n")
                                print(
                                    "#############################################################################################")
                                print("you have converted", question5, "blue xp points")
                                while playerxpblue != 0 and question5 != 0:
                                    question5 = question5 - 1
                                    playerxpblue = playerxpblue - 1
                                    playerxpred = playerxpred + 2

                                print("you now have", playerxpred, "red xp points")
                                print(
                                    "#############################################################################################")
                                print("\n")


                            else:
                                print("\n")
                                print(
                                    "#############################################################################################")
                                print("sorry you don't have enough")
                                print(
                                    "#############################################################################################")
                                print("\n")

                        if question6 == "green":
                            if playerxpblue >= question5:
                                print("\n")
                                print(
                                    "#############################################################################################")
                                print("you have converted", question5, "blue xp points")
                                while playerxpred != 0 and question5 != 0:
                                    question5 = question5 - 1
                                    playerxpblue = playerxpblue - 1
                                    playerxpred = playerxpred + 2

                                print("you now have", playerxpred, "red xp points")
                                print(
                                    "#############################################################################################")
                                print("\n")


                            else:
                                print("\n")
                                print(
                                    "#############################################################################################")
                                print("sorry you don't have enough")
                                print(
                                    "#############################################################################################")
                                print("\n")

                if question2 == "spend":

                    print("\n")
                    print(
                        "#############################################################################################")
                    print("what would you like to uprade (special) or (physical) abilites")
                    print(
                        "#############################################################################################")
                    print("\n")
                    question7 = input("")

                    if question7 == "special":
                        y = 1
                        while y == 1:

                            print("\n")
                            print(
                                "#############################################################################################")
                            print("you can purchase")
                            if heal == 0:
                                print("the heal ability for 4 red xp points")
                            if rangedattack == 0:
                                print("the ranged attack ability for 4 red xp points")
                            print("you have", playerxpred, "red xp points")
                            print("would you like to upgrade anything (heal),(ranged attack) or (no)")
                            print(
                                "#############################################################################################")
                            print("\n")
                            question8 = input("")

                            if question8 == "heal" and playerxpred >= 4:
                                print("\n")
                                print(
                                    "#############################################################################################")
                                print("you have purchased the heal ability ")
                                playerxpred = playerxpred - 4
                                print("you now have", playerxpred, "red xp points")
                                print(
                                    "#############################################################################################")
                                print("\n")

                            if question8 == "heal" and playerxpred >= 4:
                                print("\n")
                                print(
                                    "#############################################################################################")
                                print("you have purchased the ranged attack ability ")
                                playerxpred = playerxpred - 4
                                print("you now have", playerxpred, "red xp points")
                                print(
                                    "#############################################################################################")
                                print("\n")

                            else:
                                print("\n")
                                print(
                                    "#############################################################################################")
                                print(" you don't have enough xp points")
                                print(
                                    "#############################################################################################")
                                print("\n")

                            if question8 == "no":
                                y = 0

                    if question7 == "physical":
                        print("\n")
                        print(
                            "#############################################################################################")
                        print("there are 3 parts each part is interlinked with the other parts")
                        print("(speed),(strength) or (skill)")
                        print(
                            "#############################################################################################")
                        print("\n")
                        question9 = input("")

                        if question9 == "speed":
                            print("\n")
                            print(
                                "#############################################################################################")
                            print("your current speed level is", speedlevel)
                            if speedlevel == 0:
                                print("you can upgrade to level 1 for 6 green xp points")
                                print("you have", playerxpgreen, "green xp points")
                                a = 1
                            if speedlevel == 1:
                                print("you can upgrade to level 2 for 6 red xp points")
                                print("you have", playerxpred, "red xp points")
                                a = 2
                            if speedlevel == 2:
                                print("you can upgrade to level 3 for 6 blue xp points")
                                print("you have", playerxpblue, "blue xp points")
                                a = 3
                            if speedlevel == 3:
                                print("you have maxed the speed skill")
                                a = 4
                            if a != 4:
                                print("would you like to upgrade you speed skill (yes) or (no)")
                            print(
                                "#############################################################################################")
                            print("\n")

                            if a != 4:
                                question10 = input("")

                                if question10 == "yes":
                                    z = 0

                                    if a == 1 and playerxpgreen >= 6:
                                        playerxpgreen = playerxpgreen - 6
                                        speedlevel = speedlevel + 1

                                        z = 1

                                    elif a == 2 and playerxpred >= 6:
                                        playerxpred = playerxpred - 6
                                        speedlevel = speedlevel + 1
                                        z = 1

                                    elif a == 3 and playerxpblue >= 6:
                                        playerxpblue = playerxpblue - 6
                                        speedlevel = speedlevel + 1
                                        z = 1

                                    elif z != 1:
                                        print("\n")
                                        print(
                                            "#############################################################################################")
                                        print("you do not have enough xp points")
                                        print(
                                            "#############################################################################################")
                                        print("\n")


                                    elif z == 1:
                                        print("\n")
                                        print(
                                            "#############################################################################################")
                                        print(" you have upgraded you speed skill it is now level", speedlevel)
                                        print(
                                            "#############################################################################################")
                                        print("\n")

                        if question9 == "strength":
                            print("\n")
                            print(
                                "#############################################################################################")
                            print("you currently have level", strength, "strength")
                            print("your strength level allows you to have better armour and sword damage multipiers")
                            if strength == 0:
                                print(" you can upgrade to level 1 strength for 6 green xp points")
                                print("you have", playerxpgreen, "green xp points")
                                a = 1
                            if strength == 1:
                                print("you can upgrade to level 2 strength for 6 red xp points")
                                print("you have", playerxpred, "red xp points")
                                a = 2
                            if strength == 2:
                                print("you can upgrade to level 3 strength for 6 blue xp points")
                                print("you have", playerxpblue, "blue xp points")
                                a = 3
                            if strength == 3:
                                print("you have already maxed this skill")
                                a = 4
                                print("what would you like to upgrade (sword damage) or (armour)")
                            if a != 4:
                                print("what would you like to upgrade (strength skilll),(sword damage) or (armour)")
                            print(
                                "#############################################################################################")
                            print("\n")
                            question11 = input("")

                            if a != 4 and question11 == "strength skill":

                                if a == 1 and playerxpgreen >= 6:
                                    playerxpgreen = playerxpgreen - 6
                                    speedlevel = speedlevel + 1

                                    z = 1

                                elif a == 2 and playerxpred >= 6:
                                    playerxpred = playerxpred - 6
                                    speedlevel = speedlevel + 1
                                    z = 1

                                elif a == 3 and playerxpblue >= 6:
                                    playerxpblue = playerxpblue - 6
                                    speedlevel = speedlevel + 1
                                    z = 1

                                elif z != 1:
                                    print("\n")
                                    print(
                                        "#############################################################################################")
                                    print("you do not have enough xp points")
                                    print(
                                        "#############################################################################################")
                                    print("\n")

                                elif z == 1:
                                    print("\n")
                                    print(
                                        "#############################################################################################")
                                    print(" you have upgraded you strength skill it is now level", strength)
                                    print(
                                        "#############################################################################################")
                                    print("\n")
                            if question11 == "sword damage":
                                sworddamage()

                            if question11 == "armour":
                                armourlevel()

                        if question9 == "skill":
                            print("\n")
                            print(
                                "#############################################################################################")
                            print("your current sword skill level is", playerswordlevel)
                            if playerswordlevel == 0:
                                print(" you can upgrade to level 1 world level for 6 green xp points")
                                print("you have", playerxpgreen, "green xp points")
                                a = 1
                            if playerswordlevel == 1:
                                print("you can upgrade to level 2 world level for 6 red xp points")
                                print("you have", playerxpred, "red xp points")
                                a = 2
                            if playerswordlevel == 2:
                                print("you can upgrade to level 3 sworld level for 6 blue xp points")
                                print("you have", playerxpblue, "blue xp points")
                                a = 3
                            if playerswordlevel == 3:
                                print("you have already maxed this skill")
                                a = 4
                            if a != 4:
                                print("what would you like to upgrade ,(sword) or sword multiplyers")
                            else:
                                print(
                                    "would you like to upgrade your (sword skill level) or (sword) or (sword multiplyers)")
                            print(
                                "#############################################################################################")
                            print("\n")

                            question12 = input("")

                            if question12 == "sword skill level" and a > 4:
                                z = 0

                                if a == 1 and playerxpgreen >= 6:
                                    playerxpgreen = playerxpgreen - 6
                                    playerswordlevel = playerswordlevel + 1

                                    z = 1

                                elif a == 2 and playerxpred >= 6:
                                    playerxpred = playerxpred - 6
                                    playerswordlevel = playerswordlevel + 1
                                    z = 1

                                elif a == 3 and playerxpblue >= 6:
                                    playerxpblue = playerxpblue - 6
                                    playerswordlevel = playerswordlevel + 1
                                    z = 1

                                elif z != 1:
                                    print("\n")
                                    print(
                                        "#############################################################################################")
                                    print("you do not have enough xp points")
                                    print(
                                        "#############################################################################################")
                                    print("\n")

                                elif z == 1:
                                    print("\n")
                                    print(
                                        "#############################################################################################")
                                    print(" you have upgraded you sword skill it is now level", playerswordlevel)
                                    print(
                                        "#############################################################################################")
        if question1 == "sword":
            print("\n")
            print("#############################################################################################")
            print("your current sword is level", playerswordlevel)
            print("you current sword is made of", nameplayerswordlevel)
            if playerswordlevel != 3:
                print("would you like to upgrade your sword")
            else:
                print("your sword is already maxed level")
            print("#############################################################################################")
            print("\n")

            question14 = input("")

            if question14 == "yes" and playerswordlevel != 3:
                if playerswordlevel == 0 and playergold >= 10:
                    playerswordlevel = playerswordlevel + 1
                    nameplayerswordlevel = "wood"
                    playerattack = 150
                    playergold = playergold - 10

                if playerswordlevel == 1 and playergold >= 20:
                    playerswordlevel = playerswordlevel + 1
                    nameplayerswordlevel = "iron"
                    playerattack = 200
                    playergold = playergold - 20

                if playerswordlevel == 2 and playergold >= 40:
                    playerswordlevel = playerswordlevel + 1
                    nameplayerswordlevel = "diamond"
                    playerattack = 300
                    playergold = playergold - 40

                print("\n")
                print("#############################################################################################")
                print("your sword is now level", playerswordlevel)
                print("you sword is now made of", nameplayerswordlevel)
                print("#############################################################################################")
                print("\n")

        if question1 == "armour":
            armourlevel()

        if question1 == "heal":

            print("\n")
            print(
                "#############################################################################################")
            print("you can upgrade you heal for 1 gold per 10 health")
            print("you have", playerhealth, "health")
            print("you have", playergold, "gold")
            print("would you like to heal")
            print(
                "#############################################################################################")
            print("\n")

            question13 = input("")

            if question13 == "yes":
                while playerhealth != 5000 or playergold <= 0:
                    print("\n")
                print(
                    "#############################################################################################")
                print("you have full health now")
                print("you have", playerhealth, "health")
                print("you have", playergold, "gold")
                print(
                    "#############################################################################################")
                print("\n")

        if question1 == "end":
            x = 0

    clearscreen()

def chest():

    global playerhealth
    global playerattack
    global name
    global playerxpgreen
    global playerxpred
    global playerxpblue
    global playergold
    global playerarmourlevel
    global playerswordlevel
    global room
    global heal
    global rangedattack
    global speedlevel
    global strength
    global sworddamageability
    global nameplayerswordlevel
    global nameplayerarmourlevel



    roomintro = ["as you enter the room you find your self in a chest room","as you slowly and quatiously eneter the room you find that it is a chest room"]
    shuffle(roomintro)
    intro = roomintro[0]

    print("\n")
    print(
        "#############################################################################################")
    print(intro)
    if room <= 5:
        playerxpgreen = playerxpgreen + 5
        xptype = "green"

    elif 5 < room <= 10:
        playerxpred = playerxpred + 5
        xptype = "red"

    elif 10 <= room <= 15:
        playerxpblue = playerxpblue + 5
        xptype = "blue"
    print("you have gained 5",xptype,"xp")
    print(
        "#############################################################################################")
    print("\n")


def main():
    def getMode():
        while True:
            print('Do you wish to encrypt or decrypt a message?')
            mode = input().lower()
            if mode in 'encrypt e decrypt d'.split():
                return mode
            else:
                print('Enter either "encrypt" or "e" or "decrypt" or "d".')

    def getMessage():
        print('Enter your message:')
        return input()

    def getKey():
        key = 0
        while True:
            print('Enter the key number (1-%s)')
            key = int(input())
            if (key >= 1 and key <= 26):
                return key

    def getTranslatedMessage(mode, message, key):
        if mode[0] == 'd':
            key = -key
        translated = ''

        for symbol in message:
            if symbol.isalpha():
                num = ord(symbol)
                num += key

                if symbol.isupper():
                    if num > ord('Z'):
                        num -= 26
                    elif num < ord('A'):
                        num += 26
                elif symbol.islower():
                    if num > ord('z'):
                        num -= 26
                    elif num < ord('a'):
                        num += 26

                translated += chr(num)
            else:
                translated += symbol
        return translated

    mode = getMode()
    message = getMessage()
    key = getKey()

    print('Your translated text is:')
    print(getTranslatedMessage(mode, message, key))


def finalbattle():
    global playerhealth
    global playerattack
    global name
    global playerxpgreen
    global playerxpred
    global playerxpblue
    global playergold
    global playerarmourlevel
    global playerswordlevel
    global room
    global heal
    global rangedattack
    global speedlevel
    global strength
    global sworddamageability

    ## generating monster stats

    enemyhealth = 3, 500
    enemydamage = 300

    ## possibly add some more intros into the random generator
    ## random room intro generator
    roomintro = ["i am the ultimate boss you have defeated my minions but you wont defeat me"]
    shuffle(roomintro)
    intro1 = roomintro[0]

    ## random name generator
    monstername = ['Iredar']
    shuffle(monstername)
    monster = monstername[0]

    ## random monster intro generator
    ## add more at later date
    monsterintro = ["ruler of the skyes"]
    shuffle(monsterintro)
    intro = monsterintro[0]
    print("\n")
    print("#############################################################################################")
    print(intro1, " \nI am", monster, intro)
    print("#############################################################################################")
    print("\n")

    ##  pause
    time.sleep(5)

    ## printing the description of the monster
    ## room 0-5
    attack = "high"
    health = "high"

    print("\n")
    print("#############################################################################################")
    print("you study the monster carefully and you think that it has", health, "health and", attack, "attack")
    print("#############################################################################################")
    print("\n")

    ## pause
    time.sleep(3)

    ## more info about monster possibly
    print("\n")
    print("#############################################################################################")
    print("would you like to learn more about the monster (yes) (no) ")
    print("#############################################################################################")
    print("\n")
    question1 = input("").lower()
    x = 1
    y = 0

    if question1 == "yes":
        print("\n")
        print("#############################################################################################")
        print("this will cost 1 gold are you sure (yes) (no) ")
        print("#############################################################################################")
        print("\n")
        question4 = input("").lower
        if question4 == "no":
            question2 = 0
            question3 = 100
            x = 0
            y = 0
        elif playergold != 0:
            print("\n")
            print("#############################################################################################")
            print("chose a number between 15 and 0 ")
            print("#############################################################################################")
            print("\n")
            question2 = int(input(""))

        elif playergold == 0:
            print("\n")
            print("#############################################################################################")
            print("this will cost 1 gold are you sure (yes) (no) ")
            print("#############################################################################################")
            print("\n")

        question3 = randint(0, 15)
        if question2 <= question3 and playergold != 0:
            print("\n")
            print("#############################################################################################")
            print("you were succesfull at working out the monster stats")
            print("the monster has", enemyhealth, "health and", enemydamage, "damadge")
            print("press enter to continue")
            print("#############################################################################################")
            y = 1
            playergold = playergold - 1
            print("\n")
            question6 = input("")

        elif question3 <= question2:
            print("\n")
            print("#############################################################################################")
            print("unfortunatly you were unable to work out the monsters stats")
            print("press enter to contiune")
            print("#############################################################################################")
            print("\n")
            playergold = playergold - 1
            question6 = input("")



            ## main fight
            ## display health of you or monster
    b = 0
    a = 0
    c = 0
    while playerhealth != 0 and enemyhealth != 0 and b != 1:

        x = x + 1
        if x >= 5:
            x = 5
        z = 0
        e = 0
        d = 0

        clearscreen()
        print("\n")
        print("#############################################################################################")
        print("you have", playerhealth, "health and", playerattack, "attack")
        if y == 1:
            print("the monster has", enemyhealth, "health and", enemydamage, "attack")
        else:
            print("you can not tell when the monster health changes he is to strong")
            print("the monster has", health, "health and", attack, "attack")
        print("#############################################################################################")
        print("\n")

        ## choice of attack

        print("\n")
        print("#############################################################################################")
        print("what would you like to do")
        print("type ? if you don't know what to type")
        print("#############################################################################################")
        print("\n")

        question5 = input("")

        if question5 == "?":
            print("\n")
            print("#############################################################################################")
            print("type attack to attack the monster")
            print("type special ability to use a special ability")
            print("type run to attempt to run away ")
            print("type block to attempt to block the attack")
            print("type auto to have the battle fought for you")
            print("press enter when done")
            print("#############################################################################################")
            print("\n")
            e = 1
            question6 = input("")

        if question5 == "attack":

            if sworddamageability == 1:
                times = 1.5
            if sworddamageability == 2:
                times = 2
            else:
                times = 1

            if c == 1:
                times = times + 1.5

            actualattack = playerattack * times

            percentage = randint(50, 100)

            actualattack2 = percentage / actualattack
            actualattack2 = actualattack2 * 100
            actualattack2 = myRoundingFunction(actualattack2, 0)
            enemyhealth = enemyhealth - actualattack2

            print("\n")
            print("#############################################################################################")
            print("you attack the monster you deal", actualattack2, "damage")
            print("press enter to continue")
            print("#############################################################################################")
            print("\n")

            question6 = input("")

        if question5 == "special":
            if x == 5:
                print("\n")
                print("#############################################################################################")
                print("which special move would you like to make (heal) or (ranged attack)")
                print("#############################################################################################")
                print("\n")

                question7 = input("")

                if question7 == "heal":
                    if playerhealth < 5000:
                        playerhealth = playerhealth + 500
                    print("\n")
                    print(
                        "#############################################################################################")
                    print("you now have", playerhealth)
                    print("press enter when done")
                    print(
                        "#############################################################################################")
                    print("\n")
                    quesiton6 = input("")

                if question7 == "ranged attack":

                    z = 1

                    if sworddamageability == 1:
                        times = 1.5
                    if sworddamageability == 2:
                        times = 2
                    else:
                        times = 1
                    actualattack = playerattack * times

                    percentage = randint(50, 100)

                    actualattack2 = percentage / actualattack

                    actualattack2 = myRoundingFunction(actualattack2, 0)

                    enemyhealth = enemyhealth - actualattack2

                    print("\n")
                    print(
                        "#############################################################################################")
                    print("you deal", actualattack2)
                    print("press enter when done")
                    print(
                        "#############################################################################################")
                    print("\n")
                    quesiton6 = input("")
            else:

                print("\n")
                print(
                    "#############################################################################################")
                time1 = 5 - x
                print("you have to weight for", time1, "turns")
                print(
                    "#############################################################################################")
                print("\n")

        if question5 == "run":

            if a != 1:
                e = 1
                a = 1
                print("\n")
                print("#############################################################################################")
                print("you attempt to run away")
                question8 = randint(0, 100)
                if speedlevel == 0:
                    time.sleep(2)
                    if question8 >= 90:
                        print("you were unsucesfull at running away")
                    else:
                        print("you succesfully run away")
                        b = 1

                if speedlevel == 1:
                    time.sleep(2)
                    if question8 >= 80:
                        print("you were unsucesfull at running away")
                    else:
                        print("you succesfully run away")
                        b = 1

                if speedlevel == 2:
                    time.sleep(2)
                    if question8 >= 60:
                        print("you were unsucesfull at running away")
                    else:
                        print("you succesfully run away")
                        b = 1

                if speedlevel == 3:
                    time.sleep(2)
                    if question8 >= 50:
                        print("you were unsucesfull at running away")
                    else:
                        print("you succesfully run away")
                        b = 1
                print("press enter when done")
                print("#############################################################################################")
                print("\n")

                question6 = input("")

        if question5 == "block":
            d = 1

        if question5 == "auto":
            print("\n")
            print("#############################################################################################")
            print("the auto attack will simply bash it out with the monster using no special abilitys")
            print("are you sure that you want to do this? (yes) or (no)")
            print("#############################################################################################")
            print("\n")
            question9 = input("")

            if question9 == "yes":

                while playerhealth != 0 or enemyhealth != 0:

                    if sworddamageability == 1:
                        times = 1.5

                    if sworddamageability == 2:
                        times = 2

                    else:
                        times = 1

                    actualattack = playerattack * times

                    percentage = randint(50, 100)

                    actualattack2 = percentage / actualattack

                    actualattack2 = actualattack * 100

                    actualattack2 = myRoundingFunction(actualattack2, 0)

                    enemyhealth = enemyhealth - actualattack2

                    print("you deal", actualattack2)

                    if y == 1:

                        print("the monster has", enemyhealth, "health and", enemydamage, "attack")

                    else:

                        ## room 0-5
                        if room <= 5:
                            if enemyhealth <= 400:
                                health = "low"
                            else:
                                health = "high"

                            if enemydamage <= 75:
                                attack = "low"

                            else:
                                attack = "high"
                                ## room 5-10
                        elif 5 < room <= 10:
                            if enemyhealth <= 750:
                                health = "low"
                            else:
                                health = "high"

                            if enemydamage <= 175:
                                attack = "low"

                            else:
                                attack = "high"

                                ## room 10-15
                        elif 10 < room <= 15:
                            if enemyhealth <= 1500:
                                health = "low"
                            else:
                                health = "high"

                            if enemydamage <= 200:
                                attack = "low"

                            else:
                                attack = "high"

                        print("the monster has", health, "health and", attack, "attack")

                    percentage = randint(50, 100)

                    enemydamage1 = percentage / enemydamage

                    enemydamage1 = enemydamage1 * 100

                    enemydamage1 = myRoundingFunction(enemydamage1, 0)

                    playerhealth = playerhealth - enemydamage1

                    print("the monster deals", enemydamage1)
                    print("you now have", playerhealth)

            else:
                e = 1

        if e != 1:
            print("\n")
            print("#############################################################################################")
            print("it is the monsters turn to attack")

            if z == 1:
                print("the monster misses it attack")

            elif d == 1:
                percentage1 = randint(0, 50)

                percentage = randint(50, 100)

                damage1 = percentage / enemydamage

                damage1 = damage1 / percentage1

                damage1 = damage1 * 100

                damage1 = myRoundingFunction(damage1, 0)

                playerhealth = playerhealth - damage1

                c = 1

                print("the monster deals", damage1, "to you")

            else:

                percentage = randint(50, 100)

                damage1 = percentage / enemydamage

                damage1 = damage1 * 100

                damage1 = myRoundingFunction(damage1, 0)

                playerhealth = playerhealth - damage1

                print("the monster deals", damage1)

            print("press enter when done")
            print("#############################################################################################")
            print("\n")
            quesiton6 = input("")

    print("\n")
    print(
        "#############################################################################################")
    print("you have succesfully killed the final boss")
    print("well done")
    print("you now have access to my coding machine")

    x = 1
    while x == 1:
        main()


def intro():

    global playerhealth
    global playerattack
    global name
    global playerxpgreen
    global playerxpred
    global playerxpblue
    global playergold
    global playerarmourlevel
    global playerswordlevel
    global room
    global heal
    global rangedattack
    global speedlevel
    global strength
    global sworddamageability
    global nameplayerswordlevel
    global nameplayerarmourlevel


    print("\n")
    print("#############################################################################################")
    print(" welcome to the land of narule")
    print("i am the gate keeper what is your name")
    print("#############################################################################################")
    print("\n")

    name = input("")

    print("\n")
    print("#############################################################################################")
    print("well",name,"you have many quests ahead of you")
    print("you must pass 15 room before you can reach the boss")
    print("good luck",name,"you'll need it")
    print("#############################################################################################")
    print("\n")


    while room != 15:
        print("\n")
        print("#############################################################################################")
        print("are you ready to move on")
        print("#############################################################################################")
        print("\n")
        quesiton60 = input("")

        clearscreen()
        room1 = randint(0,100)
        room = room + 1

        if room1 <= 50:
            battle()
        elif 51 < room1 <= 65:
            chest()
        else:
            shop()

    finalbattle()


intro()







