from selenium import webdriver
import copy
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

emails1 = ['EmailPersonA@example.com', 'EmailPersonB@example.com', 'EmailPersonC@example.com', 'EmailPersonD@example.com']
names1 = ['Person A', 'Person B', 'Person C', 'Person D']

emails = ['scarlatalinn@gmail.com', 'denisa_vatulescu@yahoo.com']
names = ['Ionut', 'Denisa']

address = 'https://mail.google.com/mail/u/0/h/prfn4k4j6fjk/?zy=e&f=1'
email_address = 'santaklausautomation@gmail.com'
email_password = 'SantaKlaus1234#'


def match_santa(names):
    my_new_list = names
    choose = copy.copy(my_new_list)
    result = []
    for i in my_new_list:
        names = copy.copy(my_new_list)
        names.pop(names.index(i))
        chosen = random.choice(list(set(choose) & set(names)))
        result.append((i, chosen))
        choose.pop(choose.index(chosen))
    return result


ms_result = match_santa(names)
final = zip(ms_result, emails)
final = list(final)



# open Chrome
driver = webdriver.Chrome('D:\chromedriver')
driver.get(address)
driver.maximize_window()

# fill the email
login_email = driver.find_element_by_xpath('//*[@id="identifierId"]')
login_email.send_keys(email_address)

# find and press the Submit button
submit_button = driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
submit_button.click()
time.sleep(2)

# find and fill the password
WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.NAME, 'password'))
        )
password_email = driver.find_element_by_name('password')
password_email.send_keys(email_password)

password_button = driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span')
password_button.click()


def match_emails(email):
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/table[3]/tbody/tr/td[1]/table[1]/tbody/tr[1]/td/b/a'))
    )
    send_button = driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td[1]/table[1]/tbody/tr[1]/td/b/a')
    send_button.click()

    to_address = driver.find_element_by_name('to')
    to_address.click()
    to_address.send_keys(email[1])

    subject_email = driver.find_element_by_name('subject')
    subject_email1 = 'HELLO SECRET SANTA ' + str(email[0][0]).upper()
    subject_email.send_keys(subject_email1)

    body_text = driver.find_element_by_name('body')
    body1 = "Hello, " + str(email[0][0] + "!")
    body2 = "\n\nYou will be Secret Santa for: "
    body3 = "\nLoading...\nLoading...\nLoading...\nLoading..."
    body4 = "\n" + str(email[0][1])
    body5 = "\n\n\nThe budget is 10 euros!"
    body6 = "\n\nMerry Christmas! Ho Ho Ho!!!"
    body_text.send_keys(body1 + body2 + body3 + body4 + body5 + body6)

    send_button2 = driver.find_element_by_name('nvp_bu_send')
    send_button2.click()


def send_emails():
    for email in final:
        match_emails(email)


send_emails()
driver.close()
