from selenium.webdriver.common.by import By

from Lib.BasePage import Baseclass
from TestCases.LogoutTest import Test_Logout


class Test_Login(Baseclass):

    def test_login(self):
        print("Hello")
        self.driver.find_element(By.NAME, "username").send_keys("support@moveon4.com")
        self.driver.find_element(By.NAME, "password").send_keys("Moveon@30000")
        self.driver.find_element(By.NAME, "label_button_login").click()
        user_login= self.driver.find_element(By.ID,"loginDetails").text
        assert user_login == "surname_1, firstname_1"
        '''
        This is a multiline
        comment.
        '''
        logout = Test_Logout(self.driver)
        logout.test_logout()

