# -*- coding: utf-8 -*-

'''
Python Clicker

Small-scale Python terminal remake of Cookie Clicker made by Cristiano Porretta for Python I final project.

Original source: https://github.com/ShaShaMan26/PythonClicker
'''

# imports
import random, time, os, sys, datetime

# load save function
def load():
    global total_cookies, current_cookies, num_click, gc_got, gc_miss, start_time, num_cursor, cost_cursor, cps_cursor, num_grandma, cost_grandma, cps_grandma, num_farm, cost_farm, cps_farm, num_mine, cost_mine, cps_mine, num_factory, cost_factory, cps_factory, num_bank, cost_bank, cps_bank, num_temple, cost_temple, cps_temple, num_wiz, cost_wiz, cps_wiz, num_ship, cost_ship, cps_ship, num_alc, cost_alc, cps_alc, num_port,cost_port, cps_port, num_tima, cost_tima, cps_tima, first_boot, in_frenzy, frenzy_end, in_click_frenzy, click_frenzy_end
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

            # time
            start_time = start_time.replace(year = int(save_file.readline()), month = int(save_file.readline()), day = int(save_file.readline()), hour = int(save_file.readline()), minute = int(save_file.readline()), second = int(save_file.readline()), microsecond = int(save_file.readline()))

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
            in_frenzy = int(save_file.readline())
            frenzy_end = frenzy_end.replace(year = int(save_file.readline()), month = int(save_file.readline()), day = int(save_file.readline()), hour = int(save_file.readline()), minute = int(save_file.readline()), second = int(save_file.readline()), microsecond = int(save_file.readline()))
            in_click_frenzy = int(save_file.readline())
            click_frenzy_end = click_frenzy_end.replace(year = int(save_file.readline()), month = int(save_file.readline()), day = int(save_file.readline()), hour = int(save_file.readline()), minute = int(save_file.readline()), second = int(save_file.readline()), microsecond = int(save_file.readline()))

            save_file.close()
    except:
        print("No save file detected. Creating new one...\n")

def save():
    global total_cookies, current_cookies, num_click, gc_got, gc_miss, start_time, num_cursor, cost_cursor, cps_cursor, num_grandma, cost_grandma, cps_grandma, num_farm, cost_farm, cps_farm, num_mine, cost_mine, cps_mine, num_factory, cost_factory, cps_factory, num_bank, cost_bank, cps_bank, num_temple, cost_temple, cps_temple, num_wiz, cost_wiz, cps_wiz, num_ship, cost_ship, cps_ship, num_alc, cost_alc, cps_alc, num_port,cost_port, cps_port, num_tima, cost_tima, cps_tima, first_boot, in_frenzy, frenzy_end, in_click_frenzy, click_frenzy_end
    try:
        with open(os.path.join(sys.path[0],"SaveData.txt"), "w") as save_file:
            # cookies
            save_file.writelines("%s\n%s\n" % (str(total_cookies), str(current_cookies)))

            # clicks
            save_file.writelines("%s\n" % (str(num_click)))

            # golden cookies
            save_file.writelines("%s\n%s\n" % (str(gc_got), str(gc_miss)))

            # time
            save_file.writelines("%s\n%s\n%s\n%s\n%s\n%s\n%s\n" % (str(start_time.year), str(start_time.month), str(start_time.day), str(start_time.hour), str(start_time.minute), str(start_time.second), str(start_time.microsecond)))

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
            save_file.writelines(str(in_frenzy) + "\n")
            save_file.writelines("%s\n%s\n%s\n%s\n%s\n%s\n%s\n" % (str(frenzy_end.year), str(frenzy_end.month), str(frenzy_end.day), str(frenzy_end.hour), str(frenzy_end.minute), str(frenzy_end.second), str(frenzy_end.microsecond)))
            save_file.writelines(str(in_click_frenzy) + "\n")
            save_file.writelines("%s\n%s\n%s\n%s\n%s\n%s\n%s\n" % (str(click_frenzy_end.year), str(click_frenzy_end.month), str(click_frenzy_end.day), str(click_frenzy_end.hour), str(click_frenzy_end.minute), str(click_frenzy_end.second), str(click_frenzy_end.microsecond)))

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

