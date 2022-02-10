from selenium.webdriver.common.by import By


class Test_Logout:
    def __init__(self,driver):
        self.driver = driver

    def test_logout(self):
            self.driver.find_element(By.ID, "logout").click()
