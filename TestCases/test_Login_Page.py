import time

# import pytest

from PageObjects.Login_Page import LoginPage
from Utilities.Logger import LogGenerator


class Test_Login:
    log = LogGenerator.loggen()

    # @pytest.mark.skip
    def test_page_title(self, open_browser):
        self.log.info("Testcase 'test_page_title' is initiated")

        self.log.info("Opening the browser")
        self.driver = open_browser
        self.lp = LoginPage(self.driver)

        self.log.info("Fetching the URL")
        self.lp.login_url()

        self.log.info("the Page title is:- " + self.driver.title)
        if self.driver.title == "OrangeHRM":
            self.log.info("Page title found")
            time.sleep(2)
            self.driver.save_screenshot(".\\Screenshots\\OrangeHRM_title_pass.PNG")
            self.log.info("Closing the browser")
            self.driver.close()
            self.log.info("Testcase 'test_page_title' is now completed")
            assert True
        else:
            self.log.info("Page title not found")
            time.sleep(2)
            self.driver.save_screenshot(".\\Screenshots\\OrangeHRM_title_fail.PNG")
            self.log.info("Closing the browser")
            self.driver.close()
            self.log.info("Testcase 'test_page_title' is failed")
            assert False

    # @pytest.mark.skip
    def test_login_page(self, open_browser):
        self.log.info("Testcase 'test_login_page' is initiated")

        self.log.info("Opening the browser")
        self.driver = open_browser
        self.lp = LoginPage(self.driver)

        self.log.info("Fetching the URL")
        self.lp.login_url()

        self.log.info("Entering the Username")
        self.lp.enter_username("Admin")

        self.log.info("Entering the Password")
        self.lp.enter_password("admin123")

        self.log.info("Clicking on the login button")
        time.sleep(2)
        self.lp.click_login_button()

        self.log.info("Login successful")
        self.log.info("Clicking on the menu button on top right corner")
        self.lp.click_menu_right_corner()

        self.log.info("Clicking on the logout button")
        time.sleep(1)
        self.lp.click_logout_button()

        time.sleep(2)
        self.log.info("Checking for logout confirmation")
        if self.lp.check_orangehrm_logo() == True:
            self.log.info("OrangeHRM logo found. Logout successful")
            self.driver.save_screenshot(".\\Screenshots\\OrangeHRM_logout_pass.PNG")
            self.log.info("Closing the browser")
            self.driver.close()
            self.log.info("Testcase 'test_login_page' is now completed")
            assert True
        else:
            self.log.info("OrangeHRM logo not found")
            self.driver.save_screenshot(".\\Screenshots\\OrangeHRM_logout_fail.PNG")
            self.log.info("Closing the browser")
            self.driver.close()
            self.log.info("Testcase 'test_login_page' is failed")
            assert False
