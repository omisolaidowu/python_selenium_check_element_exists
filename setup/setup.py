from selenium import webdriver
from dotenv import load_dotenv
import os
import warnings
import urllib3
load_dotenv('.env')
LT_USERNAME = os.getenv("LT_USERNAME")
LT_ACCESS_KEY = os.getenv("LT_ACCESS_KEY")

desired_caps = {
		'LT:Options' : {
			"user" : os.getenv("LT_USERNAME"),
			"accessKey" : os.getenv("LT_ACCESS_KEY"),
			"build" : "Dropdown test-1",
			"name" : "Dropdown test",
			"platformName" : os.getenv("test_OS")
		},
		"browserName" : "Chrome",
		"browserVersion" : "114.0",
	}
gridURL = "https://{}:{}@hub.lambdatest.com/wd/hub".format(LT_USERNAME, LT_ACCESS_KEY)


class Setting:    
    def __init__(self):
        self.driver = webdriver.Remote(command_executor=gridURL, desired_capabilities= desired_caps)
  
    def setUp(self):
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    
    def tearDown(self):
        if (self.driver != None):
            self.driver.quit()