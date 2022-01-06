from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from chromedriver_autoinstaller import install
from selenium.webdriver.common.by import By
from os import path, getcwd
from time import sleep

import config

chrome_options = webdriver.ChromeOptions()

install()

profile = path.join(getcwd(), "profile", "cache")

chrome_options.add_argument(r"user-data-dir={}".format(profile))
chrome_options.add_argument("--profile-directory=Default")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get(config.URL)

    input_email = driver.find_element(By.ID, 'username')
    input_password = driver.find_element(By.ID, 'password')

    input_email.send_keys(config.EMAIL)
    input_password.send_keys(config.PASSWORD)

    btn_login = driver.find_element(By.XPATH, '//button[@type="submit"]')
    btn_login.click()

    sleep(3)
except:
    print('Usuário já esta logado!')

search = driver.find_element(By.XPATH, '//input[@placeholder="Pesquisar"]')
search.send_keys('Python')
search.send_keys(Keys.RETURN)

input('')