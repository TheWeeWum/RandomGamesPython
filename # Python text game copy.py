# Python text game
# this is a game which generates random enemies which you then fight
import random

#### SAVING/LOADING GAME ####################
# creates the variables for creating a new character
player_health_max = 100
player_mana_max = 100
player_defence_max = 1
player_health = player_health_max
player_mana = player_mana_max
player_defence = player_defence_max
player_attack = 1
player_exp = 0
times_leveled_up = 0
location = 'start'
number_of_wins = 0
player_level = 0
money = 0

multiplier = 1

# determines whether it creates a new player file or loads an old one
load_or_save = input("Would you like to load or create a new game (load/new): ")
# gets the name of the account
player_save_name = input("What is your account name: ")

# tells the user how they can save, or leave the game
print("Type 'exit' at any point to leave the game, this will also save progress")
print("Type 'save' at any point to save the game")

# creates the list of items from the player save data
def itemListMaker(items):
    player_items = []
    # removes these characters
    disallowed_characters = "[],'"
    splitted = []
    # splits the items by spaces (so don't put spaces in the item ids)
    splitted = items.split(" ")
    # for each individual word
    for each in splitted:
        # remove all of those characters
        for character in disallowed_characters:
            each = each.replace(character, "")
        # append this new string to the list
        player_items.append(each)
    # return the list to be applied to the dictionary
    return player_items

# loads the game for the user
def loadGame():
    global player_health_max
    global player_mana_max
    global player_defence_max
    global player_health
    global player_mana
    global player_defence
    global player_attack
    global number_of_wins
    global location
    global player_exp
    global player_level
    global times_leveled_up
    global money

    list = []
    save_game = open("playerStats" + player_save_name + ".txt","r")
    lines = save_game.readlines()
    count = 1
    # Strips the newline character
    for line in lines:
        count += 1
        if line == "":
            continue
        else:
            try:
                list.append(line)
            except AttributeError:
                print("Something went wrong")
    new_list = []
    counter = 0
    player_items = []
    # removes the suffix \n from each of the idexes, except for 12, not sure why 12 doesnt have the \n
    for each in list:
        counter += 1
        new_list.append(each[:-1])
        # if counter != 14:
        #     new_list.append(each[:-1])
        # else:
        #     new_list.append(each)
    # attaches the file results to the variables
    player_health_max = int(new_list[0])
    player_mana_max = int(new_list[1])
    player_defence_max = int(new_list[2])
    player_health = float(new_list[3])
    player_mana = float(new_list[4])
    player_defence = float(new_list[5])
    player_attack = float(new_list[6])
    number_of_wins = int(new_list[7])
    location = new_list[8]
    player_exp = float(new_list[9])
    player_level = int(new_list[10])
    times_leveled_up = int(new_list[11])
    money = float(new_list[12])
    player_items = itemListMaker(new_list[13])
    save_game.close()
    global player

    # puts all this stuff into a dictionary
    player = dict({'health': player_health, 'mana': player_mana, 'defence': player_defence, 'attack': player_attack,
                'maxHealth': player_health_max, 'maxMana': player_mana_max, 'maxDefence': player_defence_max,
                'exp': player_exp, 'level': player_level, 'timesLeveled': times_leveled_up, 'player_items': player_items, 'player_money': money})

# if the player wants to leave, or save the game
def saveGame():
    global player
    global number_of_wins
    global location
    global player_exp
    global player_level
    global times_leveled_up
    save_game = open("playerStats" + player_save_name + ".txt","w+")
    save_game.writelines("{}\n".format(round(player['maxHealth'], 2)))
    save_game.writelines("{}\n".format(round(player['maxMana'], 2)))
    save_game.writelines("{}\n".format(round(player['maxDefence'], 2)))
    save_game.writelines("{}\n".format(round(player['health'], 2)))
    save_game.writelines("{}\n".format(round(player['mana'], 2)))
    save_game.writelines("{}\n".format(round(player['defence'], 2)))
    save_game.writelines("{}\n".format(round(player['attack'], 2)))
    save_game.writelines("{}\n".format(round(number_of_wins, 2)))
    save_game.writelines("{}\n".format(location))
    save_game.writelines("{}\n".format(round(player_exp, 2)))
    save_game.writelines("{}\n".format(round(player_level, 2)))
    save_game.writelines("{}\n".format(round(times_leveled_up, 2)))
    save_game.writelines("{}\n".format(round(player['player_money'], 0)))
    save_game.writelines("{}\n".format(player['player_items']))
    save_game.close()

