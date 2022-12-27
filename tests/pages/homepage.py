import time
from pages.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from tests.utils.helper_utils import Helper
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
class HomePage(BasePage):
    def __init__(self,context):
        BasePage.__init__(self, context)
        self.title = "Open Banking Features | FINEXITY Business"
        self.context=context
        self.helper=Helper(self.context)
    
    TOP_MENU=(By.XPATH,"//div[@class='desktop-display']//div[@class='top-part bg-dark d-flex justify-between align-center ']")
    LOGO=(By.XPATH,"//header[@id='headerDashboard']/a//*[local-name()='svg']")
    PERSONAL=(By.XPATH,"//a[text()='Personal']")
    JOIN_NOW=(By.XPATH,"//div[@class='left-side']//button[1]")
    EXIT=(By.XPATH,"//a[contains(@class,'new-link medium flex align-center')]")
    REGISTER_NOW=(By.XPATH,"//button[normalize-space()='Register now']")
    MARKETPLACE=(By.XPATH,"//a[@href='/personal/marketplace']")
    MARKETPLACE_TAB=(By.XPATH,"//a[normalize-space()='Marketplace']")
    MARKETPLACE_TABS=(By.XPATH, "//div[@class='flex project-btn-container']/button")
    MARKETPLACE_PRODUCT=(By.XPATH,"//div//h6")
    DIGITAL_WEALTH=(By.XPATH,"//span[contains(text(),'Digital Wealth')]")
    DIGITAL_WEALTH_MENU=(By.XPATH,"//ul[@class='bottom-menu flex-row']/li[2]/div/div/ul/li")
    COMPANY= (By.XPATH,"//span[contains(text(),'Company')]")
    COMPANY_MENU=(By.XPATH,"//div[@class='inner-sub-menu']/ul/li")
    
    def verify_title(self):
        """Verifies that the hardcoded text appears in page title"""
        return self.match_title(self.title)
    
    def top_menu(self):
        self.context.browser.find_element(*self.TOP_MENU).is_displayed()
        assert True

    def click_on_logo(self):
        self.helper.explicit_wait(self.LOGO).click()

    def go_to_home_page(self):
        self.helper.explicit_wait(self.MARKETPLACE_TAB).click()
        time.sleep(5)

    def click_on_personal(self): 
        self.context.browser.find_element(*self.PERSONAL).click()
        time.sleep(2)
        
    def join_now(self):    
        self.context.browser.find_element(*self.JOIN_NOW).is_displayed()
        
    def exitButton(self):
        self.helper.explicit_wait(self.EXIT).click()
      
    def click_on_join_now_tab(self):  
        self.helper.explicit_wait(self.JOIN_NOW).click()
        self.exitButton()
        
    def click_on_register_now(self):
        self.helper.explicit_wait(self.REGISTER_NOW).click()
        self.exitButton()
        
        self.helper.explicit_wait(self.MARKETPLACE).click()
        
    def click_on_marketplace(self):
        self.helper.explicit_wait(self.MARKETPLACE).click()
        time.sleep(5)
        
    def marketpalce_tabs(self):     
        self.context.browser.find_element(*self.MARKETPLACE_TABS).is_displayed()
        
    def click_on_marketpalce_tabs(self):     
        self.helper.click_on_multiple_element(self.MARKETPLACE_TABS)
        
    def product_availibility_on_marketpalce(self):    
        self.context.browser.find_element(*self.MARKETPLACE_PRODUCT).is_displayed() 
           
    def check_marketpalce_product_details(self):
        self.click_on_marketplace()    
        self.helper.click_on_multiple_element(self.MARKETPLACE_PRODUCT)
    
    def hoverover_on_digital_wealth(self):
        self.helper.hoverover(self.DIGITAL_WEALTH)
    
    def check_digital_wealth_options(self):
        for element in WebDriverWait(self.context.browser, 25).until(
            EC.visibility_of_all_elements_located(self.DIGITAL_WEALTH_MENU)):
            print(element.text)
        [element for element in WebDriverWait(self.context.browser, 25).until(
            EC.visibility_of_all_elements_located(self.DIGITAL_WEALTH_MENU))]
        print(element.text)
        print(type(element))
        # print(elements)
        # for element in elements:
        #     element.click()
        #     print("clicked on " , element.text)
        #     self.hoverover_on_digital_wealth()
    
    def hoverover_on_company(self):
        self.helper.hoverover(self.COMPANY)
    
    def check_company_option(self):
        self.context.browser.find_element(By.XPATH,"//a[normalize-space()='About Us']").click()
        time.sleep(2)
        self.hoverover_on_company()
        time.sleep(2)
        self.context.browser.find_element(By.XPATH,"//a[normalize-space()='Our Team']").click()
        time.sleep(2)
        self.hoverover_on_company()
        time.sleep(2)
        self.context.browser.find_element(By.XPATH,"//a[normalize-space()='Newsroom']").click()
        time.sleep(2)
        self.hoverover_on_company()
        time.sleep(2)
        self.context.browser.find_element(By.XPATH,"//a[contains(@class,'new-link medium d-inline-block')][normalize-space()='Contact']").click()

    def click_button_by_text(
        self,
        text,
        wait_time=1,
        wait_before=0,
        scroll_to=True,
       
    ):

        if wait_before > 0:
            time.sleep(wait_before)
        loc=(By.XPATH, f"//button[contains(text(),'{text}')]")
      
        if scroll_to:
            element = self.context.browser.find_element(*loc)
            self.context.browser.execute_script("arguments[0].scrollIntoView()", element)

        for i in range(15):
            buttons = self.context.browser.find_elements(*loc)
            all_buttons_text = [ele.text for ele in buttons]
            valid_buttons = [ele for ele in buttons if text in ele.text]
            if len(valid_buttons) >= 1:
                break
            time.sleep(1)

        if len(valid_buttons) >= 1:
            valid_buttons[0].click()
        else:
            raise RuntimeError(
                f"No clickable buttons with text {text} found! Buttons available : {' '.join(all_buttons_text)}"
            )

        time.sleep(wait_time)
       