#####################################################
## Discord Bump Bot                                ##
## A bot that automatically bumps a server in dc.  ##
## https://voidsecurity.ml                         ##
## Coded by: drk                                   ##
#####################################################

# Imports
import time
from selenium import webdriver

# Global Variables
driver = webdriver.Chrome("/home/drk/Desktop/coding/python/selenium/driver/chromedriver")
discordmail = "email"
discordpass = "password"
# Code

driver.get("https://discord.com/login")
print("\n\nEntered", driver.title)

elemail = driver.find_element_by_name("email")
elemail.send_keys(discordmail)

elpasswd = driver.find_element_by_name("password")
elpasswd.send_keys(discordpass)

