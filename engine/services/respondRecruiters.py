from engine.browser import *
from time import sleep
import warnings
import config

warnings.filterwarnings("ignore")

class RespondRecruiters():
    def __init__(self, driver):
        self.driver = driver

    def __open_menu_option(self, menu_option_xpath):
        self.driver.find_element(By.XPATH, menu_option_xpath).click()
        sleep(3)

    def accept_connections(self):
        print("[LINKEDIN BOT] Verificando novas conexões")
        try:
            self.driver.get('https://www.linkedin.com/mynetwork/')
            
            sleep(1)
            
            accept_buttons = self.driver.find_elements(By.XPATH, '//button[contains(@aria-label, "Aceitar o convite")]')
            for accept_button in accept_buttons:
                accept_button.click()
                sleep(1)
            sleep(1)
        except Exception as e:
            print(e)
            print("[LINKEDIN BOT] Sem conexões novas")
    
    def __send_message(self, driver, message):
        textarea = driver.find_element(By.XPATH, '//div[contains(@class, "msg-form__msg-content-container")]/div/div/p')
        message = message.replace("\n", Keys.ENTER)
        textarea.send_keys(message)        
        sleep(1)
        driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    
    def __get_answered_users(self):
        file = open('answeredusers.txt', 'r')
        return  [x.strip() for x in file.readlines()]
    
    def answer_job_invitations(self, text):
        print("[LINKEDIN BOT] Respondendo propostas")
        self.__open_menu_option('//*[@id="global-nav"]/div/nav/ul/li[4]/a')
        
        conversations = self.driver.find_elements(By.XPATH, '//div[contains(@id, "conversation")]')  
                  
        for conversation in conversations:
            conversation.click()
            sleep(2)
            
            try:
                author   = conversation.find_element(By.XPATH, '//a[contains(@class, "profile-card-one-to-one")]').text
            except:
                print("[LINKEDIN BOT] Pulando anúncio")
                
            answered_users = self.__get_answered_users()  
            if author == '' or author in answered_users: continue
              
            print(f"[LINKEDIN BOT] Respondendo: {author}")
            messages = conversation.find_elements(By.XPATH, '//li[contains(@class, "msg-s-message-list")]')
            for message in messages:
                author_msg = message.find_element(By.XPATH, '//span[contains(@class, "msg-s-message-group__name")]').text
                if author_msg == author:
                    raw_msg = message.find_element(By.XPATH, '//p[contains(@class, "msg-s-event-listitem__body")]').text
                    if any(x in raw_msg.lower() for x in ['python', 'engenheiro', 'big data', 'de dados', 'data engineer']):
                        self.__send_message(message, text)
                        break
            sleep(2)
        print("[LINKEDIN BOT] Usuários respondidos")
            

        