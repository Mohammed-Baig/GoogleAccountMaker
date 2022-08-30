from time import sleep
import time
from selenium import webdriver
import os
import random
import string
from selenium.webdriver.common.keys import Keys
from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType

# Get free proxies for rotating
def file_size(file):
    num_lines = sum(1 for line in open(file))
    return (num_lines)

def get_free_proxies(driver):
    driver.get('https://sslproxies.org')
    table = driver.find_element(By.TAG_NAME, 'table')
    thead = table.find_element(By.TAG_NAME, 'thead').find_elements(By.TAG_NAME, 'th')
    tbody = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

    headers = []
    for th in thead:
        headers.append(th.text.strip())

    proxies = []
    for tr in tbody:
        proxy_data = {}
        tds = tr.find_elements(By.TAG_NAME, 'td')
        for i in range(len(headers)):
            proxy_data[headers[i]] = tds[i].text.strip()
        proxies.append(proxy_data)

    return proxies

#performs reddit services
def reddit(times_voted, link, anti_key, site_key, chr_path):
    api_key = anti_key

    num_google_bots = file_size("users.txt")
    num_reddit_bots = file_size("reddit_users.txt")
    use_bot = int(input("to perform this vote manipulation would you like to use\n1.Your reddit bots\nor\n2.Your google bots"))
    if(use_bot == 1):

        #check if you have enough bots
        if(times_voted > num_reddit_bots):
            print("you do not have enough bots to accomplish this, making more accounts now")
            ip_type = int(input("would you like to\n1.Use a pre paid proxy\n2.Use a free generated one(less successful)"))
            proxy_ip_port = ''
            proxy_list = []
            if (ip_type == 1):
                proxy_ip = input("enter your proxy ip address here: ")
                proxy_port = input("enter your proxy port here: ")
                proxy_ip_port = '{}:{}'.format(proxy_ip, proxy_port)

            elif (ip_type == 2):
                path = '{}"{}"'.format("r", chr_path)
                driver = webdriver.Chrome(executable_path=path)
                free_proxies = get_free_proxies(driver)
                print(free_proxies)
                x = 0
                while x < len(free_proxies):
                    temp_dict = free_proxies[x]
                    http_status = temp_dict['Https']
                    google_status = temp_dict['Google']
                    if (http_status == 'yes' and google_status == 'yes'):
                        ipaddress = temp_dict['IP Address']
                        port = temp_dict['Port']
                        ip_port = '{}:{}'.format(ipaddress, port)
                        proxy_list.append(ip_port)
                    x += 1
                print(proxy_list)

            df = open('reddit_users.txt', 'a')
            x = 0
            num_needed = times_voted - num_reddit_bots
            while(x < num_needed):

                if (ip_type == 1):
                    proxy = Proxy()
                    proxy.proxy_type = ProxyType.MANUAL
                    proxy.http_proxy = proxy_ip_port
                    proxy.ssl_proxy = proxy_ip_port
                    capabilities = webdriver.DesiredCapabilities.CHROME
                    proxy.add_to_capabilities(capabilities)

                elif (ip_type == 2):
                    proxy_ip_port = random.choice(proxy_list)
                    proxy = Proxy()
                    proxy.proxy_type = ProxyType.MANUAL
                    proxy.http_proxy = proxy_ip_port
                    proxy.ssl_proxy = proxy_ip_port
                    capabilities = webdriver.DesiredCapabilities.CHROME
                    proxy.add_to_capabilities(capabilities)

                # Go to the acc registration site
                path = '{}"{}"'.format("r", chr_path)
                browser = webdriver.Chrome(executable_path=path, desired_capabilities=capabilities)
                browser.implicitly_wait(5)
                browser.get('https://www.reddit.com/register/')
                sleep(2)

                # Generate random email
                letters = string.ascii_lowercase
                EmailName = ''.join(random.choice(letters) for i in range(8))
                Email = (EmailName + '@gmail.com')

                # Input email
                email_input = browser.find_element_by_css_selector("input[name='email']")
                email_input.send_keys(Email)

                # Continue to the next part of the registration process
                continue_button = browser.find_element_by_xpath("//button[@type='submit']")
                continue_button.click()

                # Find and input the username and password fields
                username_input = browser.find_element_by_css_selector("input[name='username']")
                password_input = browser.find_element_by_css_selector("input[name='password']")

                # randomly generate a username
                letters = string.ascii_lowercase
                Username = ''.join(random.choice(letters) for i in range(8))
                Password = ''.join(random.choice(letters) for i in range(8))

                username_input.send_keys(Username)
                password_input.send_keys(Password)

                # Gather site key
                url = browser.current_url

                # Acc do the solving process
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

                # Finish it
                FinishIt = browser.find_element_by_xpath('//button[@type="submit" and text()="Finish"]')
                FinishIt.click()

                # Send username and password to txt or csv file for later use
                df.write(str(Username))
                df.write(' ')
                df.write(str(Password))
                df.write('\n')

                x+=1
            df.close()

        else:
            print("lorem")

    elif(use_bot == 2):

        #check if you have enough bots
        if(times_voted > num_google_bots):
            print("you do not have enough bots to accomplish this, making more accounts now")
            print("We will need some information from you too for this step")

            # get the number of accounts being made
            num_being_made = times_voted - num_google_bots
            # get anticaptcha key
            anticaptcha_key = input("Please enter your anticaptcha key: ")
            # get chromedriver path
            chromedriver_path = input("Please enter your chromedriver path here: ")
            # get sms account details
            sms_username = input("Please enter your getsms username: ")
            sms_password = input("Please enter your getsms password: ")
            make_account(num_being_made, anticaptcha_key, chromedriver_path, sms_username, sms_password)

        else:
            print("lorem")


    else:
        print("invalid input, please try again later")
        quit()

