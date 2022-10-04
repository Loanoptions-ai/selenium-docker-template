from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
import os

def lambda_handler(event, context):

    options = Options()
    options.binary_location = '/var/task/headless-chromium/headless-chromium'
    options.add_argument('--headless')
    options.add_argument("download.default_directory=C:/Users/Nirlep/Desktop")
    options.add_argument('--no-sandbox')
    options.add_argument('--start-maximized')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome('/var/task/chromedriver/chromedriver',chrome_options=options)
    driver.get('https://www.google.com')
    return {
        "statusCode": 200,
        "title": str(driver.title)
    }
        