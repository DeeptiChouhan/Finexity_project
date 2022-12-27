import time
from pages.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helper_utils import Helper

class ExclusivePage(BasePage):
    def __init__(self,context,):
       self.context=context
       self.helper=Helper(self.context)
       
    EXCLUSIVE_TAB=(By.XPATH,"//a[@href='/exclusive']")
    TOP_MENU=(By.XPATH,"//div[@class='desktop-display']/div")
    EXCLUSIVE_HEADER=(By.XPATH,"//div[contains(@class,'desktop-display')]//a[contains(@class,'new-link medium d-inline-block py-3')][normalize-space()='Exclusive']")
    MARKETPLACE_ON_EXCLUSIVE=(By.XPATH,"//li[@class='li-menu-item ']")
    PRODUCTS_ON_MARKETPLACE=(By.XPATH, "//div//h6")
    PAGE_CONTENT=(By.XPATH,"//html")
    MARKETPLACE_PRODUCT=(By.XPATH,"//section[@class='property-section small-container']")
    
    def click_on_exclusive_tab(self):
        self.context.browser.find_element(*self.EXCLUSIVE_TAB).click()
        time.sleep(3)
        
    def content_of_exclusive(self):
        self.context.browser.find_element(*self.PAGE_CONTENT).is_displayed()
          
    def menu_tab(self):
        self.context.browser.find_element(*self.TOP_MENU).is_displayed()
        assert True
    def check_exclusive_header(self):
        self.context.browser.find_element(*self.EXCLUSIVE_HEADER).is_displayed()
        assert True
        
    def marketplace_on_exclusive(self):
        self.context.browser.find_element(*self.MARKETPLACE_ON_EXCLUSIVE).click()
        time.sleep(3)
  
    def marketplace_product(self):
        self.context.browser.find_element(*self.MARKETPLACE_PRODUCT).is_displayed()

    
       
        
        
        