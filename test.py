#test file to test libraries and various other services

#driver.get('http://whatismyipaddress.com')
from selenium import webdriver
from time import sleep
import undetected_chromedriver.v2 as uc

def main():
    username = 'hello'
    username = username + "@gmail.com"
    print(username)



if __name__ == "__main__":
    main()