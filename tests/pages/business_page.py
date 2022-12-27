import time
from pages.basepage import BasePage
from selenium.webdriver.common.by import By
from utils.helper_utils import Helper
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions as cond
from selenium.common.exceptions import (ElementClickInterceptedException,
                                        NoSuchElementException,
                                        StaleElementReferenceException)
class Business(BasePage):
    
    BUSINESS_TAB=(By.XPATH,"//div[@class='desktop-display']//a[text()='Business']")  
    HOVER_ON_SOLUTION=(By.XPATH, "//span[contains(text(),'Solutions')]")
    HOVER_ON_DISCOVER=(By.XPATH, "//span[contains(text(),'Discover')]")
    HOVER_ON_COMPANY=(By.XPATH, "//span[contains(text(),'Company')]")
    SUB_MENU=(By.XPATH,"//li[@class='li-menu-item single has-children']/div/div/ul/li/a")

    OPEN_BANKING=(By.XPATH, "//a[normalize-space()='Open Banking for Tokenized Assets']")
    
    NAME_INPUT=(By.XPATH, "//input[@id='name']")
    EMAIL_INPUT=(By.XPATH," //input[@id='email']")
    PHONE_INPUT=(By.XPATH,"//input[@name='phone']")
    YOUR_MESSAGE=(By.XPATH,"//textarea[@placeholder=' Your message *']")
    REQUEST_INFORMATION=(By.XPATH,"//button[normalize-space()='Request information']")
    REQUEST_SUMBITTED =(By.XPATH,"//section[@class='article request-form-container pb-14']/div/div")
    def __init__(self,context):
       self.context=context
       self.helper=Helper(self.context)
       
    def click_on_business(self):
        self.helper.explicit_wait(self.BUSINESS_TAB).click()
        
    def hoverover_in_solution(self): 
        self.helper.hoverover(self.HOVER_ON_SOLUTION)
        
    def check_all_option_of_solution(self):
        self.helper.get_pop_value(self.SUB_MENU)
        
    def hoverover_in_discover(self):
        self.helper.hoverover(self.HOVER_ON_DISCOVER)
          
    def check_all_option_of_discover(self):
        self.helper.explicit_wait(self.SUB_MENU)
        
    def hoverover_in_company(self):
        self.helper.hoverover(self.HOVER_ON_COMPANY) 
         
    def check_all_option_of_company(self):
        self.helper.explicit_wait(self.SUB_MENU)

        Dropdown_Element = self.context.browser.find_element(*self.SUB_MENU).click()
        # Store the ActionChains class inside the actions variable
        actions = ActionChains(self.context.browser)
        # Click on the element using the click(on_element=)
        actions.click(on_element=Dropdown_Element)
        time.sleep(2)
        actions.perform()
        
    def click_on_open_banking(self):
        self.helper.explicit_wait(self.OPEN_BANKING).click()
        
    def request_information_now(self,text):
        self.helper.explicit_wait(self.NAME_INPUT).clear()
        self.helper.explicit_wait(self.NAME_INPUT).send_keys("Auto Test")
        email=self.helper.explicit_wait(self.EMAIL_INPUT).clear()
        self.helper.explicit_wait(self.EMAIL_INPUT).send_keys("testuser07@finexity.com")
        self.context.find_element(self.REQUEST_INFORMATION).is_displayed()
        phone=self.helper.explicit_wait(self.PHONE_INPUT).clear()
        self.helper.explicit_wait(self.PHONE_INPUT).send_keys("123456")
        self.helper.explicit_wait(self.REQUEST_INFORMATION).click()
        
    def request_was_sent(self):
        WebDriverWait(self.context.browser,30).until(cond.presence_of_element_located(self.REQUEST_SUMBITTED)).is_displayed()

    def scroll_to_element(self, locator, default_mode=True, index=0, dual_mode=False):
        driver = self.driver if not dual_mode else self.driver_admin
        element = driver.find_elements(*locator)[index]

        if default_mode == True:
            driver.execute_script("arguments[0].scrollIntoView()", element)
        else:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()

    def click(self,locator,wait=0.5,wait_before=0.2,dual_mode=False,index=0,scroll_to=False,scroll_by_action=False,):
        driver = self.driver if not dual_mode else self.driver_admin
        time.sleep(wait_before)

        if dual_mode and index == 0:
            self.wait_admin.until(cond.element_to_be_clickable(locator))
        else:
            if index == 0:
                self.wait.until(cond.element_to_be_clickable(locator))

        if scroll_to:
            element = driver.find_element(*locator)
            driver.execute_script("arguments[0].scrollIntoView()", element)

        if scroll_by_action:
            element = driver.find_element(*locator)
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()

        for retry_counter in range(5):
            try:
                driver.find_elements(*locator)[index].click()
                self.logger.info(f"Clicked : {locator[1]}")
                time.sleep(wait)
                return

            except StaleElementReferenceException:
                self.logger.info(
                    f"{StaleElementReferenceException} occurred when clicking {locator[1]}, retrying after refresh."
                )
                driver.refresh()
                time.sleep(2)

            except ElementClickInterceptedException:
                self.logger.info(
                    f"{ElementClickInterceptedException} occurred when clicking {locator[1]}, retrying in 2 sec."
                )
                time.sleep(2)