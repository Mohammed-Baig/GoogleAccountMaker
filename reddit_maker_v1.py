from time import sleep
from selenium import webdriver
from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
import os
import time
import random
import string

#Gather Api Key
api_key = (INSERT API KEY HERE)

for x in range(5):

    #Go to the acc registration site
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get('https://www.reddit.com/register/')
    sleep(2)

   #Generate random email
    letters = string.ascii_lowercase
    EmailName = ''.join(random.choice(letters) for i in range(8))
    Email = (EmailName +'@gmail.com')

   #Input email
    email_input = browser.find_element_by_css_selector("input[name='email']")
    email_input.send_keys(Email)

    #Continue to the next part of the registration process
    continue_button = browser.find_element_by_xpath("//button[@type='submit']")
    continue_button.click()

    #Find and input the username and password fields
    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")

    #randomly generate a username
    letters = string.ascii_lowercase
    Username = ''.join(random.choice(letters) for i in range(8))

    username_input.send_keys(Username)
    password_input.send_keys(INSERT PASSWORD HERE)

    #Wait for Reddits dumbass "YoUve BeeN DoInG ThIs Too Much" shit to end
    print("Waiting for this stupid reddit shit to end")
    sleep(540)

    #Gather site key
    url = browser.current_url
    site_key = (INSERT SITE KEY HERE)

    #Acc do the solving process
    client = AnticaptchaClient(api_key)
    task = NoCaptchaTaskProxylessTask(url, site_key)
    job = client.createTask(task)
    print("Waiting for recaptcha solution")
    job.join()

    # Receive response
    response = job.get_solution_response()
    print(response)
    print("Solution has been gotted")

    # Inject response in webpage
    browser.execute_script('document.getElementById("g-recaptcha-response").innerHTML = "%s"' % (response))
    print("Injecting Solution")

    # Wait a moment to execute the script (just in case).
    time.sleep(1)
    print("Solution has been gotted for sure")


    # Press submit button
    Signup = browser.find_element_by_xpath('//button[@type="submit" and text()="Sign Up"]')
    Signup.click()

    #Finish it
    FinishIt = browser.find_element_by_xpath('//button[@type="submit" and text()="Finish"]')
    FinishIt.click()

    # Open a new window
    sleep(10)
    browser.execute_script("window.open('');")

    # Switch to the new window and open URL B
    browser.switch_to.window(browser.window_handles[1])
    browser.get(SITE YOU WOULD LIKE TO UPVOTE/DOWNVOTE)

    #Actually click the upvote button(I hope)
    sleep(10)
    upvote_button = browser.find_element_by_xpath('//button[@id = (ID OF BUTTON HERE)]')
    upvote_button.click()

    browser.close()