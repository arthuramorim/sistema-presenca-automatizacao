import os
dotenv_path = './.env'
from dotenv import load_dotenv
load_dotenv(dotenv_path)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class StudentTransfer():
    def __init__(self, driver):
        self.driver = driver
        self.nis_student_input = (By.ID, "mat-input-2")
        self.search_button = (By.ID, "btnPesquisar")
        self.transfer_button = (By.XPATH, "//td/button")
        self.inep_school_input = (By.ID, "")
        
    def open_student_transfer_page(self):
        self.driver.get(os.getenv('TRANSFER_PAGE_URL'))
        
          
    def load_student_transfer_page(self)-> bool:
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "mat-input-2")))
            return True
        except:
            return False  
        
       
    def fill_nis_student_input(self, nis_student):
        nis_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "mat-input-2")))
        nis_input.send_keys(nis_student)
        
    #parei aqui, preciso criar a regra de verificação se a pagina de transferencia já foi aberta.
    def transfer_student(self, nis_student):
        if not self.load_student_transfer_page():
            self.open_student_transfer_page()
        
        if not len(nis_student) == 13:
            print ("Nis invalido!")
            return False
        
        self.fill_nis_student_input(nis_student)

    