# -*- coding: utf-8 -*-

'''
Python Clicker

Small-scale text-based remake of Cookie Clicker made by Cristiano Porretta as a Python I final project.

Original source: https://github.com/ShaShaMan26/PythonClicker
'''

# imports
import random, time, os, sys, datetime

application_path = sys.path[0]
# os.path.dirname(sys.executable)

# load save function
def load():
    '''
    Loads save data from SaveData.txt.

    args:
        N/A
    returns:
        N/A
    '''
    global total_cookies, current_cookies, gc_st, gc_got, gc_miss, first_time, start_time, num_C, num_RIF, cost_RIF, num_CTPC, cost_CTPC, num_A, cost_A, num_TF, cost_TF, cost_C, cps_C, num_G, cost_G, cps_G, num_Fr, cost_Fr, cps_Fr, num_M, cost_M, cps_M, num_Fc, cost_Fc, cps_Fc, num_B, cost_B, cps_B, num_T, cost_T, cps_T, num_W, cost_W, cps_W, num_S, cost_S, cps_S, num_AL, cost_AL, cps_AL, num_Po,cost_Po, cps_Po, num_TM, cost_TM, cps_TM, num_AC, cost_AC, cps_AC, num_Pr, cost_Pr, cps_Pr, num_Ch, cost_Ch, cps_Ch, num_FE, cost_FE, cps_FE, num_PC, cost_PC, cps_PC, num_Iv, cost_Iv, cps_Iv, num_CB, cost_CB, cps_CB, first_boot, in_frenzy, frenzy_end, in_click_frenzy, click_frenzy_end
    try:
        with open(os.path.join(application_path,"SaveData.txt"), "r") as save_file:
        
            # cookies
            total_cookies = float(save_file.readline())
            current_cookies = float(save_file.readline())

            # clicks
            gc_st = float(save_file.readline())

            # golden cookies
            gc_got = float(save_file.readline())
            gc_miss = float(save_file.readline())

            # time            
            first_time = first_time.replace(year = int(save_file.readline()), month = int(save_file.readline()), day = int(save_file.readline()), hour = int(save_file.readline()), minute = int(save_file.readline()), second = int(save_file.readline()), microsecond = int(save_file.readline()))
            start_time = start_time.replace(year = int(save_file.readline()), month = int(save_file.readline()), day = int(save_file.readline()), hour = int(save_file.readline()), minute = int(save_file.readline()), second = int(save_file.readline()), microsecond = int(save_file.readline()))
            
            # upgrades
            # reinforced index finger
            num_RIF = int(save_file.readline())
            cost_RIF = int(save_file.readline())
            # carpal tunnel prevention
            num_CTPC = int(save_file.readline())
            cost_CTPC = int(save_file.readline())
            # ambidextrous
            num_A = int(save_file.readline())
            cost_A = int(save_file.readline())         
            # thousand fingers
            num_TF = int(save_file.readline())
            cost_TF = int(save_file.readline())
            
            # buildings (var names made to match that of Cookie Clicker)
            # cursor
            num_C = float(save_file.readline())
            cost_C = float(save_file.readline())
            cps_C = float(save_file.readline())
            # grandma
            num_G = float(save_file.readline())
            cost_G = float(save_file.readline())
            cps_G = float(save_file.readline())
            # farm
            num_Fr = float(save_file.readline())
            cost_Fr = float(save_file.readline())
            cps_Fr = float(save_file.readline())
            # mine
            num_M = float(save_file.readline())
            cost_M = float(save_file.readline())
            cps_M = float(save_file.readline())
            # factory
            num_Fc = float(save_file.readline())
            cost_Fc = float(save_file.readline())
            cps_Fc = float(save_file.readline())
            # bank
            num_B = float(save_file.readline())
            cost_B = float(save_file.readline())
            cps_B = float(save_file.readline())
            # temple
            num_T = float(save_file.readline())
            cost_T = float(save_file.readline())
            cps_T = float(save_file.readline())
            # wizard tower
            num_W = float(save_file.readline())
            cost_W = float(save_file.readline())
            cps_W = float(save_file.readline())
            # shipment
            num_S = float(save_file.readline())
            cost_S = float(save_file.readline())
            cps_S = float(save_file.readline())
            # alchemy lab
            num_AL = float(save_file.readline())
            cost_AL = float(save_file.readline())
            cps_AL = float(save_file.readline())
            # portal
            num_Po = float(save_file.readline())
            cost_Po = float(save_file.readline())
            cps_Po = float(save_file.readline())
            # time machine
            num_TM = float(save_file.readline())
            cost_TM = float(save_file.readline())
            cps_TM = float(save_file.readline())
            # antimatter condenser
            num_AC = float(save_file.readline())
            cost_AC = float(save_file.readline())
            cps_AC = float(save_file.readline())
            # prism
            num_Pr = float(save_file.readline())
            cost_Pr = float(save_file.readline())
            cps_Pr = float(save_file.readline())
            # chancemaker
            num_Ch = float(save_file.readline())
            cost_Ch = float(save_file.readline())
            cps_Ch = float(save_file.readline())
            # fractal engine
            num_FE = float(save_file.readline())
            cost_FE = float(save_file.readline())
            cps_FE = float(save_file.readline())
            # python console
            num_PC = float(save_file.readline())
            cost_PC = float(save_file.readline())
            cps_PC = float(save_file.readline())
            # idleverse
            num_Iv = float(save_file.readline())
            cost_Iv = float(save_file.readline())
            cps_Iv = float(save_file.readline())
            # cortex baker
            num_CB = float(save_file.readline())
            cost_CB = float(save_file.readline())
            cps_CB = float(save_file.readline())
        
            # booleans
            first_boot = int(save_file.readline())
            # golden cookie effects
            in_frenzy = int(save_file.readline())
            frenzy_end = frenzy_end.replace(year = int(save_file.readline()), month = int(save_file.readline()), day = int(save_file.readline()), hour = int(save_file.readline()), minute = int(save_file.readline()), second = int(save_file.readline()), microsecond = int(save_file.readline()))
            in_click_frenzy = int(save_file.readline())
            click_frenzy_end = click_frenzy_end.replace(year = int(save_file.readline()), month = int(save_file.readline()), day = int(save_file.readline()), hour = int(save_file.readline()), minute = int(save_file.readline()), second = int(save_file.readline()), microsecond = int(save_file.readline()))

            save_file.close()
    except:
        print("No save file detected. Creating new one...\n")