def lucky():
    global total_cookies, cps, current_cookies
    print("~~Lucky!~~")
    if (1.15 * (current_cookies + 13)) <= ((cps * 900) + 13):
        total_cookies += (1.15 * (current_cookies + 13))
        current_cookies += (1.15 * (current_cookies + 13))
        print("+%d cookies\n" % int(1.15 * (current_cookies + 13)))
    else:
        total_cookies += ((cps * 900) + 13)
        current_cookies += ((cps * 900) + 13)
        print("+%d cookies\n" % int((cps * 900) + 13))

def frenzy():
    global in_frenzy, frenzy_time, frenzy_end
    print("~~Frenzy~~\nClicks per second x7 for 77 seconds.\n")
    in_frenzy = 1
    frenzy_time = datetime.datetime.today()
    frenzy_end = frenzy_time + datetime.timedelta(seconds = 77)

def click_frenzy():
    global in_click_frenzy, click_frenzy_time, click_frenzy_end
    print("~~Click Frenzy~~\ncookies per second x777 for 13 seconds.\n")
    in_click_frenzy = 1
    click_frenzy_time = datetime.datetime.today()
    click_frenzy_end = click_frenzy_time + datetime.timedelta(seconds = 13)

def blab():
    blab = ['Cookie crumbliness x3 for 60 seconds!', 'Chocolatiness x7 for 77 seconds!', 'Dough elasticity halved for 66 seconds!', 'Golden Cookie shininess doubled for 3 seconds!', 'World economy halved for 30 seconds!', 'Grandma kisses 23% stingier for 45 seconds!', 'Thanks for clicking!', 'Fooled you! This one was just a test.', 'Golden Cookies clicked +1!', 'Your click has been registered. Thank you for your cooperation.', 'Thanks! That hit the spot!', 'Thank you. A team has been dispatched.', 'They know.', 'Oops. This was just a chocolate cookie with shiny aluminium foil.', 'Mouse acceleration +0.03%!', 'All cookies multiplied by 999! All cookies divided by 999!', 'Gained 1 extra!', 'Chocolate chips reshuffled!', 'Ascension bonuses x5,000 for 0.1 seconds!', 'It seems you hallucinated that cookie.', 'Organs added.', 'Bones removed.', 'You saw nothing.', 'In theory there is no wrong way of clicking a golden cookie, but you did that, somehow.', 'Nice try, but no.', 'Randomized chance card outcome!', 'Huh? Oh, there was nothing there.', 'I felt that.', 'This golden cookie was a complete fabrication.', 'Eschaton immanentized!', 'Yippee!', 'Again.', 'Why?', "You've made a grave mistake.", 'Oh, that tickled!', "Wait, sorry, I wasn't ready yet.", 'Did you just click that?', 'Sorry, better luck next time!']
    blab_num = random.randint(1, 38)
    print(blab[blab_num] + "\n")

def gc_spawn():
    global num_click, gc_got, gc_miss

    if num_click >= 300:
        if random.randint(300, 900) in range(300, num_click):
            num_click = 0
            chance = 0
            while(chance < 3):
                gc_char = chr(random.randint(97, 122))
                chance += 1
                if input("A golden cookie appeared! Enter '%s' to collect: " % (gc_char) ).lower() == gc_char:
                    clear()
                    chance = 4
                    gc_got += 1
                    effect_num = random.randint(1, 100)
                    if effect_num in range(1, 47):
                        lucky()
                    elif effect_num in range(47, 93):
                        frenzy()
                    elif effect_num in range(93, 100):
                        click_frenzy()
                    elif effect_num == 100:
                        blab()
                else:
                    clear()
            if chance == 3:
                clear()
                gc_miss +=1
                print("You missed the Golden Cookie.\n")

