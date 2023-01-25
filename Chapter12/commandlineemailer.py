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
    time.sleep(5)
    passwordElem = browser.find_element_by_name('Passwd')
    passw=input("enter password")
    passwordElem.send_keys(passw)
    nextbutt1 = browser.find_element_by_id('passwordNext')
    nextbutt1.click()
    time.sleep(5)
except:
    print("login failed")

#to send mail
time.sleep(5)
browser.get('https://mail.google.com/mail/u/0/#inbox?compose=new')
time.sleep(5)
recipient=browser.find_element_by_name('to')
recmail=input("enter recipients address")
recipient.send_keys(recmail)
time.sleep(5)
subject=browser.find_element_by_name('subjectbox')
sub=input("enter the subject")
subject.send_keys(sub)
time.sleep(5)
body=browser.find_element_by_name('body')
bodyip=input("enter the body")
body.send_keys(bodyip)
time.sleep(5)
submit=browser.find_element_by_name('send')
submit.click()
time.sleep(5)