def save():
    '''
    Saves save data to SaveData.txt. Creates new file if none found.

    args:
        N/A
    returns:
        N/A
    '''
    global total_cookies, current_cookies, gc_st, gc_got, gc_miss, first_time, start_time, num_C, num_RIF, cost_RIF, num_CTPC, cost_CTPC, num_A, cost_A, num_TF, cost_TF, cost_C, cps_C, num_G, cost_G, cps_G, num_Fr, cost_Fr, cps_Fr, num_M, cost_M, cps_M, num_Fc, cost_Fc, cps_Fc, num_B, cost_B, cps_B, num_T, cost_T, cps_T, num_W, cost_W, cps_W, num_S, cost_S, cps_S, num_AL, cost_AL, cps_AL, num_Po,cost_Po, cps_Po, num_TM, cost_TM, cps_TM, num_AC, cost_AC, cps_AC, num_Pr, cost_Pr, cps_Pr, num_Ch, cost_Ch, cps_Ch, num_FE, cost_FE, cps_FE, num_PC, cost_PC, cps_PC, num_Iv, cost_Iv, cps_Iv, num_CB, cost_CB, cps_CB, first_boot, in_frenzy, frenzy_end, in_click_frenzy, click_frenzy_end
    try:
        with open(os.path.join(application_path,"SaveData.txt"), "w") as save_file:
            # cookies
            save_file.writelines("%s\n%s\n" % (str(total_cookies), str(current_cookies)))

            # clicks
            save_file.writelines("%s\n" % (str(gc_st)))

            # golden cookies
            save_file.writelines("%s\n%s\n" % (str(gc_got), str(gc_miss)))

            # time
            save_file.writelines("%s\n%s\n%s\n%s\n%s\n%s\n%s\n" % (str(first_time.year), str(first_time.month), str(first_time.day), str(first_time.hour), str(first_time.minute), str(first_time.second), str(first_time.microsecond)))
            save_file.writelines("%s\n%s\n%s\n%s\n%s\n%s\n%s\n" % (str(start_time.year), str(start_time.month), str(start_time.day), str(start_time.hour), str(start_time.minute), str(start_time.second), str(start_time.microsecond)))
            
            # upgrades
            # reinforced index finger
            save_file.writelines("%s\n%s\n" % (str(num_RIF), str(cost_RIF)))
            # carpal tunnel prevention
            save_file.writelines("%s\n%s\n" % (str(num_CTPC), str(cost_CTPC)))
            # ambidextrous
            save_file.writelines("%s\n%s\n" % (str(num_A), str(cost_A)))            
            # thousand fingers
            save_file.writelines("%s\n%s\n" % (str(num_TF), str(cost_TF)))

            # buildings
            # cursor
            save_file.writelines("%s\n%s\n%s\n" % (str(num_C), str(cost_C), str(cps_C)))
            # grandma
            save_file.writelines("%s\n%s\n%s\n" % (str(num_G), str(cost_G), str(cps_G)))
            # farm
            save_file.writelines("%s\n%s\n%s\n" % (str(num_Fr), str(cost_Fr), str(cps_Fr)))
            # mine
            save_file.writelines("%s\n%s\n%s\n" % (str(num_M), str(cost_M), str(cps_M)))
            # factory
            save_file.writelines("%s\n%s\n%s\n" % (str(num_Fc), str(cost_Fc), str(cps_Fc)))
            # bank
            save_file.writelines("%s\n%s\n%s\n" % (str(num_B), str(cost_B), str(cps_B)))
            # temple
            save_file.writelines("%s\n%s\n%s\n" % (str(num_T), str(cost_T), str(cps_T)))
            # wizard tower
            save_file.writelines("%s\n%s\n%s\n" % (str(num_W), str(cost_W), str(cps_W)))
            # shipment
            save_file.writelines("%s\n%s\n%s\n" % (str(num_S), str(cost_S), str(cps_S)))
            # alchemy lab
            save_file.writelines("%s\n%s\n%s\n" % (str(num_AL), str(cost_AL), str(cps_AL)))
            # portal
            save_file.writelines("%s\n%s\n%s\n" % (str(num_Po), str(cost_Po), str(cps_Po)))
            # time machine
            save_file.writelines("%s\n%s\n%s\n" % (str(num_TM), str(cost_TM), str(cps_TM)))
            # antimatter condenser
            save_file.writelines("%s\n%s\n%s\n" % (str(num_AC), str(cost_AC), str(cps_AC)))
            # prism
            save_file.writelines("%s\n%s\n%s\n" % (str(num_Pr), str(cost_Pr), str(cps_Pr)))
            # chancemaker
            save_file.writelines("%s\n%s\n%s\n" % (str(num_Ch), str(cost_Ch), str(cps_Ch)))
            # fractal engine
            save_file.writelines("%s\n%s\n%s\n" % (str(num_FE), str(cost_FE), str(cps_FE)))
            # python console
            save_file.writelines("%s\n%s\n%s\n" % (str(num_PC), str(cost_PC), str(cps_PC)))
            # idleverse
            save_file.writelines("%s\n%s\n%s\n" % (str(num_Iv), str(cost_Iv), str(cps_Iv)))
            # cortex baker
            save_file.writelines("%s\n%s\n%s\n" % (str(num_CB), str(cost_CB), str(cps_CB)))
        
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