def shop(type):
    global in_shop, num_cursor, cost_cursor, num_grandma, cost_grandma, num_farm, cost_farm, num_mine, cost_mine, num_factory, cost_factory, num_bank, cost_bank, num_temple, cost_temple, num_wiz, cost_wiz, num_ship, cost_ship, num_alc, cost_alc, num_port, cost_port, num_tima, cost_tima
    type = type.lower()

    try:
        if type == "cursor" or type == "1":
            type = "cursor"
            num_cursor, cost_cursor = (purchase(type, num_cursor, cost_cursor, 15, input("\tAmount: ")))
        elif type == "grandma" or type == "2":
            type = "grandma"
            num_grandma, cost_grandma = (purchase(type, num_grandma, cost_grandma, 100, input("\tAmount: ")))
        elif (type == "farm" or type == "3") and num_grandma > 0:
            type = "farm"
            num_farm, cost_farm = (purchase(type, num_farm, cost_farm, 1100, input("\tAmount: ")))
        elif (type == "mine" or type == "4") and num_farm > 0:
            type = "mine"
            num_mine, cost_mine = (purchase(type, num_mine, cost_mine, 12000, input("\tAmount: ")))
        elif (type == "factory" or type == "5") and num_mine > 0:
            type = "factory"
            num_factory, cost_factory = (purchase(type, num_factory, cost_factory, 130000, input("\tAmount: ")))
        elif (type == "bank" or type == "6") and num_factory > 0:
            type = "bank"
            num_bank, cost_bank = (purchase(type, num_bank, cost_bank, 1400000, input("\tAmount: ")))
        elif (type == "temple" or type == "7") and num_bank > 0:
            type = "temple"
            num_temple, cost_temple = (purchase(type, num_temple, cost_temple, 20000000, input("\tAmount: ")))
        elif (type == "wizard tower" or type == "8") and num_temple > 0:
            type = "wizard tower"
            num_wiz, cost_wiz = (purchase(type, num_wiz, cost_wiz, 330000000, input("\tAmount: ")))
        elif (type == "shipment" or type == "9") and num_wiz > 0:
            type = "shipment"
            num_ship, cost_ship = (purchase(type, num_ship, cost_ship, 5100000000, input("\tAmount: ")))
        elif (type == "alchemy lab" or type == "10") and num_ship > 0:
            type = "alchemy lab"
            num_alc, cost_alc = (purchase(type, num_alc, cost_alc, 75000000000, input("\tAmount: ")))
        elif (type == "portal" or type == "11") and num_alc > 0:
            type = "portal"
            num_port, cost_port = (purchase(type, num_port, cost_port, 1000000000000, input("\tAmount: ")))
        elif (type == "time machine" or type == "12") and num_port > 0:
            type = "time machine"
            num_tima, cost_tima = (purchase(type, num_tima, cost_tima, 14000000000000, input("\tAmount: ")))
    
        elif "desc" in type:
            clear()
            if type == "desc.cursor" or type == "desc.1":
                print("[Cursor] --> Clicks cookies alongside you. Who controls them...?; increases cookies per second by 0.1")
            elif type == "desc.grandma" or type == "desc.2":
                print("[Grandma] --> Bakes for you. How nice!; increases cookies per second by 1")
            elif (type == "desc.farm" or type == "desc.3") and num_grandma > 0:
                print("[Farm] --> Grows cookies for harvesting. Don't think about it too hard; increases cookies per second by 8")
            elif (type == "desc.mine" or type == "desc.4") and num_farm > 0:
                print("[Mine] --> Extracts the natural cookies of the Earth. What, you didn't know about that?; increases cookies per second by 47")
            elif (type == "desc.factory" or type == "desc.5") and num_mine > 0:
                print("[Factory] --> Mass-produces cookies on a global scale. It's not a monopoly, it's business; increases cookies per second by 260")
            elif (type == "desc.bank" or type == "desc.6") and num_factory > 0:
                print("[Bank] --> Take out a copious number of cookie loans. Bad credit?\n\nWell i was shopping for a new car which ones me?\nA cool convertible or an SUV\nToo bad i didn't know my credit was whack and now I'm driving off the lot in a used sub-compact\nF-R-E-E that spells free. creditreport.com baby\nSaw their ads on my TV, thought about going but was too lazy\nNow instead of looking fly and rolling fat My legs are sticking to the vinyl and my posses getting laughed at!\nF-R-E-E that spell free. creditreport.com baby!;\n\nincreases cookies per second by 1.4K")
            elif (type == "desc.temple" or type == "desc.7") and num_bank > 0:
                print("[Temple] --> Pray to the Cookie Gods, I'm sure they'll love you; increases cookies per second by 7.8K")
            elif (type == "desc.wizard tower" or type == "desc.8") and num_temple > 0:
                print("[Wizard Tower] --> Enlist the help of Cookie Wizards throughout the world; increases cookies per second by 44K")
            elif (type == "desc.shipment" or type == "desc.9") and num_wiz > 0:
                print("[Shipment] --> Order shipments of cookies from far off planets. Did someone order a package?; increases cookies per second by 260K")
            elif (type == "desc.alchemy lab" or type == "desc.10") and num_ship > 0:
                print("[Alchemy Lab] --> Synthesize cookies to your heart's content. Are we breaking any natural laws here?; increases cookies per second by 1.6M")
            elif (type == "desc.portal" or type == "desc.11") and num_alc > 0:
                print("[Portal] --> Open a portal to the Cookie Dimension. Shovel as many cookies as you can before the spacetime-continuum collapses; increases cookies per second by 10M")
            elif (type == "desc.time machine" or type == "desc.12") and num_port > 0:
                print("[Time Machine] --> Travel back in time and steal the cookies yet to be baked. Try not to make out with your mom; increases cookies per second by 65M")
            else:
                print("Input not recognized or building not unlocked")
            print("")

        elif type == "/e" or type == "exit":
            clear()
            in_shop = False

        else:
            clear()
            print("Input error\n")
    except:
        clear()
        print("Input error\n")

