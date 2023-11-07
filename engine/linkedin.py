from engine.browser import *
from time import sleep
import warnings
import config

warnings.filterwarnings("ignore")

class Linkedin(Browser):
    def __init__(self):
        super().__init__()
        self.driver.get(f'{config.URL}')
    
    def login(self):
        print("[LINKEDIN BOT] Realizando login")
        try:
            self.driver.get(config.URL)

            input_email = self.driver.find_element(By.ID, 'username')
            input_password = self.driver.find_element(By.ID, 'password')

            input_email.send_keys(config.EMAIL)
            input_password.send_keys(config.PASSWORD)

            btn_login = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
            btn_login.click()

            sleep(3)
        except:
            print("[LINKEDIN BOT] Usuário já esta logado!")
        finally:
            return self.driver