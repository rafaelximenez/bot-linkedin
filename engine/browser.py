from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from chromedriver_autoinstaller import install
from selenium.webdriver.common.by import By
from os import path, getcwd

class Browser:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()

        install()

        profile = path.join(getcwd(), "profile", "cache")

        chrome_options.add_argument(r"user-data-dir={}".format(profile))
        chrome_options.add_argument("--profile-directory=Default")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--mute-audio")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        
    def __del__(self):
        self.driver.close()