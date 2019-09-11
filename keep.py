#! python3
# A script to run to automate Google's Keep extension 
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Title of note on keep
noteTitle = input('Please enter week: ')

# Retrieves driver
driver = webdriver.Chrome('/your/path/to/chrome/webdriver/here')  
# Takes chrome to keep.google.com
driver.get('https://keep.google.com')
# Enters username
email = driver.find_element_by_name('identifier')
email.send_keys('EMAIL HERE')
email.send_keys(Keys.ENTER)

# Pauses program so webpage can keep up with program 
time.sleep(1) 

# Enters users password
password = driver.find_element_by_css_selector('input.whsOnd.zHQkBf')
password.send_keys('PASSWORD HERE')
password.send_keys(Keys.ENTER)

# Pauses program so webpage can keep up with program 
time.sleep(1)

# Creates new list
new_list = driver.find_element_by_css_selector('div.Q0hgme-LgbsSe.Q0hgme-Bz112c-LgbsSe.RmniWd-rymPhb.VIpgJd-LgbsSe')
new_list.click()

# Creates title 
title = driver.find_element_by_css_selector('div.notranslate.IZ65Hb-YPqjbf.fmcmS-x3Eknd.r4nke-YPqjbf')
title.send_keys('Fall B2 - Week {}'.format(noteTitle))

# Creates list item
listItem = driver.find_element_by_css_selector('div.notranslate.IZ65Hb-YPqjbf.fmcmS-x3Eknd.CmABtb-YPqjbf')

listItem.send_keys('LIST ITEM 1', Keys.ENTER, 
	'LIST ITEM 2', Keys.ENTER, 
	'LIST ITEM 3', Keys.ENTER, 
	'LIST ITEM 4', Keys.ENTER, 
	'LIST ITEM 5', Keys.ENTER, 
	'LIST ITEM 6')