def update():
    global cpc, cps, end_time, total_cookies, current_cookies, gc_st, start_time, loan_lst
    '''
    Updates values and clears terminal.
    
    args:
        N/A
    returns:
        N/A
    '''
    # cpc calculation
    cpc = (1 + (.1 * (num_TF*(num_G + num_Fr + num_M + num_Fc + num_B + num_T + num_W + num_S + num_AL + num_Po + num_TM + num_AC + num_Pr + num_Ch + num_FE + num_PC + num_Iv + num_CB)))) * (num_RIF + 1) * (num_CTPC + 1) * (num_A + 1)
    if in_click_frenzy == 1 and end_time < click_frenzy_end:
        cpc *= 777

    # cps calculation
    cps = cps_C*num_C + cps_G*num_G + cps_Fr*num_Fr + cps_M*num_M + cps_Fc*num_Fc + cps_B*num_B + cps_T*num_T + cps_W*num_W + cps_S*num_S + cps_AL*num_AL + cps_Po*num_Po + cps_TM*num_TM + cps_AC*num_AC + cps_Pr*num_Pr + cps_Ch*num_Ch + cps_FE*num_FE + cps_PC*num_PC + cps_Iv*num_Iv + cps_CB*num_CB
    if in_frenzy == 1 and end_time < frenzy_end:
        cps *= 7

    # update time value
    end_time = datetime.datetime.today()

    # update cookie count
    total_cookies += ((end_time - start_time).total_seconds() * (cps))
    current_cookies += ((end_time - start_time).total_seconds() * (cps))
        
    # update time values
    gc_st += (end_time - start_time).total_seconds()
    start_time = datetime.datetime.today()

    # system clear
    os.system('clear')

def display_num(num):
    '''
    Formats abbreviated numbers. Ex: 1000 --> 1K

    args:
        num: number to be abbreviated.
    returns:
        display_num: formatted number.
    '''
    #designates suffix letter
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

    # checks how many digits are to be displayed
    num = int(num)
    if num < 1000:
        display_num = num
    elif (len(str(num)) - 1) % 3 == 0:
        if str(num)[1] != "0":
            display_num = "%s.%s%s" % (str(num)[0], str(num)[1], end)
        else:
            display_num = "%s%s" % (str(num)[0], end)
    elif (len(str(num)) - 2) % 3 == 0:
        if str(num)[2] != "0":
            display_num = "%s.%s%s" % (str(num)[0] + str(num)[1], str(num)[2], end)
        else:
            display_num = "%s%s" % (str(num)[0] + str(num)[1], end)
    elif (len(str(num)) - 3) % 3 == 0:
        if str(num)[3] != "0":
            display_num = "%s.%s%s" % (str(num)[0] + str(num)[1] + str(num)[2], str(num)[3], end)
        else:
            display_num = "%s%s" % (str(num)[0] + str(num)[1] + str(num)[2], end)
    else:
        display_num = int(num)
    
    return display_num

def display_num2(num):
    '''
    Formats numbers to have ',' every three places. Ex: 1000 --> 1,000

    args:
        num: number to be abbreviated.
    returns:
        display_num: formatted number.
    '''
    display_num = ""

    # breaks up num into two variables
    num = str(float("%.2f" % (num)))
    num = num.split(".")
    (front_half, back_half) = num

    # used for number of iterations
    length = len(front_half)

    # places a ',' after every three digits
    for digit in front_half:
        length -= 1
        if length % 3 == 0 and length > 1:
            display_num += digit + ","
        else:
            display_num += digit

    display_num += "." + back_half
    
    return display_num

def lucky():
    '''
    Instantly gain an amount of cookies equal to either 15% of current_cookies +13
    or 15 min worth of cookies +13 (whichever is less).

    args:
        N/A
    returns:
        N/A
    '''
    global total_cookies, cps, current_cookies
    print("~~Lucky!~~")
    # adds 15% of current_cookies +13 to current/total_cookies
    if (1.15 * (current_cookies + 13)) <= ((cps * 900) + 13):
        total_cookies += (1.15 * (current_cookies + 13))
        current_cookies += (1.15 * (current_cookies + 13))
        print("+%s cookies\n" % display_num2(1.15 * (current_cookies + 13)))
    # adds 15 min worth of cookies +13 to current/total_cookies
    else:
        total_cookies += ((cps * 900) + 13)
        current_cookies += ((cps * 900) + 13)
        print("+%s cookies\n" % display_num2((cps * 900) + 13))

def frenzy():
    '''
    Multiplies cookie production by x7 for 77 seconds.

    args:
        N/A
    returns:
        N/A
    '''
    global in_frenzy, frenzy_time, frenzy_end
    print("~~Frenzy~~\nCookies per second x7 for 77 seconds.\n")
    in_frenzy = 1
    frenzy_time = datetime.datetime.today()
    frenzy_end = frenzy_time + datetime.timedelta(seconds = 77)

def click_frenzy():
    '''
    Multiplies Cookies per Click by x777 for 13 seconds.

    args:
        N/A
    returns:
        N/A
    '''
    global in_click_frenzy, click_frenzy_time, click_frenzy_end
    print("~~Click Frenzy~~\nCookies per click x777 for 13 seconds.\n")
    in_click_frenzy = 1
    click_frenzy_time = datetime.datetime.today()
    click_frenzy_end = click_frenzy_time + datetime.timedelta(seconds = 13)