# if the player wants a new game
def newGame():
    global player
    global number_of_wins
    global location
    global player_exp
    global player_level
    global times_leveled_up
    player_health = 100
    player_mana = 100
    player_defence = 1
    player_attack = 1
    player_health_max = 100
    player_mana_max = 100
    player_defence_max = 1
    player_exp = 0
    player_level = 1
    times_leveled_up = 0
    money = 0
    player = dict({'health': player_health, 'mana': player_mana, 'defence': player_defence, 'attack': player_attack,
                    'maxHealth': player_health_max, 'maxMana': player_mana_max, 'maxDefence': player_defence_max,
                    'exp': player_exp, 'level': player_level, 'timesLeveled': times_leveled_up, 'player_items': [], 'player_money': money})

def checkSaveOrLeave(input):
    if (input == 'save'):
        saveGame()
    if (input == 'exit'):
        saveGame()
        exit()

#### GAME STARTUP ##################
if (load_or_save == "load"):
    print("Loading Game...")
    loadGame()
elif (load_or_save == "new"):
    print("Creating New Game...")
    newGame()
else:
    print("Please type a valid input")


#### PLAYER AREA ########################
# levels up the stat that the use wants to level up
def levelUpstats():
    global player_attack
    global player
    global times_leveled_up
    stat_to_level = input("Which stat would you like to level up extra? health + 10 (h)/ mana + 10 (m)/ defence + 0.1 (d)/ attack + 0.1(a): ")
    if (stat_to_level == 'h'):
        player['maxHealth'] += 20
        times_leveled_up += 1
    elif (stat_to_level == 'm'):
        player['maxMana'] += 20
        times_leveled_up += 1
    elif (stat_to_level == 'd'):
        player['defence'] += 0.2
        times_leveled_up += 1
    elif (stat_to_level == 'a'):
        player['attack'] += 0.2
        times_leveled_up += 1
    else:
        print("Not valid input")
        levelUpstats()
    # levels up everything once
    player['maxHealth'] += 10
    player['maxMana'] += 10
    player['defence'] += 0.1
    player['attack'] += 0.1
    # brings the users health and mana to max
    player['health'] = player['maxHealth']
    player['mana'] = player['maxMana']
    return times_leveled_up

# determines whether the user can level up or not
def levelUper(exp_gain):
    global player_exp
    global player_level
    global times_leveled_up
    player_exp += exp_gain
    # the level up requirement is the users level to the power of 3
    level_up_goal = player_level ** 3
    if (player_exp >= level_up_goal):
        player_level += 1
        if (player_level > times_leveled_up):
            print("You leveled Up!")
            times_leveled_up = levelUpstats()

#### ITEMS AREA #########################
# determines if the enemy drops an item or not
def itemDrop(enemy, enemy_level):
    global player
    item_drop_chance = random.randint(0, 10)

    if(item_drop_chance > 5):
        # makes it so that level 1 slimes will drop 1 potion instead of 2
        if (enemy_level <= 1):
            enemy_level = 2
        print("The {} dropped {} health potions (type 'health' to use them. They do not take up a turn)".format(enemy['name'], int(enemy_level / 2)))
        for number in range(0, int(enemy_level / 2)):
            what_potion = random.randint(0, 5)
            if (what_potion != 5):
                player['player_items'].append(enemy['potionDrop1'])
            else:
                player['player_items'].append(enemy['potionDrop2'])

    if(item_drop_chance == 1):
        print("The {} dropped it's rare drop! It dropped a(n) {}!".format(enemy['name'], enemy['rare_drop']))
        player['player_items'].append(enemy['rare_drop'])

    player['player_money'] += (enemy['money'] * enemy_level)