#makes google accounts
def make_account(number_of_accounts, anti_key, chr_path, sms_uid, sms_pass):
    ip_type = int(input("would you like to\n1.Use a pre paid proxy\n2.Use a free generated one(less successful)"))
    proxy_ip_port = ""
    proxy_list = []

    if(ip_type == 1):
        proxy_ip = input("enter your proxy ip address here: ")
        proxy_port = input("enter your proxy port here: ")
        proxy_ip_port = '{}:{}'.format(proxy_ip,proxy_port)

    elif(ip_type == 2):
        path = '{}"{}"'.format("r",chr_path)
        driver = webdriver.Chrome(executable_path=path)
        free_proxies = get_free_proxies(driver)
        print(free_proxies)
        x = 0
        while x < len(free_proxies):
            temp_dict = free_proxies[x]
            http_status = temp_dict['Https']
            google_status = temp_dict['Google']
            if (http_status == 'yes' and google_status == 'yes'):
                ipaddress = temp_dict['IP Address']
                port = temp_dict['Port']
                ip_port = '{}:{}'.format(ipaddress, port)
                proxy_list.append(ip_port)
            x += 1
        print(proxy_list)

    else:
        print("invalid input, please try again later")
        quit()

    df = open('users.txt', 'a')
    x = 0
    number_of_accounts_made = number_of_accounts
    while (x < number_of_accounts_made):

        #if ip_type is 1, keep it, if 2 then iterate through proxy_list on each loop
        if(ip_type == 1):
            proxy = Proxy()
            proxy.proxy_type = ProxyType.MANUAL
            proxy.http_proxy = proxy_ip_port
            proxy.ssl_proxy = proxy_ip_port
            capabilities = webdriver.DesiredCapabilities.CHROME
            proxy.add_to_capabilities(capabilities)

        elif(ip_type == 2):
            proxy_ip_port = random.choice(proxy_list)
            proxy = Proxy()
            proxy.proxy_type = ProxyType.MANUAL
            proxy.http_proxy = proxy_ip_port
            proxy.ssl_proxy = proxy_ip_port
            capabilities = webdriver.DesiredCapabilities.CHROME
            proxy.add_to_capabilities(capabilities)

        api_key = anti_key

        path = '{}"{}"'.format("r", chr_path)
        browser = webdriver.Chrome(executable_path=path, desired_capabilities=capabilities)
        browser.implicitly_wait(5)
        browser.get('https://www.getsmscode.com/user.php')

        email_input = browser.find_element_by_css_selector("input[name='username']")
        email_input.send_keys(sms_uid)

        password_input = browser.find_element_by_css_selector("input[type='password']")
        password_input.send_keys(sms_pass)

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
        df.write(str(username))
        df.write(' ')
        df.write(str(Password))
        df.write('\n')

        # Finally loop the program
        browser.close()

        x += 1
    df.close()


def main():
    print("This program allows you to make google accounts, and then use those accounts for services. You can like a "
          "comment as much as you want, downvote one, give yourself any number of followers on reddit or twitter, "
          "subscribers on youtube, etc.")

    x = int(input("What would you like to do today?\n1.Check number of existing bots\n2.Make more bots\n3.Bot Reddit\n4.Quit\n"))
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

        #get the number of accounts being made
        num_being_made = int(input("Please enter how many accounts you would like to make: "))
        #get anticaptcha key
        anticaptcha_key = input("Please enter your anticaptcha key: ")
        #get chromedriver path
        chromedriver_path = input("Please enter your chromedriver path here: ")
        #get sms account details
        sms_username = input("Please enter your getsms username: ")
        sms_password = input("Please enter your getsms password: ")
        make_account(num_being_made,anticaptcha_key,chromedriver_path,sms_username,sms_password)

    elif (x == 3):
        print("We will need some information from you too for this step")

        num_downvotes = int(input("Enter how many times you would like to downvote/upvote this post"))
        post_link = input("Please enter the link to this post: ")
        anticaptcha_key = input("Please enter your anticaptcha key: ")
        site_key = input("Please enter your site key: ")
        chr_path = input("Please enter your chromedriver path here: ")
        reddit(num_downvotes, post_link, anticaptcha_key, site_key, chr_path)


    elif (x == 4):
        quit()

    else:
        print("Invalid input, please try again later")
        quit()


if __name__ == "__main__":
    main()

