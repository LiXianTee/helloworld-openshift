from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
import pytest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



@allure.severity(allure.severity_level.NORMAL)
class TestHRM:
    @allure.severity(allure.severity_level.MINOR)
    def test_logo(self):
        self.driver = webdriver.Remote("http://localhost:4444/wd/hub", DesiredCapabilities.CHROME)
        #self.driver=webdriver.Chrome("./chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        status=self.driver.find_element_by_xpath("//*[@id='divLogo']/img").is_displayed()
        if status==True:
                assert True
        else:
                assert False
        self.driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    def test_listemployee(self):
        pytest.skip('Skipping test later I implement....')

    @allure.severity(allure.severity_level.CRITICAL)
    def test_Login(self):
        self.driver = webdriver.Remote("http://localhost:4444/wd/hub", DesiredCapabilities.CHROME)
        #self.driver=webdriver.Chrome("./chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        actual_title=self.driver.title

        if actual_title=="OrangeHRM123":
            self.driver.close()
            assert True
        
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="testLoginScreen",
                            attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False


