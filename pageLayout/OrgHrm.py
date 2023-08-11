from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OrangeHRM:
    user_name_xpath = (By.XPATH,"//input[@placeholder='Username']")
    user_password_xpath = (By.XPATH,"//input[@placeholder='Password']")
    login_button_xpath = (By.XPATH,"//button[@type='submit']")
    menu_button_css = (By.CSS_SELECTOR,".oxd-icon.bi-caret-down-fill.oxd-userdropdown-icon")
    logout_button_xpath = (By.XPATH,"//a[normalize-space()='Logout']")
    title_logo_xpath = (By.XPATH,"//div[@class='orangehrm-login-logo']//img[@alt='orangehrm-logo']")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def OrgHRM_Url(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    def Eentr_username(self,name):
        self.wait.until(expected_conditions.visibility_of_element_located(self.user_name_xpath))
        self.driver.find_element(*OrangeHRM.user_name_xpath).send_keys(name)
    def Enter_password(self,password):
        self.driver.find_element(*OrangeHRM.user_password_xpath).send_keys(password)
    def Click_loginButton(self):
        self.driver.find_element(*OrangeHRM.login_button_xpath).click()
    def Click_menuButton(self):
        self.driver.find_element(*OrangeHRM.menu_button_css).click()
    def Click_logout(self):
        self.driver.find_element(*OrangeHRM.logout_button_xpath).click()
    def Login_Status(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(self.menu_button_css))

            self.driver.find_element(*OrangeHRM.menu_button_css)
            return True
        except:
            return False
    def take_screenshot(self):

        self.wait.until(expected_conditions.visibility_of_element_located(self.title_logo_xpath))


