import time
from behave import *
from pages.basepage import BasePage
from pages.registration import Registration
from pages.login_page import Login

@when(u'User clicks on registration link')
def step_impl(context):
    context.registration.clickOnRegistrationLink()
    
@when(u'User is on registration page')
def step_impl(context):
    context.registration.match_registration_page_content()
    
@step('User provides registration email as "{username}" on registration page')
def step_impl(context,username):
    context.browser.find_element(*Registration.EMAIL_INPUT).send_keys(username)
    
@step('User provides registration password as "{password}" on registration page')
def step_impl(context,password):
    context.browser.find_element(*Registration.PASSWORD_INPUT).send_keys(password)

@when(u'User clicks on Create Account button')
def step_impl(context):
    context.registration.click_on_create_account()

@when(u'User clicks on Continue button')
def step_impl(context):
   context.basepage.click_on_continue()
   
@then(u'Verify that new user registration was successful')
def step_impl(context):
    context.registration.registerSuccessful()

@when(u'User clicks on Exit Registration button')
def step_impl(context):
    context.homepage.exitButton()

@when(u'User clicks on Login link')
def step_impl(context):
    context.login.click_on_login_link()
    
@when(u'User provides registration mobile_number as "999999"')
def step_impl(context):
    context.registration.enter_mobile()

@when(u'User clicks on Continue button with 1 error handled')
def step_impl(context):
    context.browser.find_element(*Registration.EMAIL_INPUT).click()

@then(u'Verify blank password error message "{message}"')
def step_impl(context,message):
    context.browser.find_element(*Login.BLANK_PASS_INPUT).send_keys(message)
    context.login.blank_pass()

@then(u'Verify invalid error message "{message}"')
def step_impl(context,message):
    context.browser.find_element(*Login.INVAILID_EMAIL).send_keys(message)
    
@when(u'User tries to register without entering the password then')
def step_impl(context):
    context.browser.find_element(*Registration.PASSWORD_INPUT).click()
    context.browser.find_element(*Registration.EMAIL_INPUT).click()
    
@when(u'user enters "{username}" and "{password}" for registration')
def step_impl(context,username,password):  
    context.browser.find_element(*BasePage.USERNAME_INPUT).send_keys(username)
    context.browser.find_element(*BasePage.USERPASS_INPUT).send_keys(password)
     
@then(u'Verify error message E-Mail address invalid')
def step_impl(context):
    context.login.invalid_msg_for_mail()
    
@then(u'User provides registration mobile_number as "{mobile_number}"')
def step_impl(context,mobile_number):
   context.browser.find_element(*Registration.EMAIL_INPUT).send_keys(mobile_number)

@then(u'Verify error message Invalid mobile number')
def step_impl(context):
    context.login.invalid_msg_for_mobile()

@then(u'Verify that user is redirected to User-onboarding page')
def step_impl(context):
    pass
@when(u'User clicks on Continue button on Welcome page')
def step_impl(context):
   context.basepage.click_on_continue()
   pass
   
@when(u'User clicks on Skip button on complete your personal data page')
def step_impl(context):
    context.registration.skip()
    pass

@when(u'User clicks on Skip button on Your Interests')
def step_impl(context):
    context.registration.skip()
    pass
@step('User enters mobile number as "{phone_number}"')
def step_impl(context,phone_number):
    context.browser.find_element(*Login.PHONE_NO_INPUT).sned_keys(phone_number)
   
    
@when(u'User clicks on Request code button with wait of 5 sec')
def step_impl(context):
    context.registration.request_code()
    time.sleep(5)
   
@when(u'User enters TAN as 999999')
def step_impl(context):
    context.registration.otp_code()
    
@when(u'User waits for 10 sec')
def step_impl(context):
    time.sleep(10)
    
@when(u'User checks all tick boxes')
def step_impl(context):
    context.registration.tick_on_check_boxes()

@when(u'User clicks on Continue button on Conditions page')
def step_impl(context):
   context.basepage.click_on_continue()

@when(u'User clicks on To Dashboard button on Congratulations page')
def step_impl(context):
    context.basepage.click_on_continue()

@when(u'Verify that user is redirected to Dashboard page')
def step_impl(context):
    context.dashboard.dashboard_text()
       
@when(u'User provides registration mobile_number as "{mobile_number}"')
def step_impl(context,mobile_number):
    context.browser.find_element(*Registration.EMAIL_INPUT).send_keys(mobile_number)