#### ENEMIES AREA #######################

# Slimes
green_slime = dict({'name' : 'green slime', 'health': 5.0, 'mana': 0, 'defence': 1, 'attack': 1, 'expGive': 1, 'rare_drop': 'slime', 'money': 1, 'potionDrop1': 'tinyHealthPotion', 'potionDrop2': 'tinyManaPotion'})
blue_slime = dict({'name' : 'blue slime', 'health': 10.0, 'mana': 0, 'defence': 1, 'attack': 2, 'expGive': 5, 'rare_drop': 'slime', 'money': 5, 'potionDrop1': 'tinyHealthPotion', 'potionDrop2': 'tinyManaPotion'})
red_slime = dict({'name' : 'green slime', 'health': 20.0, 'mana': 0, 'defence': 2, 'attack': 3, 'expGive': 20, 'rare_drop': 'slime', 'money': 20, 'potionDrop1': 'tinyHealthPotion', 'potionDrop2': 'tinyManaPotion'})
orange_slime = dict({'name' : 'orange slime', 'health': 10.0, 'mana': 0, 'defence': 5, 'attack': 4, 'expGive': 25, 'rare_drop': 'slime', 'money': 25, 'potionDrop1': 'tinyHealthPotion', 'potionDrop2': 'tinyManaPotion'})
purple_slime = dict({'name' : 'purple slime', 'health': 10.0, 'mana': 10, 'defence': 1, 'attack': 0, 'expGive': 15, 'rare_drop': 'slime', 'money': 15, 'potionDrop1': 'tinyHealthPotion', 'potionDrop2': 'tinyManaPotion'})


#### LOCATIONS #########################
# location name = [bossLevel, enmy1, enmy2, enmy3...]
forest = [5, green_slime, blue_slime, orange_slime]
plains = [5, green_slime, blue_slime, orange_slime]


#### FIGHTING AREA #####################
# makes the bars
def barMaker(max, stat):
    dash_convert = (max/dashes)            # Get the number to divide by to convert health to dashes (being 10)
    current_dashes = int(stat/dash_convert)              # Convert health to dash count: 80/10 => 8 dashes
    remaining_stat = dashes - current_dashes       # Get the health remaining to fill as space => 12 spaces

    display = '-' * current_dashes                  # Convert 8 to 8 dashes as a string:   "--------"
    remaining_display = ' ' * remaining_stat             # Convert 12 to 12 spaces as a string: "            "
    results = []
    results.append(display)
    results.append(remaining_display)
    return(results)

dashes = 20  # Max Displayed dashes

