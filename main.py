from time import sleep
from selenium import webdriver
import os
import time
import random
import string
from selenium.webdriver.common.keys import Keys
from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
from random import randint


def make_account():
    print("lorem")


def main():
    print("This program allows you to make google accounts, and then use those accounts for services. You can like a "
          "comment as much as you want, downvote one, give yourself any number of followers on reddit or twitter, "
          "subscribers on youtube, etc.")

    x = int(input("What would you like to do today?\n1.Check number of existing bots\n2.Make more bots\n3.Quit\n"))
    if (x == 1):
        num_lines = sum(1 for line in open('users.txt'))
        print(num_lines)
        y = int(input("would you like to\n1.return to main menu\n2.quit\n"))
        if (y == 1):
            main()

        elif (y == 2):
            quit()

        else:
            print("invalid input, please try again later")
            quit()

    elif (x == 2):
        print("We will need some information from you too for this step")


    elif (x == 3):
        quit()

    else:
        print("Invalid input, please try again later")
        quit()


if __name__ == "__main__":
    main()