def blab():
    '''
    Displays random message from list 'blab'.

    args:
        N/A
    returns:
        N/A
    '''
    blab = ['Cookie crumbliness x3 for 60 seconds!', 'Chocolatiness x7 for 77 seconds!', 'Dough elasticity halved for 66 seconds!', 'Golden Cookie shininess doubled for 3 seconds!', 'World economy halved for 30 seconds!', 'Grandma kisses 23% stingier for 45 seconds!', 'Thanks for clicking!', 'Fooled you! This one was just a test.', 'Golden Cookies clicked +1!', 'Your click has been registered. Thank you for your cooperation.', 'Thanks! That hit the spot!', 'Thank you. A team has been dispatched.', 'They know.', 'Oops. This was just a chocolate cookie with shiny aluminium foil.', 'Mouse acceleration +0.03%!', 'All cookies multiplied by 999! All cookies divided by 999!', 'Gained 1 extra!', 'Chocolate chips reshuffled!', 'Ascension bonuses x5,000 for 0.1 seconds!', 'It seems you hallucinated that cookie.', 'Organs added.', 'Bones removed.', 'You saw nothing.', 'In theory there is no wrong way of clicking a golden cookie, but you did that, somehow.', 'Nice try, but no.', 'Randomized chance card outcome!', 'Huh? Oh, there was nothing there.', 'I felt that.', 'This golden cookie was a complete fabrication.', 'Eschaton immanentized!', 'Yippee!', 'Again.', 'Why?', "You've made a grave mistake.", 'Oh, that tickled!', "Wait, sorry, I wasn't ready yet.", 'Did you just click that?', 'Sorry, better luck next time!']
    # picks random message from 'blab'
    blab_num = random.randint(1, 38)
    print(blab[blab_num] + "\n")

def gc_spawn():
    '''
    Chance to spawn a Golden Cookie based on value of gc_st.

    args:
        N/A
    returns:
        N/A
    '''
    global gc_st, gc_got, gc_miss
    if gc_st >= 300:
        if gc_st > 900:
            gc_st = 0
        if random.randint(300, 900) in range(300, int(gc_st)):
            gc_st = 0
            chance = 0
            while(chance < 3):
                gc_char = chr(random.randint(97, 122))
                chance += 1
                if input("A golden cookie appeared! Enter '%s' to collect: " % (gc_char) ).lower() == gc_char:
                    update()
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
                    update()
            if chance == 3:
                update()
                gc_miss +=1
                print("You missed the Golden Cookie.\n")

