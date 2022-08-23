# ____________________________________________________________________________________Getting all the necessary imports_____________________________________________________________________________________
from time import sleep
from selenium import webdriver
import os
import time
import random
import string
from selenium.webdriver.common.keys import Keys
from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
from random import randint

# ____________________________________________________________________________________Navigate to where you'll be getting your number_____________________________________________________________________
api_key = '(INSERT AntiCaptchaKey here)'

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get('https://www.getsmscode.com/user.php')

email_input = browser.find_element_by_css_selector("input[name='username']")
email_input.send_keys("ENTER SITE USERNAME")

password_input = browser.find_element_by_css_selector("input[type='password']")
password_input.send_keys("ENTER SITE PASSWORD")

url = browser.current_url
site_key = "6LfQnD4UAAAAAOpgxHPo0E9gIgGe7PybDDGZ6UQM"

# Acc do the solving process
client = AnticaptchaClient(api_key)
task = NoCaptchaTaskProxylessTask(url, site_key)
job = client.createTask(task)

job.join()

# Receive response
response = job.get_solution_response()
print(response)

# Inject response in webpage
browser.execute_script('document.getElementById("g-recaptcha-response").innerHTML = "%s"' % (response))

# Wait a moment to execute the script (just in case).
time.sleep(1)
continue_button = browser.find_element_by_css_selector("input[name= 'submit']")
continue_button.click()

browser.get('https://www.getsmscode.com/cgetcode.php')
sleep(5)

# ____________________________________________________________________________________Acc start the bulk of the code_____________________________________________________________________________________
number_of_accounts_made = int(input("Enter how many accounts you want to make here:"))
x = 0

while (x < number_of_accounts_made):
    browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
    browser.get('https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp')
    sleep(2)

    # Generate first name
    letters = string.ascii_lowercase
    FirstName = ''.join(random.choice(letters) for i in range(10))
    FirstNameInput = (FirstName)

    # Actually input the first name
    first_name_input = browser.find_element_by_css_selector("input[name='firstName']")
    first_name_input.send_keys(FirstNameInput)

    # Generate first name
    letters = string.ascii_lowercase
    LastName = ''.join(random.choice(letters) for i in range(10))
    LastNameInput = (LastName)

    # Actually input the first name
    last_name_input = browser.find_element_by_css_selector("input[name='lastName']")
    last_name_input.send_keys(LastNameInput)

    # username input
    letters = string.ascii_lowercase
    username = ''.join(random.choice(letters) for i in range(10))
    user_name_input = browser.find_element_by_css_selector("input[name='Username']")
    user_name_input.send_keys(username)

    # Password input
    letters = string.ascii_lowercase
    Password = ''.join(random.choice(letters) for i in range(10))
    password_input = browser.find_element_by_css_selector("input[name='Passwd']")
    password_input.send_keys(Password)

    # password confirmation
    password_confirmation = browser.find_element_by_css_selector("input[name='ConfirmPasswd']")
    password_confirmation.send_keys(Password)

    # Move onto the next section
    co = browser.find_element_by_id("accountDetailsNext")
    co.click()

    # move back to the service
    browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + Keys.TAB)
    sleep(5)

    # get the phone number
    browser.find_element_by_xpath("//input[@type='submit' and @value='Capture Phone Number']").click()
    sleep(5)

    number = browser.find_element_by_css_selector("input[name = 'nMobilenum']")
    number_output = number.get_attribute('value')
    print("your number for run {} is {}".format(x, number_output))
    sleep(5)

    # switch back to input number
    browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + Keys.TAB)
    number_input = browser.find_element_by_xpath("//input[@type='tel' and @id='phoneNumberId']")
    number_input.send_keys(number_output)
    sleep(5)
    Next = browser.find_element_by_css_selector(
        "button[class = 'VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc']")  # if cant find use: browser.find_element_by_tag_name('body').send_keys(Keys.ENTER)
    Next.click()

    # switch back to get msg verification code
    browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + Keys.TAB)
    sleep(30)
    get_sms = browser.find_element_by_css_selector("input[name = 'getcode']")
    get_sms.click()
    sleep(10)
    msg = browser.find_element_by_css_selector("textarea[name = 'Code']")
    msg_output = msg.get_attribute('value')
    msg_output = msg_output[2:8]
    print("The code for run {} is {}".format(x, msg_output))

    # switch back to put in the code
    browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + Keys.TAB)
    sms_code_input = browser.find_element_by_xpath("//input[@type='tel' and @id='code']")
    sms_code_input.send_keys(msg_output)
    sleep(5)
    Verify = browser.find_element_by_css_selector(
        "button[class = 'VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc']")  # if cant find use: browser.find_element_by_tag_name('body').send_keys(Keys.ENTER)
    Verify.click()

    # Finishing touches like gender, bday, etc
    day_input = browser.find_element_by_css_selector("input[name = 'day']")
    random_day = randint(1, 28)
    day_input.send_keys(str(random_day))

    year_input = browser.find_element_by_css_selector("input[name = 'year']")
    random_year = randint(1995, 2005)
    year_input.send_keys(str(random_year))

    month_input = browser.find_element_by_id('month')
    month_input.click()
    random_month = randint(0, 11)
    if (random_month == 0):
        month = "j"
    elif (random_month == 1):
        month = "f"
    elif (random_month == 2):
        month = "m"
    elif (random_month == 3):
        month = "a"
    elif (random_month == 4):
        month = "may"
    elif (random_month == 5):
        month = "june"
    elif (random_month == 6):
        month = "july"
    elif (random_month == 7):
        month = "august"
    elif (random_month == 8):
        month = "s"
    elif (random_month == 9):
        month = "o"
    elif (random_month == 10):
        month = "n"
    else:
        month = "d"
    month_input.send_keys(month)
    browser.find_element_by_tag_name('body').send_keys(Keys.ENTER)

    gender_choice = browser.find_element_by_id('gender')
    gender_choice.click()
    random_gender = randint(1, 3)
    if (random_gender == 1):
        gender = "f"
    elif (random_gender == 2):
        gender = "m"
    else:
        gender = "r"
    gender_choice.send_keys(gender)
    browser.find_element_by_tag_name('body').send_keys(Keys.ENTER)

    next_button = browser.find_element_by_css_selector(
        "button[class = 'VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc']")
    next_button.click()

    sleep(2)
    skip_button = browser.find_element_by_css_selector(
        "button[class = 'VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc']")
    skip_button.click()

    sleep(2)
    browser.find_element_by_tag_name('body').send_keys(Keys.SPACE)
    browser.find_element_by_tag_name('body').send_keys(Keys.SPACE)

    sleep(2)
    agree_button = browser.find_element_by_id('termsofserviceNext')
    agree_button.click()

    # Send username and password to txt or csv file for later use
    # TO BE CONTINUED...

    # Finally loop the program
    browser.close()
    print("google username{}: {}".format(x, username))
    print("google username{}: {}".format(x, Password))
    x += 1