# function from https://stackoverflow.com/questions/48035367/python-text-game-health-bar
# posted by Spencer Wieczorek
def do_stats(health, mana, max_health, max_mana, e_health, e_mana, enemy, e_level):
    
    ######### PLAYER BARS ######################
    
    returned = barMaker(max_health, health)
    health_display = returned[0]
    remaining_display = returned[1]
    
    returned = barMaker(max_mana, mana)
    mana_display = returned[0]
    remaining_display_mana = returned[1]
    
    returned = barMaker(enemy['health'] + e_level * enemy['health'] / 10, e_health)
    e_health_display = returned[0]
    e_remaining_display_health = returned[1]
    
    ######### ENEMY BARS ########################

    if enemy['mana'] == 0:
        print(end='')
    else:
        returned = barMaker(enemy['mana'], e_mana)
        e_mana_display = returned[0]
        e_remaining_display_mana = returned[1]  

    # player health and mana bars
    print("\n\n\n\nPlayer Stats                                                                                                              Enemy Stats")
    print("|" + health_display + remaining_display + "|", end='')  # Print out textbased healthbar
    print("|" + mana_display + remaining_display_mana + "|", end='')  # Print out textbased healthbar
    print("                                                                         ", end='')
    print("|" + e_health_display + e_remaining_display_health + "|")  # Print out textbased healthbar
    if enemy['mana'] == 0:
        print(end='')
    else:
        print("|" + e_mana_display + e_remaining_display_mana + "|")  # Print out textbased healthbar
    
    # player health and mana percentages
    print("    health " + str(health) + "/" + str(max_health), end='') 
    print("         mana " + str(mana) + "/" + str(max_mana), end='')
    print("        defence: {}    attack: {}".format(round(player['defence']), round(player['attack'], 1)), end='')
    
    print("                                              health " + str(e_health) + '/' + str(enemy['health'] + e_level * enemy['health'] / 10), end='')
    print("        defence: {}    attack: {}".format(round(enemy['defence'] + (e_level) * enemy['defence'] / 10, 1), (round(enemy['attack'] + (e_level) * enemy['attack'] / 10, 1))))

def revive():
    global location
    print("You awake feeling slightly dazed. You notice that you have awoken back at the entrance to the forst and the plains.")
    location = 'start'
    explore()

def makeEnemies(number_of_wins, area):
    global multiplier
    if (number_of_wins != 0) and (number_of_wins % area[0] != 0):
        print("normal fight")
        enemy_level = random.randint(1, 5)
        enemy_type = random.randint(1, len(area)-1)

        if (number_of_wins < area[0]):
            multiplier = 1
        else:
            multiplier = int(number_of_wins / area[0])

        if (enemy_type == 1):
            fight(area[1], enemy_level * multiplier)
        elif (enemy_type == 2):
            fight(area[2], enemy_level * multiplier)
        elif (enemy_type == 3):
            fight(area[3], enemy_level * multiplier)
        elif (enemy_type == 4):
            fight(area[4], enemy_level * multiplier)
        elif (enemy_type == 5):
            fight(area[5], enemy_level * multiplier)
        elif (enemy_type == 6):
            fight(area[6], enemy_level * multiplier)
        elif (enemy_type == 7):
            fight(area[7], enemy_level * multiplier)
    elif (number_of_wins % area[0] == 0 and number_of_wins != 0): # boss fight level
        print("boss fight")
        multiplier = int(number_of_wins / area[0])
        fight(area[multiplier], random.randint(number_of_wins-2, number_of_wins+5) * multiplier)
    else:
        print("first fight")
        fight(green_slime, 0)

def getAreaEnemies(location):
    if (location == 'forest'):
        makeEnemies(number_of_wins, forest)
    elif (location == 'plains'):
        makeEnemies(number_of_wins, plains)

def explore():
    global number_of_wins
    global location
    if (location == 'start' or location == 'forest' or location == 'plains'):
        location = input("Where would you like to go? The forest(f)/The plains(p): ")
        checkSaveOrLeave(location)

        if (location == "f"):
            print("\nYou walk into a thick forest. The light can barely make it through the dense canopy of leaves.")
            location = 'forest'
            getAreaEnemies('forest')
        elif (location == "p"):
            print("\nYou walk into a big open field, where you can see dozens of creatures roaming around.")
            location = 'plains'
            getAreaEnemies('plains')
        else:
            print("please enter valid input")
            location = 'start'
            explore()

