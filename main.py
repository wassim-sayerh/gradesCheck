#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 21:38:53 2019

@author: wassim
"""

#%%
#Import libraries

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import smtplib, ssl


from time import sleep
import time
import datetime

#Get to page and sign in

first_iteration = True

def sendEmail() :

    port = 465  # For SSL
    
    from inputs import emailSMTP as emailSMTP
    from inputs import passwordSMTP as passwordSMTP
   
    # Create a secure SSL context
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(emailSMTP, passwordSMTP)
        
    sender_email = emailSMTP
    receiver_email = emailSMTP
    message = """\
    Subject: New grade available
    
    Please check the portal, a new grade is available for you"""

    server.sendmail(sender_email, receiver_email, message)


while True:

    browser = webdriver.Firefox(executable_path='./geckodriver')
    browser.maximize_window()
    
    
    browser.get("https://campus.ie.edu")
    
    
    from inputs import email as userEmail
    from inputs import password as userPassword
    
    username = browser.find_element_by_id('userNameInput')
    username.send_keys(userEmail)
    
    password = browser.find_element_by_id('passwordInput')
    password.send_keys(userPassword)
    
    login = browser.find_element_by_id('submitButton')
    login.click()
    
    browser.get("https://campus.ie.edu/webapps/osc-BasicLTI-BBLEARN/tool.jsp?lti_page=usertool&id=checkg&returnUrl=/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_1_1&tabId=_1_1&forwardUrl=index.jsp")
    
    browser.switch_to.window(browser.window_handles[1])
    
    gradesRows = browser.find_elements_by_xpath("//div[@id='divNotasIE']//tbody//tr")
    
    oldGrades = {}
    newGrades = {}
    
    for row in gradesRows:
        courseName = row.find_elements_by_xpath(".//td")[0].text
        courseGrade = row.find_elements_by_xpath(".//td")[1].text
        
        newGrades[courseName] = courseGrade
        
    
    if oldGrades = {}: #If first iteration
        oldGrades = newGrades
        browser.quit()
        sleep(5 * 60)
        continue
    
    if oldGrades != newGrades:
        sendEmail()
        browser.quit()
        sleep(5 * 60)
        continue
        
    oldGrades = newGrades
    browser.quit()
    sleep(5 * 60)
    
    

