from pageLayout.OrgHrm import OrangeHRM
from Utilities.Logger import LogGenerator
import allure
from allure_commons.types import AttachmentType
from Utilities.ReadC0nfig import ReadConfigOrange
import pytest
import time
class Test_Orange_HRM:
    Username = ReadConfigOrange.GetUserName()
    Password = ReadConfigOrange.GetPassword()
    log=LogGenerator.loggen()

    @allure.title("Orange HRM")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    @allure.story("OrangeHrm Page Title test case ")
    @allure.id("test_orange_title_001")

    def test_orange_title_001(self,setup):
        self.log.info("test case test_orange_title_001 is start ")
        self.driver = setup
        self.log.info("open Browser ")
        self.lp = OrangeHRM(self.driver)
        self.log.info("open url of OrangeHRM")
        self.lp.OrgHRM_Url()
        self.log.info("page title is "+ self.driver.title)
        if self.driver.title == "OrangeHRM":
            self.log.info("taking screenshot")
            self.lp.take_screenshot()
            self.driver.save_screenshot("D:\\programming\\OrangeHrm\\ScreenShot\\test_orange_title_001_pass.png")
            allure.attach(self.driver.get_screenshot_as_png(),name="test_orange_title_001_Pass",attachment_type=AttachmentType.PNG)
            self.driver.close()
            self.log.info("test case test_orange_title_001 is pass ")
            assert True
        else:
            self.log.info("taking screenshot")
            self.driver.save_screenshot("D:\\programming\\OrangeHrm\\ScreenShot\\test_orange_title_001_fail.png")
            allure.attach(self.driver.get_screenshot_as_png(),name="test_orange_title_001_fail",attachment_type=AttachmentType.PNG)
            self.driver.close()
            self.log.info("test case test_orange_title_001 is fail ")
            assert False

    @allure.title("Orange HRM")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    @allure.story("OrangeHrm Login  test case ")
    @allure.id("test_orange_login_002")
    def test_orange_login_002(self,setup):
        self.log.info("test case test_orange_login_002 is start ")
        self.driver = setup
        self.log.info("open browser")
        self.lp=OrangeHRM(self.driver)
        self.log.info("open url of orange Hrm ")
        self.lp.OrgHRM_Url()
        self.log.info("entering user name  ")
        self.lp.Eentr_username("Admin")
        self.log.info("entering password ")
        self.lp.Enter_password("admin123")
        self.log.info("click login button ")
        self.lp.Click_loginButton()
        self.log.info("checking loging status ")
        if self.lp.Login_Status()==True:
            self.log.info("taking screenshot")
            self.driver.save_screenshot("D:\\programming\\OrangeHrm\\ScreenShot\\test_orange_login_002_pass.png")
            allure.attach(self.driver.get_screenshot_as_png(),name="test_orange_login_002_Pass",attachment_type=AttachmentType.PNG)
            self.log.info("click on menu button  ")
            self.lp.Click_menuButton()
            self.log.info("click on logout button ")
            self.lp.Click_logout()
            self.driver.close()
            self.log.info("test case test_orange_login_002 is pass" )
            assert True
        else:
            self.log.info("taking screenshot")
            self.driver.save_screenshot("D:\\programming\\OrangeHrm\\ScreenShot\\test_orange_login_002_fail.png")
            allure.attach(self.driver.get_screenshot_as_png(),name="test_orange_login_002_fail",attachment_type=AttachmentType.PNG)
            self.driver.close()
            self.log.info("test case test_orange_login_002 is fail ")
            assert False

    @pytest.mark.con
    @allure.title("Orange HRM")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    @allure.story("OrangeHrm Login  test case ")
    @allure.id("test_orange_login_config_003")

    def test_orange_login_config_003(self,setup):
        self.log.info("test case test_orange_login_002 is start ")
        self.driver = setup
        self.log.info("open browser")
        self.lp=OrangeHRM(self.driver)
        self.log.info("open url of orange Hrm ")
        self.lp.OrgHRM_Url()
        self.log.info("entering user name  ")
        self.lp.Eentr_username(self.Username)
        self.log.info("entering password ")
        self.lp.Enter_password(self.Password)
        self.log.info("click login button ")
        self.lp.Click_loginButton()
        self.log.info("checking loging status ")
        if self.lp.Login_Status()==True:
            self.log.info("taking screenshot")
            self.driver.save_screenshot("D:\\programming\\OrangeHrm\\ScreenShot\\test_orange_login_config_003_pass.png")
            allure.attach(self.driver.get_screenshot_as_png(),name="test_orange_login_config_003_Pass",attachment_type=AttachmentType.PNG)
            self.log.info("click on menu button  ")
            self.lp.Click_menuButton()
            self.log.info("click on logout button ")
            self.lp.Click_logout()
            self.driver.close()
            self.log.info("test case test_orange_login_002 is pass" )
            assert True
        else:
            self.log.info("taking screenshot")
            self.driver.save_screenshot("D:\\programming\\OrangeHrm\\ScreenShot\\test_orange_login_config_003_fail.png")
            allure.attach(self.driver.get_screenshot_as_png(),name="test_orange_login_config_003_fail",attachment_type=AttachmentType.PNG)
            self.driver.close()
            self.log.info("test case test_orange_login_002 is fail ")
            assert False

