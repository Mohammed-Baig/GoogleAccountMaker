import pyautogui

# for waiting------------------------------------------------------------------------------------------
from time import sleep

# for typing
import keyboard

# for randomly generating names------------------------------------------------------------------------
import random
import string


def make_account():
    x = 0
    # define variables
    ms_edge_x = 0
    ms_edge_y = 0

    letters = string.ascii_lowercase

    month_box_location_x = 0
    month_box_location_y = 0

    next_box_location_x = 0
    next_box_location_y = 0

    agree_box_location_x = 0
    agree_box_location_y = 0

    x = int(input("the first step is to get the coordinates of where the clicks must be sent and the data filled. If "
                  "you know the coordinates already please press '1', if not please press '2'\n"))

    # insert if you already know the values
    if (x == 1):
        ms_edge_x = int(input("Input the X coordinate of the ms_edge box here:"))
        ms_edge_y = int(input("Input the Y coordinate of the ms_edge box here:"))

        month_box_location_x = int(input("Input the X coordinate of the month box here:"))
        month_box_location_y = int(input("Input the Y coordinate of the month box here:"))

        next_box_location_x = int(input("Input the X coordinate of the next box here:"))
        next_box_location_y = int(input("Input the Y coordinate of the next box here:"))

        agree_box_location_x = int(input("Input the X coordinate of the agree box here:"))
        agree_box_location_y = int(input("Input the Y coordinate of the agree box here:"))

    # gets the values live
    elif (x == 2):
        # getting location to open ms edge
        ans = input("when you're ready, type in 'Y' and a 5 second countdown will begun, hover over the microsoft edge "
                    "button on your taskbar or desktop:\n")
        if (ans.upper() == 'Y'):
            for i in range(5, 0, -1):
                sleep(1)
                print(i)
            ms_edge_x, ms_edge_y = pyautogui.position()
            print("your coordinates to open ms_edge are {}, {}".format(ms_edge_x, ms_edge_y))

        # getting coordinates to the month box
        ans = input("on the second page, we will need the coordinates to the 'month' box location. When you're ready, "
                    "type in 'Y' and a 5 second countdown will begun, meanwhile you hover over this button \n")
        if (ans.upper() == 'Y'):
            for i in range(5, 0, -1):
                sleep(1)
                print(i)
            month_box_location_x, month_box_location_y = pyautogui.position()
            print("your coordinates to open ms_edge are {}, {}".format(month_box_location_x, month_box_location_y))

        # getting coordinates to the next button
        ans = input("on this same second page, we will need the coordinates to the 'next' box location. When you're "
                    "ready, type in 'Y' and a 5 second countdown will begun, meanwhile you hover over this button \n")
        if (ans.upper() == 'Y'):
            for i in range(5, 0, -1):
                sleep(1)
                print(i)
            next_box_location_x, next_box_location_y = pyautogui.position()
            print("your coordinates to open ms_edge are {}, {}".format(next_box_location_x, next_box_location_y))

        # getting coordinates to the agree button
        ans = input("the final step is on the last page, we will need the coordinates to the 'agree' box location. "
                    "When you're ready, type in 'Y' and a 5 second countdown will begun, meanwhile you hover over "
                    "this button \n")
        if (ans.upper() == 'Y'):
            for i in range(5, 0, -1):
                sleep(1)
                print(i)
            agree_box_location_x, agree_box_location_y = pyautogui.position()
            print("your coordinates to open ms_edge are {}, {}".format(agree_box_location_x, agree_box_location_y))

    while(x < number_of_accounts):
        # change IP address here here
        proxyswitch()

        # move to open msedge
        pyautogui.moveTo(ms_edge_x, ms_edge_y)
        pyautogui.click()
        sleep(5)

        # move to main site
        keyboard.write('https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp')
        keyboard.press('enter')
        sleep(5)

        # enter all fields for first page
        first_name = ''.join(random.choice(letters) for i in range(10))
        keyboard.write(first_name)
        sleep(5)
        keyboard.press('tab')

        last_name = ''.join(random.choice(letters) for i in range(10))
        keyboard.write(last_name)
        sleep(5)
        keyboard.press('tab')

        user_name = ''.join(random.choice(letters) for i in range(10))
        keyboard.write(user_name)
        sleep(5)
        keyboard.press('tab')
        keyboard.press('tab')

        pass_word = ''.join(random.choice(letters) for i in range(10))
        keyboard.write(pass_word)
        sleep(5)
        keyboard.press('tab')

        sleep(5)
        keyboard.write(pass_word)
        sleep(1)
        keyboard.press('enter')

        # enter info for second page
        sleep(5)
        pyautogui.moveTo(month_box_location_x, month_box_location_y)
        pyautogui.click()

        sleep(5)
        random_month = random.randint(0, 11)
        if (random_month == 0):
            month = 'j'
        elif (random_month == 1):
            month = 'f'
        elif (random_month == 2):
            month = 'm'
        elif (random_month == 3):
            month = 'a'
        elif (random_month == 4):
            month = 'may'
        elif (random_month == 5):
            month = 'june'
        elif (random_month == 6):
            month = 'july'
        elif (random_month == 7):
            month = 'august'
        elif (random_month == 8):
            month = 's'
        elif (random_month == 9):
            month = 'o'
        elif (random_month == 10):
            month = 'n'
        else:
            month = 'd'
        keyboard.write(month)
        keyboard.press('enter')

        keyboard.press('tab')
        sleep(5)
        random_day = ''.join(random.randint(1, 28))
        keyboard.write(random_day)
        keyboard.press('tab')

        sleep(5)
        random_year = ''.join(random.randint(1980, 2005))
        keyboard.write(random_year)
        keyboard.press('tab')

        random_gender = random.randint(1, 3)
        if (random_gender == 1):
            gender = 'f'
        elif (random_gender == 2):
            gender = 'm'
        else:
            gender = 'r'
        keyboard.write(gender)
        sleep(5)

        screen_x, screen_y = pyautogui.size()
        pyautogui.moveTo(int(screen_x / 10), int(screen_y / 2))
        pyautogui.click()
        keyboard.press('space')
        keyboard.press('space')
        keyboard.press('space')
        pyautogui.moveTo(next_box_location_x, next_box_location_y)
        pyautogui.click()
        sleep(5)

        # final page
        keyboard.press('space')
        keyboard.press('space')
        keyboard.press('space')
        keyboard.press('space')
        pyautogui.moveTo(agree_box_location_x, agree_box_location_y)
        pyautogui.click()
        sleep(5)

        #close and log username/password
        pyautogui.moveTo(screen_x - 1, 0)
        pyautogui.click()
        #put username and password into text file

        #increment
        x+=1