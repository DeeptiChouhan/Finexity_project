import os
import time
from pages.basepage import BasePage
from pages.homepage import HomePage
from pages.login_page import Login
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.business_page import Business
from pages.login_page import Login
from pages.dashboard_page import Dashboard
from pages.exclusive_page import ExclusivePage
from pages.investment_page import InvestmentPage
from pages.registration import Registration
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from pages.marketplace_page import MarketPlacePage
     
def before_feature(context,feature):  
    login=Login(context) 
    home=HomePage(context)
    # context.browser = webdriver.Chrome(executable_path=r"driver\chromedriver.exe")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("download.default_directory=E:/New folder")
    prefs = {
            "download.default_directory" : "E:/New folder",
            "profile.default_content_setting_values.notifications" : 1
    }
    chrome_options.add_experimental_option('prefs', prefs)
    context.browser = webdriver.Chrome(chrome_options=chrome_options)
    TOKEN = open("./tests/configs/token.txt", "r")
    TOKEN_ACCESS = TOKEN.read()
    context.browser.get("https://test.finexity.com/"+TOKEN_ACCESS)
    context.browser.maximize_window()
    time.sleep(1)
    home.go_to_home_page()
    time.sleep(1)
    login.click_on_login_link()
    time.sleep(1)
    
def before_scenario(context,scenario):
   
    context.basepage=BasePage(context)
    context.publicpage=(context)
    context.homepage=HomePage(context)
    context.login=Login(context)
    context.exclusive=ExclusivePage(context)
    context.business=Business(context)
    context.investment=InvestmentPage(context)
    context.registration=Registration(context)
    context.dashboard=Dashboard(context)
    context.marketplace=MarketPlacePage(context)
    
def after_feature(context,feature):
    context.browser.quit() 