def shop(type):
    '''
    Preforms shop actions based on user input.

    args:
        type: item type.
    returns:
        N/A
    '''
    global in_shop, num_RIF, num_CTPC, num_A, num_TF, num_C, cost_C, num_G, cost_G, num_Fr, cost_Fr, num_M, cost_M, num_Fc, cost_Fc, num_B, cost_B, num_T, cost_T, num_W, cost_W, num_S, cost_S, num_AL, cost_AL, num_Po, cost_Po, num_TM, cost_TM, num_AC, cost_AC, num_Pr, cost_Pr, num_Ch, cost_Ch, num_FE, cost_FE, num_PC, cost_PC, num_Iv, cost_Iv, num_CB, cps_CB
    type = type.lower()

    try:
        if type == "reinforced index finger" or type == "u1":
            type = "reinforced index finger"
            num_RIF = purchase_u(type, cost_RIF, num_RIF)
        elif type == "carpal tunnel prevention cream" or type == "u2":
            type = "carpal tunnel prevention cream"
            num_CTPC = purchase_u(type, cost_CTPC, num_CTPC)
        elif type == "ambidextrous" or type == "u3":
            type = "ambidextrous"
            num_A = purchase_u(type, cost_A, num_A)
        elif type == "thousand fingers" or type == "u4":
            type = "thousand fingers"
            num_TF = purchase_u(type, cost_TF, num_TF)
        elif type == "cursor" or type == "1":
            type = "cursor"
            num_C, cost_C = (purchase_b(type, num_C, cost_C, 15, input("\tAmount: ")))
        elif type == "grandma" or type == "2":
            type = "grandma"
            num_G, cost_G = (purchase_b(type, num_G, cost_G, 100, input("\tAmount: ")))
        elif (type == "farm" or type == "3") and num_G > 0:
            type = "farm"
            num_Fr, cost_Fr = (purchase_b(type, num_Fr, cost_Fr, 1100, input("\tAmount: ")))
        elif (type == "mine" or type == "4") and num_Fr > 0:
            type = "mine"
            num_M, cost_M = (purchase_b(type, num_M, cost_M, 12000, input("\tAmount: ")))
        elif (type == "factory" or type == "5") and num_M > 0:
            type = "factory"
            num_Fc, cost_Fc = (purchase_b(type, num_Fc, cost_Fc, 130000, input("\tAmount: ")))
        elif (type == "bank" or type == "6") and num_Fc > 0:
            type = "bank"
            num_B, cost_B = (purchase_b(type, num_B, cost_B, 1400000, input("\tAmount: ")))
        elif (type == "temple" or type == "7") and num_B > 0:
            type = "temple"
            num_T, cost_T = (purchase_b(type, num_T, cost_T, 20000000, input("\tAmount: ")))
        elif (type == "wizard tower" or type == "8") and num_T > 0:
            type = "wizard tower"
            num_W, cost_W = (purchase_b(type, num_W, cost_W, 330000000, input("\tAmount: ")))
        elif (type == "shipment" or type == "9") and num_W > 0:
            type = "shipment"
            num_S, cost_S = (purchase_b(type, num_S, cost_S, 5100000000, input("\tAmount: ")))
        elif (type == "alchemy lab" or type == "10") and num_S > 0:
            type = "alchemy lab"
            num_AL, cost_AL = (purchase_b(type, num_AL, cost_AL, 75000000000, input("\tAmount: ")))
        elif (type == "portal" or type == "11") and num_AL > 0:
            type = "portal"
            num_Po, cost_Po = (purchase_b(type, num_Po, cost_Po, 1000000000000, input("\tAmount: ")))
        elif (type == "time machine" or type == "12") and num_Po > 0:
            type = "time machine"
            num_TM, cost_TM = (purchase_b(type, num_TM, cost_TM, 14000000000000, input("\tAmount: ")))
        elif (type == "antimatter condenser" or type == "13") and num_TM > 0:
            type = "antimatter condenser"
            num_AC, cost_AC = (purchase_b(type, num_AC, cost_AC, 170000000000000, input("\tAmount: ")))
        elif (type == "prism" or type == "14") and num_AC > 0:
            type = "prism"
            num_Pr, cost_Pr = (purchase_b(type, num_Pr, cost_Pr, 2100000000000000, input("\tAmount: ")))
        elif (type == "chancemaker" or type == "15") and num_Pr > 0:
            type = "chancemaker"
            num_Ch, cost_Ch = (purchase_b(type, num_Ch, cost_Ch, 26000000000000000, input("\tAmount: ")))
        elif (type == "fractal engine" or type == "16") and num_Ch > 0:
            type = "fractal engine"
            num_FE, cost_FE = (purchase_b(type, num_FE, cost_FE, 310000000000000000, input("\tAmount: ")))
        elif (type == "python console" or type == "17") and num_FE > 0:
            type = "python console"
            num_PC, cost_PC = (purchase_b(type, num_PC, cost_PC, 71000000000000000000, input("\tAmount: ")))
        elif (type == "idleverse" or type == "18") and num_PC > 0:
            type = "idleverse"
            num_Iv, cost_Iv = (purchase_b(type, num_Iv, cost_Iv, 12000000000000000000000, input("\tAmount: ")))
        elif (type == "cortex baker" or type == "19") and num_Iv > 0:
            type = "cortex baker"
            num_CB, cost_CB = (purchase_b(type, num_CB, cost_CB, 1900000000000000000000000, input("\tAmount: ")))
    
        elif "desc" in type:
            update()
            if type == "desc.reinforced index finger" or type == "desc.u1":
                print("[Reinforced Index Finger] --> Reinforces fingers for optimized clicking, German Science is the finest in the world!; clicks are twice as efficient.")
            elif type == "desc.carpal tunnel prevention cream" or type == "desc.u2":
                print("[Carpal Tunnel Prevention Cream] --> Delays the inevitable deterioration of your mortal form. All that for a cookie?; clicks are twice as efficient.")
            elif type == "desc.ambidextrous" or type == "desc.u3":
                print("[Ambidextrous] --> Learn the power of using two hands; clicks are twice as efficient.")
            elif type == "desc.thousand fingers" or type == "desc.u4":
                print("[Thousand Fingers] --> Raise and army of fingers to click along side you; click power +0.1 for each non-cursor building owned.")
            elif type == "desc.cursor" or type == "desc.1":
                print("[Cursor] --> Clicks cookies alongside you. Who controls them...?; increases cookies per second by 0.1")
            elif type == "desc.grandma" or type == "desc.2":
                print("[Grandma] --> Bakes for you. How nice!; increases cookies per second by 1")
            elif (type == "desc.farm" or type == "desc.3") and num_G > 0:
                print("[Farm] --> Grows cookies for harvesting. Don't think about it too hard; increases cookies per second by 8")
            elif (type == "desc.mine" or type == "desc.4") and num_Fr > 0:
                print("[Mine] --> Extracts the natural cookies of the Earth. What, you didn't know about that?; increases cookies per second by 47")
            elif (type == "desc.factory" or type == "desc.5") and num_M > 0:
                print("[Factory] --> Mass-produces cookies on a global scale. It's not a monopoly, it's business; increases cookies per second by 260")
            elif (type == "desc.bank" or type == "desc.6") and num_Fc > 0:
                print("[Bank] --> Take out a copious number of cookie loans. Bad credit?\n\nWell i was shopping for a new car which ones me?\nA cool convertible or an SUV\nToo bad i didn't know my credit was whack and now I'm driving off the lot in a used sub-compact\nF-R-E-E that spells free. creditreport.com baby\nSaw their ads on my TV, thought about going but was too lazy\nNow instead of looking fly and rolling fat My legs are sticking to the vinyl and my posses getting laughed at!\nF-R-E-E that spell free. creditreport.com baby!;\n\nincreases cookies per second by 1.4K")
            elif (type == "desc.temple" or type == "desc.7") and num_B > 0:
                print("[Temple] --> Pray to the Cookie Gods, I'm sure they'll love you; increases cookies per second by 7.8K")
            elif (type == "desc.wizard tower" or type == "desc.8") and num_T > 0:
                print("[Wizard Tower] --> Enlist the help of Cookie Wizards throughout the world; increases cookies per second by 44K")
            elif (type == "desc.shipment" or type == "desc.9") and num_W > 0:
                print("[Shipment] --> Order shipments of cookies from far off planets. Did someone order a package?; increases cookies per second by 260K")
            elif (type == "desc.alchemy lab" or type == "desc.10") and num_S > 0:
                print("[Alchemy Lab] --> Synthesize cookies to your heart's content. Are we breaking any natural laws here?; increases cookies per second by 1.6M")
            elif (type == "desc.portal" or type == "desc.11") and num_AL > 0:
                print("[Portal] --> Open a portal to the Cookie Dimension. Shovel as many cookies as you can before the spacetime-continuum collapses; increases cookies per second by 10M")
            elif (type == "desc.time machine" or type == "desc.12") and num_Po > 0:
                print("[Time Machine] --> Travel back in time and steal the cookies yet to be baked. Try not to make out with your mom; increases cookies per second by 65M")
            elif (type == "desc.antimatter condenser" or type == "desc.13") and num_TM > 0:
                print("[Antimatter Condenser] --> Condenses the universe's antimatter into cookies. Nifty!; increases cookies per second by 430M")
            elif (type == "desc.prism" or type == "desc.14") and num_AC > 0:
                print("[Prism] --> Converts light into cookies. Wonder if it came from The Dark Side of the Moon...; increases cookies per second by 2.9B")
            elif (type == "desc.chancemaker" or type == "desc.15") and num_Pr > 0:
                print("[Chancemaker] --> Mechanize the power of four-leaf clovers, spontaneously generating cookies for you; increases cookies per second by 21B")
            elif (type == "desc.fractal engine" or type == "desc.16") and num_Ch > 0:
                print("[Fractal Engine] --> Fractal generation of cookies. Cookies out of cookies out of cookies...; increases cookies per second by 150B")
            elif (type == "desc.python console" or type == "desc.17") and num_FE > 0:
                print("[Python Console] --> Hack into the mainframe and create cookies from the code itself; increases cookies per second by 1.1t")
            elif (type == "desc.idleverse" or type == "desc.18") and num_PC > 0:
                print("[Idleverse] --> Hijack the production of cookies from other idle universes; increases cookies per second by 8.3t")
            elif (type == "desc.cortex baker" or type == "desc.19") and num_Iv > 0:
                print("[Cortex Baker] --> Dream cookies into existence. Chrome up kid; increases cookies per second by 64t")
            else:
                print("Input not recognized or building not unlocked")
            print("")

        elif type == "/e" or type == "exit":
            update()
            in_shop = False

        else:
            update()
            print("Input not recognized or building not unlocked\n")
    except:
        update()
        print("Input error\n")

