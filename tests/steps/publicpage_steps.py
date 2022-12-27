from behave import when,given
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'When User visit on finexity website')
def step_impl(context):
    pass

@when(u'user clicks on personal tab')
def step_impl(context):
    context.homepage.click_on_logo()
    

@when(u'clicks on register now')
def step_impl(context):
    context.publicpage.click_on_join_now()
    

@when(u'clicks one by one on footer "{Links}"')
def step_impl(context,Links):
    context.publicpage.check_footer_links()
    print(Links)
    
    

