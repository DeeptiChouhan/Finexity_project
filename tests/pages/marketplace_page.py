from pages.basepage import BasePage
from tests.utils.helper_utils import Helper
from selenium.webdriver.common.by import By
class MarketPlacePage(BasePage):

    ASSET_MANAGER_LABEL=(By.XPATH,"//label[contains(@for,'assetManager')]")
    ADEQUACY_CONTAINER=(By.XPATH,"//div[contains(@class,'identity-block adequacy-block experience-block pointer border-radius bg-black')]")
    CANCEL_ADEQUACY_BUTTON=(By.XPATH,"//span[@class='skip-link']")
    INFORMATION = (By.XPATH,"//button[normalize-space()='I would like to provide information']")
    CONTINUE_BUTTON=(By.XPATH,"//button[normalize-space()='Continue']")

    def __init__(self,context):
       self.context=context
       self.helper=Helper(self.context)

    def select_from_options(self, option):
        option = option.lower()
        if option == "asset manager":
            self.context.browser.find_element(*self.ASSET_MANAGER_LABEL).click()

    def adequacy_check_button(self):
        if self.context.browser.find_element(*self.ADEQUACY_CONTAINER).is_displayed():
            assert True
            self.helper.explicit_wait(self.ADEQUACY_CONTAINER).click()
        else:
            pass
    def cancel_adequacy(self):
        button=self.helper.explicit_wait(self.CANCEL_ADEQUACY_BUTTON)
        self.context.browser.execute_script("arguments[0].click();", button)

    def check_information_is_dispalyed(self):
        self.helper.explicit_wait(self.INFORMATION).is_displayed()

    def continue_button(self):
        self.helper.explicit_wait(self.CONTINUE_BUTTON).click()