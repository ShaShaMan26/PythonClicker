# -*- coding: utf-8 -*-

import random
import time
import os
import sys

def load():
    global total_cookies, current_cookies, num_click, gc_got, gc_miss, num_cursor, cost_cursor, cps_cursor, num_grandma, cost_grandma, cps_grandma, num_farm, cost_farm, cps_farm, num_mine, cost_mine, cps_mine, num_factory, cost_factory, cps_factory, num_bank, cost_bank, cps_bank, num_temple, cost_temple, cps_temple, num_wiz, cost_wiz, cps_wiz, num_ship, cost_ship, cps_ship, num_alc, cost_alc, cps_alc, num_port,cost_port, cps_port, num_tima, cost_tima, cps_tima, first_boot
    try:
        with open(os.path.join(sys.path[0],"SaveData.txt"), "r") as save_file:
        
            # cookies
            total_cookies = float(save_file.readline())
            current_cookies = float(save_file.readline())

            # clicks
            num_click = int(save_file.readline())

            # golden cookies
            gc_got = float(save_file.readline())
            gc_miss = float(save_file.readline())

            # buildings
            # cursor
            num_cursor = float(save_file.readline())
            cost_cursor = float(save_file.readline())
            cps_cursor = float(save_file.readline())
            # grandma
            num_grandma = float(save_file.readline())
            cost_grandma = float(save_file.readline())
            cps_grandma = float(save_file.readline())
            # farm
            num_farm = float(save_file.readline())
            cost_farm = float(save_file.readline())
            cps_farm = float(save_file.readline())
            # mine
            num_mine = float(save_file.readline())
            cost_mine = float(save_file.readline())
            cps_mine = float(save_file.readline())
            # factory
            num_factory = float(save_file.readline())
            cost_factory = float(save_file.readline())
            cps_factory = float(save_file.readline())
            # bank
            num_bank = float(save_file.readline())
            cost_bank = float(save_file.readline())
            cps_bank = float(save_file.readline())
            # temple
            num_temple = float(save_file.readline())
            cost_temple = float(save_file.readline())
            cps_temple = float(save_file.readline())
            # wizard tower
            num_wiz = float(save_file.readline())
            cost_wiz = float(save_file.readline())
            cps_wiz = float(save_file.readline())
            # shipment
            num_ship = float(save_file.readline())
            cost_ship = float(save_file.readline())
            cps_ship = float(save_file.readline())
            # alchemy lab
            num_alc = float(save_file.readline())
            cost_alc = float(save_file.readline())
            cps_alc = float(save_file.readline())
            # portal
            num_port = float(save_file.readline())
            cost_port = float(save_file.readline())
            cps_port = float(save_file.readline())
            # time machine
            num_tima = float(save_file.readline())
            cost_tima = float(save_file.readline())
            cps_tima = float(save_file.readline())
        
            # booleans
            first_boot = int(save_file.readline())

            save_file.close()
    except:
        print("No save file detected. Creating new one...\n")

def save():
    global total_cookies, current_cookies, num_click, gc_got, gc_miss, num_cursor, cost_cursor, cps_cursor, num_grandma, cost_grandma, cps_grandma, num_farm, cost_farm, cps_farm, num_mine, cost_mine, cps_mine, num_factory, cost_factory, cps_factory, num_bank, cost_bank, cps_bank, num_temple, cost_temple, cps_temple, num_wiz, cost_wiz, cps_wiz, num_ship, cost_ship, cps_ship, num_alc, cost_alc, cps_alc, num_port,cost_port, cps_port, num_tima, cost_tima, cps_tima, first_boot
    try:
        with open(os.path.join(sys.path[0],"SaveData.txt"), "w") as save_file:
            # cookies
            save_file.writelines("%s\n%s\n" % (str(total_cookies), str(current_cookies)))

            # clicks
            save_file.writelines("%s\n" % (str(num_click)))

            # golden cookies
            save_file.writelines("%s\n%s\n" % (str(gc_got), str(gc_miss)))

            # buildings
            # cursor
            save_file.writelines("%s\n%s\n%s\n" % (str(num_cursor), str(cost_cursor), str(cps_cursor)))
            # grandma
            save_file.writelines("%s\n%s\n%s\n" % (str(num_grandma), str(cost_grandma), str(cps_grandma)))
            # farm
            save_file.writelines("%s\n%s\n%s\n" % (str(num_farm), str(cost_farm), str(cps_farm)))
            # mine
            save_file.writelines("%s\n%s\n%s\n" % (str(num_mine), str(cost_mine), str(cps_mine)))
            # factory
            save_file.writelines("%s\n%s\n%s\n" % (str(num_factory), str(cost_factory), str(cps_factory)))
            # bank
            save_file.writelines("%s\n%s\n%s\n" % (str(num_bank), str(cost_bank), str(cps_bank)))
            # temple
            save_file.writelines("%s\n%s\n%s\n" % (str(num_temple), str(cost_temple), str(cps_temple)))
            # wizard tower
            save_file.writelines("%s\n%s\n%s\n" % (str(num_wiz), str(cost_wiz), str(cps_wiz)))
            # shipment
            save_file.writelines("%s\n%s\n%s\n" % (str(num_ship), str(cost_ship), str(cps_ship)))
            # alchemy lab
            save_file.writelines("%s\n%s\n%s\n" % (str(num_alc), str(cost_alc), str(cps_alc)))
            # portal
            save_file.writelines("%s\n%s\n%s\n" % (str(num_port), str(cost_port), str(cps_port)))
            # time machine
            save_file.writelines("%s\n%s\n%s\n" % (str(num_tima), str(cost_tima), str(cps_tima)))

            # booleans
            save_file.writelines(str(first_boot) + "\n")

            save_file.close()

            print("~~~Saving Successful~~~\n")
    except:
        print("Saving error\n")

