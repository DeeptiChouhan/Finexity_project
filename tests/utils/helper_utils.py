import os
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
class Helper():
    def __init__(self, context):
        self.context = context
        
    def explicit_wait(self,locator_time):
        wait = WebDriverWait(self.context.browser,60).until(
            EC.visibility_of_all_elements_located(locator_time))
        for locator in wait:
            return locator
            
    def click_on_multiple_element(self,locator):
        elements = [element for element in WebDriverWait(self.context.browser, 60).until(
            EC.visibility_of_all_elements_located(locator))]
        print(elements)
        for element in elements:
            print(element)
            element.click()
            # print("clicked on " , element.text)
        
    def hoverover(self,hoverover_on_locator):
        wait = WebDriverWait(self.context.browser,60)
        hover_bttn = wait.until(EC.element_to_be_clickable(hoverover_on_locator))
        actionchains=ActionChains(self.context.browser)
        actionchains.move_to_element(hover_bttn).perform()
        time.sleep(1)    
    
    def get_pop_value(self,value):
        Dropdown_Element = WebDriverWait(self.context.browser, 60).until(EC.visibility_of_all_elements_located(value))
        for checkbox in Dropdown_Element:    
            actions = ActionChains(self.context.browser)
            actions.click(on_element=checkbox)
            actions.perform()              
            time.sleep(2)  

    def is_file_downloaded(download_path, file_name, match_length=2, format_only=None, logger=None):
        timer = 0
        while timer < 20:
            time.sleep(1)
            files = os.listdir(download_path)

            if len(files) == 0:
                timer += 1
                if logger:
                    logger.info(f"Downloaded file not found yet, waiting 1 sec.")

            for file in files:
                if format_only:
                    # check by file format only
                    exts = f".{format_only}"
                    if file.lower().endswith(exts):
                        return True
                    else:
                        timer += 1

                else:
                    # check by file name
                    if file_name[:match_length] in file:
                        return True
                    else:
                        timer += 1

        return False

    def wait(self):
        wait_time=WebDriverWait(self.context.browser, 60)
        return wait_time

        