def purchase_u(upgrade, cost, num_up):
    '''
    Purchase upgrades.

    args:
        upgrade: upgrade type.
        cost: cost of upgrade.
        num_up: number of upgrades.
    returns:
        num_up: number of upgrades.
    '''
    global current_cookies
    update()
    if num_up < 1:
        if current_cookies - cost >= 0:
            current_cookies -= cost
            num_up += 1
            print("You now have the %s upgrade.\n" % (upgrade.title()))
        else:
            print("You don't have enough cookies to buy the %s upgrade.\n" % upgrade.title())
    else:
        print("You already have the %s upgrade!\n" % upgrade.title())

    return num_up

def purchase_b(building, num_build, cost_build, initial_cost, amount):
    '''
    Purchase buildings.

    args:
        building: type of building.
        num_build: number of buildings.
        cost_build: current cost of building.
        initial_cost: initial cost of building.
        amount: amount of buildings to be purchased.
    returns:
        num_build: number of building.
        cost_build: cost of building.
    '''
    global current_cookies
    i = 0
    if amount.lower() == "max" or amount.lower() == "m":
        update()
        while(current_cookies >= cost_build):
            current_cookies -= float(cost_build)
            num_build += 1
            i += 1
            cost_build = initial_cost * (1.15 ** num_build)
    elif int(amount) >= 1:
        amount = int(amount)
        update()
        if current_cookies >= cost_build:
            while(amount >= 1 and current_cookies >= cost_build):
                current_cookies -= float(cost_build)
                num_build += 1
                i += 1
                cost_build = initial_cost * (1.15 ** num_build)
                amount -= 1
        else:
            pass
    else:
        update()
        print("amount error")
    print("You were able to buy [%d] %s(s) and have [%d] total.\n" % (i, building, num_build))

    return [num_build, cost_build]
    
# cookie data
# cookie amount
total_cookies = 0
current_cookies = 0
# clicks
cpc = 1
gc_st = 0
# golden cookies
gc_got = 0
gc_miss = 0

# upgrade data
# reinforced index finger data
num_RIF = 0
cost_RIF = 100
# carpal tunnel prevention cream data
num_CTPC = 0
cost_CTPC = 500
# ambidextrous data
num_A = 0
cost_A = 10000
# thousand fingers data
num_TF = 0
cost_TF = 100000

# building data
# cursor data
num_C = 0
cost_C = 15
cps_C = .1
# grandma data
num_G = 0
cost_G = 100
cps_G = 1
# farm data
num_Fr = 0
cost_Fr = 1100
cps_Fr = 8
# mine data
num_M = 0
cost_M = 12000
cps_M = 47
# factory data
num_Fc = 0
cost_Fc = 130000
cps_Fc = 260
# bank data
num_B = 0
cost_B = 1400000
cps_B = 1400
# temple data
num_T = 0
cost_T = 20000000
cps_T = 7800
# wizard tower data
num_W = 0
cost_W = 330000000
cps_W = 44000
# shipment data
num_S = 0
cost_S = 5100000000
cps_S = 260000
# alchemy lab data
num_AL = 0
cost_AL = 75000000000
cps_AL = 1600000
# portal data
num_Po = 0
cost_Po = 1000000000000
cps_Po = 10000000
# time machine data
num_TM = 0
cost_TM = 14000000000000
cps_TM = 65000000
# antimatter condenser data
num_AC = 0
cost_AC = 170000000000000
cps_AC = 430000000
# prism data
num_Pr = 0
cost_Pr = 2100000000000000
cps_Pr = 2900000000
# chancemaker data
num_Ch = 0
cost_Ch = 26000000000000000
cps_Ch = 21000000000
# fractal engine data
num_FE = 0
cost_FE = 310000000000000000
cps_FE = 150000000000
# python console data
num_PC = 0
cost_PC = 71000000000000000000
cps_PC = 1100000000000
# idleverse data
num_Iv = 0
cost_Iv = 12000000000000000000000
cps_Iv = 8300000000000
# cortex baker data
num_CB = 0
cost_CB = 1900000000000000000000000
cps_CB = 64000000000000

