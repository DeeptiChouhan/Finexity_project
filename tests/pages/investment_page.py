import json
import os
import time
from pages.basepage import BasePage
from behave import given,when,then,step
from pages.login_page import Login
from tests.utils.helper_utils import Helper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
class InvestmentPage(BasePage):
      def __init__(self,context):
            self.context=context
            self.helper=Helper(self.context) 
                
      SELECT_PRODUCT=(By.XPATH,"//h6[normalize-space()='Green Tiny House Tim']")
      INVESTMENT_NOW=(By.XPATH,"//div[@class='desktop-display']//button[contains(@class,'action-btn mb-0 target-button')][normalize-space()='Invest now']")
      CONTINUE_INVESTMENT=(By.XPATH,"//button[normalize-space()='Continue this investment']")
      YOUR_INVESTMENT=(By.XPATH,"//input[@class='form-input text-input form-item investment-share-input']")
      CHECKBOXES = (By.XPATH,"//input[@type='checkbox'][@value='false']/following-sibling::div//div")
      BUY_NOW=(By.XPATH,"//button[@id='nextButton']")
      BACK_TO_PRODUCT=(By.XPATH,"//button[normalize-space()='Back to product page']")
      INVESTMENT=(By.XPATH,"//h6[normalize-space()='Solar-Anleihe Willofs II 2025']")
      INVESTMENT_SIDE_MODULE = (By.XPATH,"//div[@class='content-part']/div/div/div/div/div")
      INVESTMENT_DOCS = (By.XPATH,"//div[@class=' investment-process-container investment-process']//div[@class='document-icon']/i")
      DOWNLOAD=(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[2]/div[4]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[5]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/i[1]")
      def select_product_for_invesment(self):        
            self.helper.explicit_wait(self.SELECT_PRODUCT).click()
            
      def select_other_product_for_investment(self,product_name=None):
            self.helper.explicit_wait(self.INVESTMENT).click()
            return product_name
      
      def clickOnInvestNow(self):
            self.helper.explicit_wait(self.INVESTMENT_NOW).click()
        
      def enterYourInvestment(self):           
            self.helper.explicit_wait(self.YOUR_INVESTMENT).send_keys("500")
      
      def acceptAlltermsAndCondition(self):
            for i in range(20):
                  check_boxes = self.context.browser.find_elements(*self.CHECKBOXES)
                  if len(check_boxes) == 0:           
                        break
                  try:
                        for el in check_boxes:
                              self.context.browser.execute_script("arguments[0].scrollIntoView();", el)
                              self.context.browser.execute_script("arguments[0].click();", el)
                              self.context.browser.implicitly_wait(1)
                  except BaseException as ex:
                        pass      
            self.context.browser.implicitly_wait(20)
      
      def back_to_product_page(self):
            WebDriverWait(self.context.browser, 20).until(EC.element_to_be_clickable(self.BACK_TO_PRODUCT)).click()     
            
      def clickOnStart(self):
            WebDriverWait(self.context.browser, 20).until(EC.element_to_be_clickable(BasePage.CONTINUE)).click()
      
      def clickOnBuyNow(self):
            Dropdown_Element = self.context.browser.find_elements(*self.BUY_NOW)
            print(len(Dropdown_Element))
            print(Dropdown_Element)
            for checkbox in Dropdown_Element:    
                  actions = ActionChains(self.context.browser)
                  actions.click(on_element=checkbox)
                  time.sleep(2)
                  actions.perform()
      
      def download_investment_doc(self):
            check_boxes = self.context.browser.find_elements(*self.INVESTMENT_DOCS)
            for el in check_boxes:
                  self.context.browser.execute_script("arguments[0].scrollIntoView();", el)
                  self.context.browser.execute_script("arguments[0].click();", el)
                  self.context.browser.implicitly_wait(1)
                  time.sleep(5)
                       
            # self.context.browser.implicitly_wait(20)
            # button = self.context.browser.find_element(*self.INVESTMENT_DOCS)
            # for doc in button:
            #       self.context.browser.execute_script("arguments[0].click();", doc)
            #       time.sleep(5)
            # self.helper.click_on_multiple_element(self.INVESTMENT_DOCS)
            # time.sleep(5)
            # Document_download = self.context.browser.find_elements(*self.INVESTMENT_DOCS)
            # for doc in Document_download:    
            #       actions = ActionChains(self.context.browser)
            #       actions.click(on_element=doc)
            #       time.sleep(2)
            #       actions.perform()
                        
            # button = self.context.browser.find_element(*self.DOWNLOAD)
            # self.context.browser.implicitly_wait(5)
            # ActionChains(self.context.browser).move_to_element(button).click(button).perform()
            # time.sleep(5)
            # self.context.browser.implicitly_wait(5)
            # button = [self.context.browser.find_element(*self.INVESTMENT_DOCS)]
            # print(button)
            # # module=[self.context.browser.find_elements(*self.INVESTMENT_SIDE_MODULE)]
            # # print(module)
            # for doc in button:
            #       self.context.browser.implicitly_wait(5)
            #       ActionChains(self.context.browser).move_to_element(doc).click(doc).perform()
            #       time.sleep(5)
            #       self.context.browser.implicitly_wait(5)