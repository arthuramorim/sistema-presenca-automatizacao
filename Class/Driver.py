from selenium import webdriver

class Driver:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        
           
    def navigate_to(self, url):
        self.driver.get(url)
    