def fight(enemy, enemy_level): 
    global number_of_wins
    global player
    global player_level
    ran_away = False
    print("\n\n\n\n\n\n\n\n\nA {} appears before you! \nIt's level {}.".format(enemy['name'], enemy_level))
    enemy_health = enemy['health'] + enemy_level * enemy['health'] / 10
    enemy_health = round(enemy_health, 1)
    player_health_max = player['maxHealth']
    player_health = round(player['health'], 1)
    while (enemy_health > 0 and player_health > 0):
        # player stats get
        player_attack = player['attack']
        player_attack = round(player_attack, 1)
        player_mana = player['mana']
        player_mana = round(player_mana, 0)
        player_defence = player['defence']
        player_defence = round(player_defence, 1)
        # enemy stats get
        beginner = 0
        if (enemy_level == 0):
            beginner = 1
        enemy_attack = enemy['attack'] + (enemy_level + beginner) * enemy['attack'] / 10
        enemy_attack = round(enemy_attack, 1)
        enemy_mana = enemy['mana'] + (enemy_level + beginner) * enemy['mana'] / 10
        enemy_mana = round(enemy_mana, 0)
        enemy_defence = enemy['defence'] + (enemy_level + beginner) * enemy['defence'] / 10
        enemy_defence = round(enemy_defence, 1)
        do_stats(player_health, player_mana, player_health_max, player_mana_max, enemy_health, enemy_mana, enemy, enemy_level)
        # what does the player want to do 
        num_health_potions = 0
        num_mana_potions = 0
        for each in player['player_items']:
            if (each == 'tinyHealthPotion'):
                num_health_potions += 1
            if (each == 'tinyManaPotion'):
                num_mana_potions += 1
        print("\nYou have {} health potions and {} mana potions".format(num_health_potions, num_mana_potions))
        what_do = input("What do you want to do?   Attack(a)  /  Run(r)  /  Drink Health Potion(h)  /  Drink Mana Potion(m): ")
        
        if (what_do == 'h'):
            counter = 0
            index = -1
            for each in player['player_items']:
                index += 1
                if each == 'tinyHealthPotion':
                    counter += 1
                    if(counter == 1):
                        player_health += 10
                        player['player_items'].pop(index)
            if (counter == 0):
                print("You have no health potions")
        elif (what_do == 'm'):
            counter = 0
            index = -1
            for each in player['player_items']:
                index += 1
                if each == 'tinyManaPotion':
                    counter += 1
                    if(counter == 1):
                        player_mana += 10
                        player['player_items'].pop(index)
            if (counter == 0):
                print("You have no mana potions")
        elif (what_do == 'exit'):
            saveGame()
            break
        elif (what_do == 'save'):
            saveGame()
            continue
        
        elif (what_do == 'health'):
            continue
        
        elif what_do == "a":
            # punch the enemy then the enemy fights back
            if (enemy_defence >= 2):
                print("\n\n\n\n\n\n\n\n\n\nYou hit the {} for {} damage".format(enemy['name'], round((player_attack/ int((enemy_defence/2))), 1)))
                enemy_health -= player_attack / int(enemy_defence/2)
                enemy_health = round(enemy_health, 1)
            else:
                print("\n\n\n\n\n\n\n\n\n\nYou hit the {} for {} damage".format(enemy['name'], round(player_attack), 1))
                enemy_health -= player_attack
                enemy_health = round(enemy_health, 1)
            if enemy_health > 0:
                # print("Enemy health: {}, Enemy Mana: {}".format(enemy_health, enemy_mana))
                enemy_attack = round(enemy_attack / int(player_defence), 1) - 0.1
                print("Enemy hits you. You take {} damage".format(round(enemy_attack, 1)))
                player_health -= enemy_attack
                player_health = round(player_health, 1)
        elif what_do == "r":
            print("You ran away")
            ran_away = True
            explore()
        else:
            print("Please type valid input")
    if enemy_health <= 0:
        player['health'] = player_health
        print("You defeated the {}!".format(enemy['name']))
        number_of_wins += 1
        levelUper(enemy['expGive'] + int(enemy_level * enemy['expGive']/4))
        itemDrop(enemy, enemy_level)
        explore()
    
    elif (ran_away):
        player['health'] = player_health
        explore()
    elif (player_health <= 0):
        print("You died")
        player['health'] = player_health_max
        revive()

location = 'start'
explore()