def clear():
    os.system('cls')

def display_num(num):
    
    # thousand
    if num >= 1000 and num < 1000000:
        end = "K"
    # million
    elif num >= 1000000 and num < 1000000000:
        end = "M"
    # billion
    elif num >= 1000000000 and num < 1000000000000:
        end = "B"
    # trillion
    elif num >= 1000000000000 and num < 1000000000000000:
        end = "t"
    # quadrillion
    elif num >= 1000000000000000 and num < 1000000000000000000:
        end = "q"
    # quintillion
    elif num >= 1000000000000000000 and num < 1000000000000000000000:
        end = "Q"
    # sextillion
    elif num >= 1000000000000000000000 and num < 1000000000000000000000000:
        end = "s"
    # septillion
    elif num >= 1000000000000000000000000 and num < 1000000000000000000000000000:
        end = "S"

    num = int(num)
    if num < 1000:
        display_num = num
    elif (len(str(num)) - 1) % 3 == 0:
        display_num = "%s.%s%s" % (str(num)[0], str(num)[1], end)
    elif (len(str(num)) - 2) % 3 == 0:
        display_num = "%s.%s%s" % (str(num)[0] + str(num)[1], str(num)[2], end)
    elif (len(str(num)) - 3) % 3 == 0:
        display_num = "%s.%s%s" % (str(num)[0] + str(num)[1] + str(num)[2], str(num)[3], end)
    else:
        display_num = int(num)
    
    return display_num

def display_num2(num):
    
    display_num = ""

    num = str(float("%.2f" % (num)))

    num = num.split(".")

    (front_half, back_half) = num

    length = len(front_half)

    for digit in front_half:
        length -= 1
        if length % 3 == 0 and length > 1:
            display_num += digit + ","
        else:
            display_num += digit

    display_num += "." + back_half
    
    return display_num

def gc_spawn():
    global num_click, gc_got, gc_miss

    if num_click >= 300:
        if random.randint(300, 900) in range(300, num_click):
            num_click = 0
            chance = 1
            while(chance < 3):
                gc_char = chr(random.randint(97, 122))
                chance += 1
                if input("A golden cookie appeared! Enter '%s' to collect: " % (gc_char) ).lower() == gc_char:
                    clear()
                    chance = 4
                    gc_got += 1
                    effect_num = random.randint(1, 2)
                    if effect_num == 1:
                        frenzy()
                    elif effect_num == 2:
                        click_frenzy()
                else:
                    clear()
            if chance == 3:
                clear()
                gc_miss +=1
                print("You missed the Golden Cookie.\n")

def frenzy():
    global total_cookies, click_power, current_cookies
    i = 0
    while(i < 78):
        print("~~Cookie Frenzy Active~~\n77 clicks of 7x cookie production (while active, can only click)\n")
        user_input = input("[%s cookies] +%s cookies\nEnter command: " % (display_num(current_cookies), display_num2(click_power)))
        if user_input == "":
            clear()
            total_cookies += click_power * 7
            current_cookies += click_power * 7
            i += 1
        else:
            clear()
            print("~~Cookie Frenzy Canceled~~\n")
            break

