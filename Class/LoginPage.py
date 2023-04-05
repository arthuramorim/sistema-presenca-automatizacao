import os
dotenv_path = './.env'
from dotenv import load_dotenv
load_dotenv(dotenv_path)

from Class.Driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginPage(Driver):
    def __init__(self):
        super().__init__()        
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "kc-login")
    
    def open_login_page(self): 
        self.driver.get(os.getenv('LOGIN_PAGE_URL'))
  
    def fill_username(self, username):
        username_locator = self.username_input
        username_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(username_locator))
        username_element.clear()
        username_element.send_keys(username)

    def fill_password(self, password):
        password_locator = self.password_input
        password_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(password_locator))
        password_element.clear()
        password_element.send_keys(password)
        
    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.login_button)).click()
        
    def error_exists(self) -> bool:
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "input-error")))
            return True
        except:
            return False

    def login_successful(self) -> bool: 
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Página Inicial')]")))
            return True
        except:
            return False
                        
    def login(self):
        username = os.getenv('USER_LOGIN') #input('Enter your email: ')
        password = os.getenv('USER_PASSWORD') #input('Enter your password: ')
                            
        self.fill_username(username)
        self.fill_password(password)
        
        self.click_login_button()
        
        if self.error_exists():
            while self.error_exists():
                print("Invalid username or password")
                self.login()

        if not self.login_successful():
            self.open_login_page()
            self.login()
        
        return True




