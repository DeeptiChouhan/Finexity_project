import time
from behave import *
from selenium.webdriver.common.by import By
from pages.business_page import Business

@when(u'user clicks on business tab of home page')
def step_impl(context):
    context.business.click_on_business()
    time.sleep(2)
@when(u'user hoverover on solution option')
def step_impl(context):
    context.business.hoverover_in_solution()

@when(u'solution pop should be open')
def step_impl(context):
    pass

@when(u'user clicks on any option')
def step_impl(context):
    context.business.check_all_option_of_solution()
    
@step("User is on {page_name} page")
def step_impl(context,page_name):
   pass

@when(u'page should be option')
def step_impl(context):
    pass

@when(u'user hoverover on discover option')
def step_impl(context):
    context.business.hoverover_in_discover()

@when(u'discover pop should be open')
def step_impl(context):
    pass

@when(u'user hoverover on company option')
def step_impl(context):
   context.business.hoverover_in_company()

@when(u'company pop should be open')
def step_impl(context):
    pass
    
@when(u'Verify top manu content')
def step_impl(context):
    pass

@when(u'Verify that header is displayed')
def step_impl(context):
    pass

@when(u'User clicks on Open Banking for Tokenized Assets button')
def step_impl(context):
    context.business.click_on_open_banking()
    
@step("User requests information with message {text}")
def step_impl(context, text):
    pass    
@then(u'Verify that message was sent successfully')
def step_impl(context):
    context.business.request_was_sent()
    
@when(u'User clicks on Open Banking for Tokenized Assets menu')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User clicks on Open Banking for Tokenized Assets menu')
    