def click_frenzy():
    global total_cookies, click_power, current_cookies
    i = 0
    while(i < 14):
        print("~~~Click Frenzy Active~~~\n13 clicks of 77x cookie production (while active, can only click)\n")
        user_input = input("[%s cookies] +%s cookies\nEnter command: " % (display_num(current_cookies), display_num2(click_power)))
        if user_input == "":
            clear()
            total_cookies += click_power * 77
            current_cookies += click_power * 77
            i += 1
        else:
            clear()
            print("~~Click Frenzy Canceled~~\n")
            break

def shop(type):
    global in_shop, num_cursor, cost_cursor, num_grandma, cost_grandma, num_farm, cost_farm, num_mine, cost_mine, num_factory, cost_factory, num_bank, cost_bank, num_temple, cost_temple, num_wiz, cost_wiz, num_ship, cost_ship, num_alc, cost_alc, num_port, cost_port, num_tima, cost_tima
    type = type.lower()

    if type == "cursor":
        num_cursor, cost_cursor = (purchase(type, num_cursor, cost_cursor, input("\tAmount: ")))
    elif type == "grandma":
        num_grandma, cost_grandma = (purchase(type, num_grandma, cost_grandma, input("\tAmount: ")))
    elif type == "farm" and num_grandma > 0:
        num_farm, cost_farm = (purchase(type, num_farm, cost_farm, input("\tAmount: ")))
    elif type == "mine" and num_farm > 0:
        num_mine, cost_mine = (purchase(type, num_mine, cost_mine, input("\tAmount: ")))
    elif type == "factory" and num_mine > 0:
        num_factory, cost_factory = (purchase(type, num_factory, cost_factory, input("\tAmount: ")))
    elif type == "bank" and num_factory > 0:
        num_bank, cost_bank = (purchase(type, num_bank, cost_bank, input("\tAmount: ")))
    elif type == "temple" and num_bank > 0:
        num_temple, cost_temple = (purchase(type, num_temple, cost_temple, input("\tAmount: ")))
    elif type == "wizard tower" and num_temple > 0:
        num_wiz, cost_wiz = (purchase(type, num_wiz, cost_wiz, input("\tAmount: ")))
    elif type == "shipment" and num_wiz > 0:
        num_ship, cost_ship = (purchase(type, num_ship, cost_ship, input("\tAmount: ")))
    elif type == "alchemy lab" and num_ship > 0:
        num_alc, cost_alc = (purchase(type, num_alc, cost_alc, input("\tAmount: ")))
    elif type == "portal" and num_alc > 0:
        num_port, cost_port = (purchase(type, num_port, cost_port, input("\tAmount: ")))
    elif type == "time machine" and num_port > 0:
        num_tima, cost_tima = (purchase(type, num_tima, cost_tima, input("\tAmount: ")))
    
    elif "desc" in type:
        clear()
        if type == "desc.cursor":
            print("[Cursor] --> Clicks cookies alongside you. Who controls them...?; increases clicks per click by 0.1")
        elif type == "desc.grandma":
            print("[Grandma] --> Bakes for you. How nice!; increases clicks per click by 1")
        elif type == "desc.farm" and num_grandma > 0:
            print("[Farm] --> Grows cookies for harvesting. Don't think about it too hard; increases clicks per click by 8")
        elif type == "desc.mine" and num_farm > 0:
            print("[Mine] --> Extracts the natural cookies of the Earth. What, you didn't know about that?; increases clicks per click by 47")
        elif type == "desc.factory" and num_mine > 0:
            print("[Factory] --> Mass-produces cookies on a global scale. It's not a monopoly, it's business; increases clicks per click by 260")
        elif type == "desc.bank" and num_factory > 0:
            print("[Bank] --> Take out a copious number of cookie loans. Bad credit?\n\nWell i was shopping for a new car which ones me?\nA cool convertible or an SUV\nToo bad i didn't know my credit was whack and now I'm driving off the lot in a used sub-compact\nF-R-E-E that spells free. creditreport.com baby\nSaw their ads on my TV, thought about going but was too lazy\nNow instead of looking fly and rolling fat My legs are sticking to the vinyl and my posses getting laughed at!\nF-R-E-E that spell free. creditreport.com baby!;\n\nincreases clicks per click by 1.4K")
        elif type == "desc.temple" and num_bank > 0:
            print("[Temple] --> Pray to the Cookie Gods, I'm sure they'll love you; increases clicks per click by 7.8K")
        elif type == "desc.wizard tower" and num_temple > 0:
            print("[Wizard Tower] --> Enlist the help of Cookie Wizards throughout the world; increases clicks per click by 44K")
        elif type == "desc.shipment" and num_wiz > 0:
            print("[Shipment] --> Order shipments of cookies from far off planets. Did someone order a package?; increases clicks per click by 260K")
        elif type == "desc.alchemy lab" and num_ship > 0:
            print("[Alchemy Lab] --> Synthesize cookies to your heart's content. Are we breaking any natural laws here?; increases clicks per click by 1.6M")
        elif type == "desc.portal" and num_alc > 0:
            print("[Portal] --> Open a portal to the Cookie Dimension. Shovel as many cookies as you can before the spacetime-continuum collapses; increases clicks per click by 10M")
        elif type == "desc.time machine" and num_port > 0:
            print("[Time Machine] --> Travel back in time and steal the cookies yet to be baked. Try not to make out with your mom; increases clicks per click by 65M")
        else:
            print("Input not recognized or building not unlocked")
        print("")

    elif type == "/e" or type == "exit":
        clear()
        in_shop = False

    else:
        clear()
        print("Input error\n")

