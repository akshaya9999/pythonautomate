#! python3
#commandlineemailer.py - takes email from the command line 



from selenium import webdriver

import time
#to login
try:
    browser = webdriver.Firefox()
    browser.get('https://accounts.google.com/v3/signin/identifier?dsh=S2013299222%3A1674659831118234&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AWnogHceKjdE1TuQGz7YkolGG8Q52jPrwfPVvCSJvzkTCfvltzX-gcvBFIRqbrHkjkuG-bL1IHad')
    userElem = browser.find_element_by_id('identifierId')
    name=input('enter email')
    userElem.send_keys(name)
    nextbutt = browser.find_element_by_id('identifierNext')
    nextbutt.click()
    time.sleep(10)
    passwordElem = browser.find_element_by_name('Passwd')
    passw=input("enter password")
    passwordElem.send_keys(passw)
    nextbutt1 = browser.find_element_by_id('passwordNext')
    nextbutt1.click()
    time.sleep(10)
except:
    print("login failed")

#to send mail
time.sleep(10)
browser.get('https://mail.google.com/mail/u/0/#inbox?compose=new')
time.sleep(20)
recipient=browser.find_element_by_css_selector('#\:cf')
recmail=input("enter recipients address")
recipient.send_keys(recmail)
time.sleep(20)
subject=browser.find_element_by_css_selector('#\:8h')
sub=input("enter the subject")
subject.send_keys(sub)
time.sleep(20)
body=browser.find_element_by_css_selector('#\:9q')
bodyip=input("enter the body")
body.send_keys(bodyip)
time.sleep(20)
submit=browser.find_element_by_css_selector('#\:87')
submit.click()
time.sleep(5)