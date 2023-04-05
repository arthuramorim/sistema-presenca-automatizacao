from Class.Driver import Driver
from Class.LoginPage import LoginPage
from Class.StudentTransferPage import StudentTransfer

def main():
    loginPage = LoginPage()
    loginPage.open_login_page()
    isLogged = loginPage.login()
    
    if not isLogged:
        print("Não foi possível logar, o sistema pode está instavel ou passando por manutenção") 
        
    studentTransfer = StudentTransfer(loginPage.driver)
    studentTransfer.transfer_student('12312312')
    
    if studentTransfer:
        input('Aguardando...')


if __name__ == "__main__":
    main()