def purchase(building, num_build, cost_build, amount):
    global current_cookies
    if amount.lower() == "max":
        clear()
        while(current_cookies >= cost_build):
            current_cookies -= float(cost_build)
            num_build += 1
            cost_build *= (1.15 ** num_build)
    elif int(amount) >= 1:
        amount = int(amount)
        clear()
        if current_cookies >= cost_build:
            while(amount >= 1 and current_cookies >= cost_build):
                current_cookies -= float(cost_build)
                num_build += 1
                cost_build *= (1.15 ** num_build)
                amount -= 1
        else:
            print("You dont have enough cookies to buy [%d] %s(s)." % (amount, building))
    else:
        clear()
        print("amount error")
    print("You now have [%d] %s(s)\n" % (num_build, building))

    return [num_build, cost_build]
    
# cookie data
# cookie amount
total_cookies = 0
current_cookies = 0
# clicks
num_click = 0
# golden cookies
gc_got = 0
gc_miss = 0

# building data
# cursor data
num_cursor = 0
cost_cursor = 15
cps_cursor = .1
# grandma data
num_grandma = 0
cost_grandma = 100
cps_grandma = 1
# farm data
num_farm = 0
cost_farm = 1100
cps_farm = 8
# mine data
num_mine = 0
cost_mine = 12000
cps_mine = 47
# factory data
num_factory = 0
cost_factory = 130000
cps_factory = 260
# bank data
num_bank = 0
cost_bank = 1400000
cps_bank = 1400
# temple data
num_temple = 0
cost_temple = 20000000
cps_temple = 7800
# wizard tower data
num_wiz = 0
cost_wiz = 330000000
cps_wiz = 44000
# shipment data
num_ship = 0
cost_ship = 5100000000
cps_ship = 260000
# alchemy lab data
num_alc = 0
cost_alc = 75000000000
cps_alc = 1600000
# portal data
num_port = 0
cost_port = 1000000000000
cps_port = 10000000
# time machine data
num_tima = 0
cost_tima = 14000000000000
cps_tima = 65000000

# status booleans
in_shop = False
dev_mode = False
first_boot = 1


# load save
load()

# welcome text
if first_boot == 1:
    print("Welcome to Python Clicker; a Python Terminal remake of the hit game Cooke Clicker!\nAll actions are preformed by entering commands in the terminal. Type '/h' or 'help' for list of commands.\n")
    first_boot = 0
else:
    print("Welcome back to Python Clicker!\nType '/h' or 'help' for list of commands.\n")

