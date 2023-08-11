from pageLayout.OrgHrm import OrangeHRM
from Utilities.Logger import LogGenerator
from Utilities import XLorg
import allure
from allure_commons.types import AttachmentType
import time
class Test_Orange_HRM_DDT:
    log=LogGenerator.loggen()
    XlPath = "D:\\programming\\OrangeHrm\\test_case\\Test_Data\\Orange.xlsx"

    @allure.title("Orange HRM")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    @allure.story("OrangeHrm page title test case")
    @allure.id("test_orange_title_ddt_001")

    def test_orange_title_ddt_001(self,setup):
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
            self.driver.save_screenshot("D:\\programming\\OrangeHrm\\ScreenShot\\test_orange_title_ddt_001_pass.png")
            allure.attach(self.driver.get_screenshot_as_png(),name="test_orange_title_ddt_001_pass",attachment_type=AttachmentType.PNG)
            self.driver.close()
            self.log.info("test case test_orange_title_001 is pass ")
            assert True
        else:
            self.log.info("taking screenshot")
            self.driver.save_screenshot("D:\\programming\\OrangeHrm\\ScreenShot\\test_orange_title_ddt_001_fail.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_orange_title_ddt_001_fail", attachment_type=AttachmentType.PNG)
            self.driver.close()
            self.log.info("test case test_orange_title_001 is fail ")
            assert False

    @allure.title("Orange HRM")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    @allure.story("OrangeHrm Login test case ")
    @allure.id("test_orange_login_DDT_002")
    def test_orange_login_DDT_002(self,setup):
        self.log.info("test case test_orange_login_002 is start ")
        self.driver = setup
        self.log.info("open browser")
        self.lp=OrangeHRM(self.driver)
        self.log.info("open url of orange Hrm ")
        self.lp.OrgHRM_Url()
        self.row = XLorg.RowCount(self.XlPath,"Sheet1")
        self.log.info("total number of row " + str(self.row))

        Login_status_List = []
        time.sleep(3)
        for r in range (2,self.row+1):
            self.user = XLorg.ReadData(self.XlPath,"Sheet1",r,2)
            self.password = XLorg.ReadData(self.XlPath,"Sheet1",r,3)
            self.exp_result = XLorg.ReadData(self.XlPath,"Sheet1",r,4)
            # time.sleep(5)
            self.lp.OrgHRM_Url()

            self.log.info("entering user name ")
            self.lp.Eentr_username(self.user)
            self.log.info("entering password ")
            self.lp.Enter_password(self.password)
            self.log.info("click login button ")
            self.lp.Click_loginButton()
            self.log.info("checking loging status ")


            if self.lp.Login_Status()==True:

                if self.exp_result=="Pass" :

                    Login_status_List.append("Pass")
                    self.log.info("taking screenshot")
                    self.driver.save_screenshot("D:\\programming\\OrangeHrm\\ScreenShot\\test_orange_login_00"+str(r)+"_pass.png")
                    allure.attach(self.driver.get_screenshot_as_png(), name="test_orange_login_00"+str(r)+"_pass" , attachment_type=AttachmentType.PNG)
                    self.log.info("click on menu button ")
                    self.lp.Click_menuButton()
                    self.log.info("click on logout button ")
                    self.lp.Click_logout()
                    self.driver.close()
                    self.log.info("test case test_orange_login_002 is pass" )
                    self.log.info("write data in excel")
                    XLorg.WriteData(self.XlPath,"Sheet1",r,5,"Pass")
                elif self.exp_result=="Fail" :
                    Login_status_List.append("Fail")
                    self.log.info("taking screenshot")
                    self.driver.save_screenshot("D:\\programming\\OrangeHrm\\ScreenShot\\test_orange_login_00"+str(r)+"_pass.png")
                    allure.attach(self.driver.get_screenshot_as_png(), name="test_orange_login_00" + str(r) + "_pass", attachment_type=AttachmentType.PNG)
                    self.log.info("click on menu button ")
                    self.lp.Click_menuButton()
                    self.log.info("click on logout button ")
                    self.lp.Click_logout()
                    # self.driver.close()
                    self.log.info("test case test_orange_login_002 is pass" )
                    self.log.info("write data in excel")
                    XLorg.WriteData(self.XlPath,"Sheet1",r,5,"Fail")
            elif self.lp.Login_Status()==False:

                if self.exp_result == "Pass":
                    Login_status_List.append("Fail")
                    XLorg.WriteData(self.XlPath,"Sheet1",r,5,"Fail")
                elif self.exp_result == "Fail":
                    Login_status_List.append("Pass")
                    XLorg.WriteData(self.XlPath,"Sheet1",r,5,"Pass")
                    self.log.info("taking screenshot")
                    self.driver.save_screenshot("D:\\programming\\OrangeHrm\\ScreenShot\\test_orange_login_00"+str(r)+"_pass.png")
                    allure.attach(self.driver.get_screenshot_as_png(), name="test_orange_login_00" + str(r) + "_pass", attachment_type=AttachmentType.PNG)

        # self.log.info("Login Status List " + str(Login_status_List))
        print(Login_status_List)
        if "Fail" not in Login_status_List:
            assert True
        else:
            assert False




