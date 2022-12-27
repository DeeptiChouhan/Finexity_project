import time
import unittest
from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from pages.investment_page import InvestmentPage
from utils.helper_utils import Helper
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
test = unittest.TestCase()
class Dashboard(BasePage, unittest.TestCase):
    
    def __init__(self,context):
       self.context=context
       self.helper=Helper(self.context)
 
    DASHBOARD_BUTTON=(By.XPATH,"//button[text()='Dashboard']")
    DASHBOARD_TEXT=(By.XPATH,"//h2[normalize-space()='Dashboard']")
    STATUS_TEXT=(By.XPATH,"//span[contains(@class,'investment-tag')]")
    DASHBOARD=(By.XPATH,"//a[contains(@href,'/dashboard')]")
    INVESTMENT_NAME=(By.XPATH,"//h6[normalize-space()='Green Tiny House Tim']")
    PRICE_PER_DIGITAL_SHARE=(By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/div/div[9]/div[1]/div[1]/div[2]/div[1]/div[2]/h6/span[2]')
    NUM_OF_DIGITAL_SHARE=(By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/div/div[9]/div[1]/div[1]/div[2]/div[1]/div[2]/h6')
    PENDING_ORDER_CONTENER=(By.XPATH,"//div[@class='flex flex-wrap pending-investments']/div")
    def click_on_dashbord_botton(self):
        self.helper.explicit_wait(self.DASHBOARD_BUTTON).click()
        
    def dashboard_text(self):
        self.context.browser.find_element(*self.DASHBOARD_TEXT).is_displayed()
            
    def is_investment_status_present(self,status_msg):
        status=self.helper.explicit_wait(self.STATUS_TEXT).is_displayed()
        assert status==True
        if status==True:
            status_msg=self.helper.explicit_wait(self.STATUS_TEXT).text
            print(status_msg)
            
    def navigate_on_dashboard(self):
        WebDriverWait(self.context.browser, 25).until(EC.element_to_be_clickable(self.DASHBOARD)).click()
    
    def verify_investment_tile_data(self, table_data):
        for row in table_data:
            field = row["FIELD"]
            value = row["VALUE"]
            if field == "Investment Name":
                actual_value = self.context.browser.find_element(*self.INVESTMENT_NAME).text
                print(actual_value)

            elif field == "Price per digital share":
                actual_value = self.context.browser.find_element(*self.PRICE_PER_DIGITAL_SHARE).text
                print(actual_value)
                
            elif field == "Number of digital shares":
                expected = self.context.browser.find_element(*self.NUM_OF_DIGITAL_SHARE).text
                actual_value=expected.split("digital")[0].strip()
                print(actual_value)               
        test.assertEqual(actual_value, value)
       
    def verify_investment_is_displayed(self):
        container=self.helper.explicit_wait(self.PENDING_ORDER_CONTENER).text
        invetment_product=self.helper.explicit_wait(InvestmentPage.INVESTMENT).text
        if invetment_product in container:
            assert False