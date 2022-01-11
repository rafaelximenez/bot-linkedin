from engine.browser import *
from time import sleep
import config


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
    
    
    def search_jobs(self, term): 
        print("[LINKEDIN BOT] Buscando vagas")           
        search = self.driver.find_element(By.XPATH, '//input[@placeholder="Pesquisar"]')
        search.send_keys(term)
        search.send_keys(Keys.RETURN)
        sleep(1)
    
    def __open_menu_option(self, menu_option_xpath):
        self.driver.find_element(By.XPATH, menu_option_xpath).click()
        sleep(3)
        
    def accept_connections(self):
        print("[LINKEDIN BOT] Verificando novas conexões")
        try:
            self.__open_menu_option('//a[@data-link-to="mynetwork"]')
            invites = self.driver.find_elements(By.XPATH, '//li[contains(@class, "invitation-card")]')
            
            for invite in invites:
                invite.find_element(By.XPATH, '//button[contains(@aria-label, "Aceitar")]').click()
                sleep(1)
            sleep(1)
        except:
            print("[LINKEDIN BOT] Sem conexões novas")
    
    def __send_message(self, driver, message):
        textarea = driver.find_element(By.XPATH, '//div[contains(@class, "msg-form__msg-content-container")]/div/div/p')
        message = message.replace("\n", Keys.ENTER)
        textarea.send_keys(message)        
        sleep(1)
        #driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        
    
    def make_log(self, filename, text):
        with open(f'{filename}.txt', 'a') as f:
            f.write(text) 
    
    def __get_answered_users(self):
        file = open('answeredusers.txt', 'r')
        return  [x.strip() for x in file.readlines()]
    
    def answer_job_invitations(self, text):
        print("[LINKEDIN BOT] Respondendo propostas")
        self.__open_menu_option('//a[@data-link-to="messaging"]')
        
        conversations = self.driver.find_elements(By.XPATH, '//div[contains(@id, "conversation")]')  
                  
        for conversation in conversations:
            conversation.click()
            sleep(2)
            
            try:
                author   = conversation.find_element(By.XPATH, '//a[contains(@class, "profile-card-one-to-one")]').text
            except:
                print("[LINKEDIN BOT] Pulado anúncio")
                
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
                        self.make_log('answeredusers', f'{author}\n')
                        break
            sleep(2)
        print("[LINKEDIN BOT] Usuários respondidos")
            

        