# status booleans
in_shop = False
dev_mode = False
first_boot = 1
in_frenzy = 0
in_click_frenzy = 0

# time
first_time = datetime.datetime.today()
start_time = datetime.datetime.today()
end_time = datetime.datetime.today()

frenzy_end = datetime.datetime.today()
click_frenzy_end = datetime.datetime.today()

# load save
load()

# welcome text
if first_boot == 1:
    print("Welcome to Python Clicker; a text-based remake of the hit game Cooke Clicker!\nAll actions are preformed by entering commands in the terminal. Type '/h' or 'help' for list of commands.\n")
    first_boot = 0
    first_time = datetime.datetime.today()
else:
    print("Welcome back to Python Clicker!\nType '/h' or 'help' for list of commands.\n")

# main loop
while(True):
    # cpc calculation
    cpc = (1 + (.1 * (num_TF*(num_G + num_Fr + num_M + num_Fc + num_B + num_T + num_W + num_S + num_AL + num_Po + num_TM + num_AC + num_Pr + num_Ch + num_FE + num_PC + num_Iv + num_CB)))) * (num_RIF + 1) * (num_CTPC + 1) * (num_A + 1)
    if in_click_frenzy == 1 and end_time < click_frenzy_end:
        cpc *= 777

    # cps calculation
    cps = cps_C*num_C + cps_G*num_G + cps_Fr*num_Fr + cps_M*num_M + cps_Fc*num_Fc + cps_B*num_B + cps_T*num_T + cps_W*num_W + cps_S*num_S + cps_AL*num_AL + cps_Po*num_Po + cps_TM*num_TM + cps_AC*num_AC + cps_Pr*num_Pr + cps_Ch*num_Ch + cps_FE*num_FE + cps_PC*num_PC + cps_Iv*num_Iv + cps_CB*num_CB
    if in_frenzy == 1 and end_time < frenzy_end:
        cps *= 7

    # input
    user_input = input("[%s cookies] +%s cookies per second\nEnter command: " % (display_num(current_cookies), display_num2(cps))).lower()

    # click
    if user_input == "":
        update()
        
        # update time value
        end_time = datetime.datetime.today()

        # update cookie count
        total_cookies += ((end_time - start_time).total_seconds() * (cps)) + cpc
        current_cookies += ((end_time - start_time).total_seconds() * (cps)) + cpc
        
        # update time values
        gc_st += (end_time - start_time).total_seconds()
        start_time = datetime.datetime.today()

        # chance for Golden Cookie spawn
        gc_spawn()

        print("+%s cookies" % display_num2(cpc))

    # help
    elif user_input == "/h" or user_input == "help":
        update()
        print("""List of Commands:
        '' (Empty Input) - Click Cookie
        '/s' or 'shop' - Enter shop
        '/st' or 'stats' - View statistics
        '/h' or 'help' - View List of Commands
        '/a' or 'about' - View About Page
        '/c' or 'credits' - View Credits
        '/sf' or 'save' - Manual Save
        '/d' or 'delete' - Delete save file
        '/e' or 'exit' - Quit game
        """)

    # about
    elif user_input == "/a" or user_input == "about":
        update()
        print("""About Python Clicker:

    Python Clicker is a limited text-based remake of the hit game Cookie Clicker within the Python coding language.
        
    Your goal is to cook as many cookies as you can.
    "Click" cookies to bake them and spend your cultivated cookies in the shop for upgrades that increase your yield of cookies per click or on buildings that generate cookies for you.
    You can also uncover the ~lore~ in the shop by reading upgrade/building descriptions.
    Occasionally "Golden Cookies" will appear, collect them for various rewards.

    Have fun!
        """)

    # credits
    elif user_input == "/c" or user_input == "credits":
        update()
        print("""Created by Cristiano Porretta
        Original game and concept by Julien "Orteil" Thiennot
        
        Special Thanks:
        Fynises - for always being there to look up to.
        NCVPS - for providing a platform for people of all types to learn.
        Microsoft - for creating the Intro to Python Programming curriculum.
        You - for playing <3
        """)

    # stats
    elif user_input == "/st" or user_input == "stats":
        update()
        print("""You have cooked %s total cookies.
You currently have %s cookies.

You have been playing for %s.

You produce %s cookies a second.
You produce %s cookies per click.

You've collected %s Golden Cookies.
You've missed %s Golden Cookies.

You have %d upgrades.

You have %d cursors.
You have %d grandmas.
You have %d farms.
You have %d mines.
You have %d factories.
You have %d banks.
You have %d temples.
You have %d wizard towers.
You have %d shipments.
You have %d alchemy labs.
You have %d portals.
You have %d time machines.
You have %d antimatter condensers.
You have %d prisms.
You have %d chancemakers.
You have %d fractal engines.
You have %d python consoles.
You have %d indleveres.
You have %d cortex bakers.
""" % (display_num2(total_cookies), display_num2(current_cookies), (start_time - first_time), display_num2(cps), display_num2(cpc), gc_got, gc_miss, (num_RIF + num_CTPC + num_A + num_TF), num_C, num_G, num_Fr, num_M, num_Fc, num_B, num_T, num_W, num_S, num_AL, num_Po, num_TM, num_AC, num_Pr, num_Ch, num_FE, num_PC, num_Iv, num_CB))
    
    # enter shop
    elif user_input == "/s" or user_input == "shop":
        update()
        in_shop = True
        while(in_shop):
            print("Enter item name or index to purchase, type 'desc.ITEM NAME/INDEX' for information, or type 'exit' to leave shop")
            print("\n~~Upgrades~~")
            if num_RIF < 1:
                if num_C >= 1:
                    print("[u1] Reinforced Index Finger --> [%s cookies]" % display_num(cost_RIF))
                else:
                    print("[u1] ?????????? ????? ?????? --> [??? cookies]")
            else:
                print("Upgrade Purchased")
            if num_CTPC < 1:
                if num_C >= 1:
                    print("[u2] Carpal Tunnel Prevention Cream --> [%s cookies]" % display_num(cost_CTPC))
                else:
                    print("[u2] ?????? ?????? ?????????? ????? --> [??? cookies]")
            else:
                print("Upgrade Purchased")
            if num_A < 1:
                if num_C >= 10:
                    print("[u3] Ambidextrous --> [%s cookies]" % display_num(cost_A))
                else:
                    print("[u3] ???????????? --> [??? cookies]")
            else:
                print("Upgrade Purchased")
            if num_TF < 1:
                if num_C >= 25:
                    print("[u4] Thousand Fingers --> [%s cookies]" % display_num(cost_TF))
                else:
                    print("[u4] ???????? ??????? --> [??? cookies]")
            else:
                print("Upgrade Purchased")
            print("\n~~Buildings~~\n[1] Cursor --> [%s cookies]\n[2] Grandma --> [%s cookies]" % (display_num(cost_C), display_num(cost_G)))
            if num_G > 0:
                print("[3] Farm --> [%s cookies]" % display_num(cost_Fr))
            else:
                print("[3] ???? --> [??? cookies]")
            if num_Fr > 0:
                print("[4] Mine --> [%s cookies]" % display_num(cost_M))
            else:
                print("[4] ???? --> [??? cookies]")
            if num_M > 0:
                print("[5] Factory --> [%s cookies]" % display_num(cost_Fc))
            else:
                print("[5] ??????? --> [??? cookies]")
            if num_Fc > 0:
                print("[6] Bank --> [%s cookies]" % display_num(cost_B))
            else:
                print("[6] ???? --> [??? cookies]")
            if num_B > 0:
                print("[7] Temple --> [%s cookies]" % display_num(cost_T))
            else:
                print("[7] ?????? --> [??? cookies]")
            if num_T > 0:
                print("[8] Wizard Tower --> [%s cookies]" % display_num(cost_W))
            else:
                print("[8] ?????? ????? --> [??? cookies]")
            if num_W > 0:
                print("[9] Shipment --> [%s cookies]" % display_num(cost_S))
            else:
                print("[9] ???????? --> [??? cookies]")
            if num_S > 0:
                print("[10] Alchemy Lab --> [%s cookies]" % display_num(cost_AL))
            else:
                print("[10] ??????? ??? --> [??? cookies]")
            if num_AL > 0:
                print("[11] Portal --> [%s cookies]" % display_num(cost_Po))
            else:
                print("[11] ?????? --> [??? cookies]")
            if num_Po > 0:
                print("[12] Time Machine --> [%s cookies]" % display_num(cost_TM))
            else:
                print("[12] ???? ??????? --> [??? cookies]")
            if num_TM > 0:
                print("[13] Antimatter Condenser --> [%s cookies]" % display_num(cost_AC))
            else:
                print("[13] ?????????? ????????? --> [??? cookies]")
            if num_AC > 0:
                print("[14] Prism --> [%s cookies]" % display_num(cost_Pr))
            else:
                print("[14] ????? --> [??? cookies]")
            if num_Pr > 0:
                print("[15] Chancemaker --> [%s cookies]" % display_num(cost_Ch))
            else:
                print("[15] ??????????? --> [??? cookies]")
            if num_Ch > 0:
                print("[16] Fractal Engine --> [%s cookies]" % display_num(cost_FE))
            else:
                print("[16] ??????? ?????? --> [??? cookies]")
            if num_FE > 0:
                print("[17] Python Console --> [%s cookies]" % display_num(cost_PC))
            else:
                print("[17] ?????? ??????? --> [??? cookies]")
            if num_PC > 0:
                print("[18] Idleverse --> [%s cookies]" % display_num(cost_Iv))
            else:
                print("[18] ????????? --> [??? cookies]")
            if num_Iv > 0:
                print("[19] Cortex Baker --> [%s cookies]" % display_num(cost_CB))
            else:
                print("[19] ?????? ????? --> [??? cookies]")
            shop(input("\n[%s Cookies]\nEnter shop command: " % display_num(current_cookies)))
    
    # save
    elif user_input == "/sf" or user_input == "save":
        update()
        save()
    
    # exit
    elif user_input == "/e" or user_input == "exit":
        update()
        if input("Exit game? y/n: ").lower() == "y":
            update()
            save()
            print("Goodbye :)")
            time.sleep(2)
            break
        else:
            update()
    
    # delete
    elif user_input == "/d" or user_input == "delete":
        update()
        if input("Delete all save data? y/n: ").lower() == "y":
            save_file = open(os.path.join(sys.path[0],"SaveData.txt"), "w")
            save_file.close()
            update()
            print("All save data erased")
            time.sleep(2)
            break
        else:
            update()
    
    # clear
    elif user_input == "/c" or user_input == "clear":
        update()

    # dev
    elif user_input == "dev":
        update()
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
        update()
        print("Invalid Input\n")