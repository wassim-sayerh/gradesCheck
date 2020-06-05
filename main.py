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


from time import sleep
import time
import datetime

#Get to page and sign in

first_iteration = True


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
    
    grades = {}
    
    for row in gradesRows:
        courseName = row.find_elements_by_xpath(".//td")[0].text
        courseGrade = row.find_elements_by_xpath(".//td")[1].text
        
        grades[courseName] = courseGrade
        
    
    if first_iteration:
        continue
    
    browser.quit()
    sleep(5 * 60)
    
    

