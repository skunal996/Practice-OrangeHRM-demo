from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    Enter_username_cl = (By.XPATH, "//input[@placeholder='Username']")
    Enter_password_cl = (By.XPATH, "//input[@placeholder='Password']")
    Click_login_button_cl = (By.XPATH, "//button[@type='submit']")
    Click_menu_right_corner_cl = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    Click_logout_button_cl = (By.XPATH, "//a[normalize-space()='Logout']")

    Check_OrangeHRM_logo_cl = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]")

    def __init__(self, login):
        self.driver = login
        self.wait = WebDriverWait(self.driver, 20)

    def login_url(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.wait.until(expected_conditions.visibility_of_element_located(self.Enter_username_cl))

    def enter_username(self, username):
        self.driver.find_element(*LoginPage.Enter_username_cl).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*LoginPage.Enter_password_cl).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*LoginPage.Click_login_button_cl).click()

    def click_menu_right_corner(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_menu_right_corner_cl))
        self.driver.find_element(*LoginPage.Click_menu_right_corner_cl).click()

    def click_logout_button(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_logout_button_cl))
        self.driver.find_element(*LoginPage.Click_logout_button_cl).click()

    def check_orangehrm_logo(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Check_OrangeHRM_logo_cl))
        try:
            self.driver.find_element(*LoginPage.Check_OrangeHRM_logo_cl)
            return True
        except:
            return False
