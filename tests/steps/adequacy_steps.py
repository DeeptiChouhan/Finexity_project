import time
from behave import when ,then,given,step
from selenium.webdriver.common.by import By
@when(u'User opens Account sidebar')
def step_impl(context):
    context.login.click_on_user_icon()

@when(u'User clicks on adequacy check button')
def step_impl(context):
    context.marketplace.adequacy_check_button()

@when(u'User clicks on Continue button for adequacy')
def step_impl(context):
    context.marketplace.continue_button()

@step("User selects {option} option")
def step_impl(context,option):
    context.marketplace.select_from_options(option)

@when(u'User clicks on Cancel Adequacy Check button')
def step_impl(context):
    context.marketplace.cancel_adequacy()

@then(u'Verify that I would like to provide information button is displayed on sidebar')
def step_impl(context):
   context.marketplace.check_information_is_dispalyed()


@step("User clicks on {element_name} button")
def step_impl(context, element_name):
    button = context.browser.find_element(By.XPATH,"//button[normalize-space()='I do not want to provide any information']")
    context.browser.execute_script("arguments[0].scrollIntoView();", button)
    context.browser.execute_script("arguments[0].click();", button)
    time.sleep(5)
    button = context.browser.find_element(By.XPATH,"//button[normalize-space()='I want to continue without an exam']")
    context.browser.execute_script("arguments[0].click();", button)
    

@then(u'Success message is displayed')
def step_impl(context):
    context.homepage.exitButton()

@then(u'Verify that user is redirected to dashboard page')
def step_impl(context):
    context.dashboard.dashboard_text()

@then(u'User waits for 10 sec')
def step_impl(context):
   time.sleep(10)


@then(u'Verify that adequacy tile is not displayed on dashboard')
def step_impl(context):
    context.marketplace.adequacy_check_button()