def purchase(building, num_build, cost_build, initial_cost, amount):
    global current_cookies
    if amount.lower() == "max":
        clear()
        while(current_cookies >= cost_build):
            current_cookies -= float(cost_build)
            num_build += 1
            cost_build = initial_cost * (1.15 ** num_build)
    elif int(amount) >= 1:
        amount = int(amount)
        clear()
        if current_cookies >= cost_build:
            while(amount >= 1 and current_cookies >= cost_build):
                current_cookies -= float(cost_build)
                num_build += 1
                cost_build = initial_cost * (1.15 ** num_build)
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
cpc = 1
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
in_frenzy = 0
in_click_frenzy = 0

# time
start_time = datetime.datetime.today()
end_time = datetime.datetime.today()

frenzy_end = datetime.datetime.today()
click_frenzy_end = datetime.datetime.today()

# load save
load()

# welcome text
if first_boot == 1:
    print("Welcome to Python Clicker; a Python Terminal remake of the hit game Cooke Clicker!\nAll actions are preformed by entering commands in the terminal. Type '/h' or 'help' for list of commands.\n")
    first_boot = 0
else:
    print("Welcome back to Python Clicker!\nType '/h' or 'help' for list of commands.\n")

# main loop
while(True):
    # cps calculation
    cps = cps_cursor*num_cursor + cps_grandma*num_grandma + cps_farm*num_farm + cps_mine*num_mine + cps_factory*num_factory + cps_bank*num_bank + cps_temple*num_temple + cps_wiz*num_wiz + cps_ship*num_ship + cps_alc*num_alc + cps_port*num_port + cps_tima*num_tima
    
    # input
    user_input = input("[%s cookies] +%s cookies per second\nEnter command: " % (display_num(current_cookies), display_num2(cps))).lower()

    # click
    if user_input == "":
        clear()
        
        # update time value
        end_time = datetime.datetime.today()
        
        # during frenzy
        if in_frenzy == 1 and end_time < frenzy_end:
            total_cookies += (abs(end_time.second - start_time.second) * (cps * 7)) + cpc * 7
            current_cookies += (abs(end_time.second - start_time.second) * (cps * 7)) + cpc * 7
        
        # during click frenzy
        elif in_click_frenzy == 1 and end_time < click_frenzy_end:
            total_cookies += (abs(end_time.second - start_time.second) * (cps * 777)) + cpc * 777
            current_cookies += (abs(end_time.second - start_time.second) * (cps * 777)) + cpc * 777
        
        # normal click
        else:
            total_cookies += (abs(end_time.second - start_time.second) * (cps)) + cpc
            current_cookies += (abs(end_time.second - start_time.second) * (cps)) + cpc
        num_click += 1
        start_time = datetime.datetime.today()
        gc_spawn()

    # help
    elif user_input == "/h" or user_input == "help":
        clear()
        print("""List of Commands:
        '' (Empty Input) - Clicks Cookie
        '/s' or 'shop' - Enter shop
        '/st' or 'stats' - View statistics
        '/h' or 'help' - View List of Commands
        '/a' or 'about' - View About Page
        '/sf' or 'save' - Manual Save
        '/d' or 'delete' - Delete save file
        '/e' or 'exit' - Quit game
        """)

    # about
    elif user_input == "/a" or user_input == "about":
        clear()
        print("""About Python Clicker:

    Python Clicker is a limited text terminal remake of the hit game Cookie Clicker within the Python coding language.
        
    As everything runs within the terminal, values only update once an action is preformed. 
    I assure you, however, that cookie production is calculated based on the passage of real world time.
        """)

    # stats
    elif user_input == "/st" or user_input == "stats":
        clear()
        print("""You have cooked %s total cookies.
You currently have %s cookies.
cps = %s
num_click = %s
gc_got = %s
gc_miss = %s
num_cursor = %d
num_grandma = %d
num_farm = %d
num_mine = %d
num_factory = %d
num_bank = %d
num_temple = %d
num_wiz = %d
num_ship = %d
num_alc = %d
num_port = %d
num_tima = %d
""" % (display_num2(total_cookies), display_num2(current_cookies), display_num2(cps), num_click, gc_got, gc_miss, num_cursor, num_grandma, num_farm, num_mine, num_factory, num_bank, num_temple, num_wiz, num_ship, num_alc, num_port, num_tima))
    
    # enter shop
    elif user_input == "/s" or user_input == "shop":
        clear()
        in_shop = True
        while(in_shop):
            print("Enter building name or type 'desc.BUILDING NAME' or type 'exit'")
            print("[Cookies: %s]\n\n[1] Cursor --> [%s cookies]\n[2] Grandma --> [%s cookies]" % (display_num(current_cookies), display_num(cost_cursor), display_num(cost_grandma)))
            if num_grandma > 0:
                print("[3] Farm --> [%s cookies]" % display_num(cost_farm))
            else:
                print("[3] ???? --> [??? cookies]")
            if num_farm > 0:
                print("[4] Mine --> [%s cookies]" % display_num(cost_mine))
            else:
                print("[4] ???? --> [??? cookies]")
            if num_mine > 0:
                print("[5] Factory --> [%s cookies]" % display_num(cost_factory))
            else:
                print("[5] ??????? --> [??? cookies]")
            if num_factory > 0:
                print("[6] Bank --> [%s cookies]" % display_num(cost_bank))
            else:
                print("[6] ???? --> [??? cookies]")
            if num_bank > 0:
                print("[7] Temple --> [%s cookies]" % display_num(cost_temple))
            else:
                print("[7] ?????? --> [??? cookies]")
            if num_temple > 0:
                print("[8] Wizard Tower --> [%s cookies]" % display_num(cost_wiz))
            else:
                print("[8] ?????? ????? --> [??? cookies]")
            if num_wiz > 0:
                print("[9] Shipment --> [%s cookies]" % display_num(cost_ship))
            else:
                print("[9] ???????? --> [??? cookies]")
            if num_ship > 0:
                print("[10] Alchemy Lab --> [%s cookies]" % display_num(cost_alc))
            else:
                print("[10] ??????? ??? --> [??? cookies]")
            if num_alc > 0:
                print("[11] Portal --> [%s cookies]" % display_num(cost_port))
            else:
                print("[11] ?????? --> [??? cookies]")
            if num_port > 0:
                print("[12] Time Machine --> [%s cookies]" % display_num(cost_tima))
            else:
                print("[12] ???? ??????? --> [??? cookies]")
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
            time.sleep(2)
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