while(True):
    # Click_power calculation
    click_power = 1 + cps_cursor*num_cursor + cps_grandma*num_grandma + cps_farm*num_farm + cps_mine*num_mine + cps_factory*num_factory + cps_bank*num_bank + cps_temple*num_temple + cps_wiz*num_wiz + cps_ship*num_ship + cps_alc*num_alc + cps_port*num_port + cps_tima*num_tima

    # input
    user_input = input("[%s cookies] +%s cookies\nEnter command: " % (display_num(current_cookies), display_num2(click_power))).lower()

    # click
    if user_input == "":
        clear()
        total_cookies += click_power
        current_cookies += click_power
        num_click += 1
        gc_spawn()

    # help
    elif user_input == "/h" or user_input == "help":
        clear()
        print("""List of Commands:
        '' (Empty Input) - Clicks Cookie
        '/s' or 'shop' - Enter shop
        '/st' or 'stats' - View statistics
        '/h' or 'help' - View List of Commands
        '/sf' or 'save' - Manual Save
        '/d' or 'delete' - Delete save file
        '/e' or 'exit' - Quit game
        """)

    # stats
    elif user_input == "/st" or user_input == "stats":
        clear()
        print("You have cooked %s total cookies.\nYou currently have %s cookies.\nclick_power = %s\nnum_click = %s\ngc_got = %s\ngc_miss = %s\nnum_cursor = %d\nnum_grandma = %d\nnum_farm = %d\nnum_mine = %d\nnum_factory = %d\nnum_bank = %d\n" % (display_num2(total_cookies), display_num2(current_cookies), display_num2(click_power), num_click, gc_got, gc_miss, num_cursor, num_grandma, num_farm, num_mine, num_factory, num_bank))
    
    # enter shop
    elif user_input == "/s" or user_input == "shop":
        clear()
        in_shop = True
        while(in_shop):
            print("Enter building name or type 'desc.BUILDING NAME' or type 'exit'")
            print("[Cookies: %s]\n\nCursor --> [%s cookies]\nGrandma --> [%s cookies]" % (display_num(current_cookies), display_num(cost_cursor), display_num(cost_grandma)))
            if num_grandma > 0:
                print("Farm --> [%s cookies]" % display_num(cost_farm))
            else:
                print("???? --> [??? cookies]")
            if num_farm > 0:
                print("Mine --> [%s cookies]" % display_num(cost_mine))
            else:
                print("???? --> [??? cookies]")
            if num_mine > 0:
                print("Factory --> [%s cookies]" % display_num(cost_factory))
            else:
                print("??????? --> [??? cookies]")
            if num_factory > 0:
                print("Bank --> [%s cookies]" % display_num(cost_bank))
            else:
                print("???? --> [??? cookies]")
            if num_bank > 0:
                print("Temple --> [%s cookies]" % display_num(cost_temple))
            else:
                print("?????? --> [??? cookies]")
            if num_temple > 0:
                print("Wizard Tower --> [%s cookies]" % display_num(cost_wiz))
            else:
                print("?????? ????? --> [??? cookies]")
            if num_wiz > 0:
                print("Shipment --> [%s cookies]" % display_num(cost_ship))
            else:
                print("???????? --> [??? cookies]")
            if num_ship > 0:
                print("Alchemy Lab --> [%s cookies]" % display_num(cost_alc))
            else:
                print("??????? ??? --> [??? cookies]")
            if num_alc > 0:
                print("Portal --> [%s cookies]" % display_num(cost_port))
            else:
                print("?????? --> [??? cookies]")
            if num_port > 0:
                print("Time Machine --> [%s cookies]" % display_num(cost_tima))
            else:
                print("???? ??????? --> [??? cookies]")
            shop(input("\nEnter shop command: "))
    
    # save
    elif user_input == "/sf" or user_input == "save":
        clear()
        save()
    
    # exit
    elif user_input == "/e" or user_input == "exit":
        clear()
        if input("Exit game? y/n: ").lower() == "y":
            clear()
            save()
            print("Goodbye :)")
            time.sleep(2)
            break
        else:
            clear()
    
    # delete
    elif user_input == "/d" or user_input == "delete":
        clear()
        if input("Delete all save data? y/n: ").lower() == "y":
            save_file = open(os.path.join(sys.path[0],"SaveData.txt"), "w")
            save_file.close()
            clear()
            print("All save data erased")
            time.wait(2)
            break
        else:
            clear()
    
    # clear
    elif user_input == "/c" or user_input == "clear":
        clear()

    # dev
    elif user_input == "dev":
        clear()
        print("~~Dev Mode enabled~~")
        dev_mode = True
    
    # dev commands
    elif dev_mode == True:
        if user_input == "+":
            dev_amount = int(input("\tAmount to add: "))
            current_cookies += dev_amount
            total_cookies += dev_amount
        elif user_input == "-":
            dev_amount = int(input("\tAmount to sub: "))
            current_cookies -= dev_amount
            total_cookies -= dev_amount
        elif user_input == "=":
            dev_amount = int(input("\tChange amount: "))
            current_cookies = dev_amount
            total_cookies = dev_amount
        else:
            print("How did you manage to get this error message?!")
    
    # fallback
    else:
        clear()
        print("Invalid Input\n")