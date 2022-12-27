import time
from pages.basepage import BasePage

from behave import given,when,then,step

from tests.configs.constants import USER_MAP

@when(u'user enters "{username}" and "{password}"')
def step_impl(context,username,password):
   context.browser.find_element(*BasePage.USERNAME_INPUT).send_keys(username)
   context.browser.find_element(*BasePage.USERPASS_INPUT).send_keys(password)
   
@step('User provides registration password as "{password}" on login page')
def step_impl(context,password):
    context.browser.find_element(*BasePage.USERPASS_INPUT).send_keys(password)
       
@step(u'User provides registration email as "{username}" on login page')
def step_impl(context,username):
    context.browser.find_element(*BasePage.USERNAME_INPUT).send_keys(username)
            
@when(u'User clicks on Login button')
def step_impl(context):
      context.login.click_on_login()
      time.sleep(1)
      
@then(u'Verify that dashboard is displayed')
def step_impl(context):
    context.dahshboard.click_on_dashbord_botton()
  
@when(u'User clicks the option to log out by clicking the user icon')
def step_impl(context):
      context.login.click_on_user_icon()
                  
@when(u'user click on logout option')
def step_impl(context):
      context.login.logout()
      time.sleep(5)

@step("User {username} is logged in")
def step_impl(context, username):
    user_details = USER_MAP.get(username)
    if user_details:
        email_id = user_details[0]
        password = user_details[1]
    else:
        pass    
    context.login.enter_cred(email_id,password)
    context.login.click_on_login()
      
@step('refresh browser')
def step_impl(context):
    context.browser.refresh()
    time.sleep(2)
    
@when(u'E-Mail address invalid message should be show')
def step_impl(context):
    context.login.invalid_msg_for_mail()
     
@when(u'Wrong email or password. should be show')
def step_impl(context):
    context.login.invalid_msg_for_pass()
    
@then(u'E-Mail address is required should be show')
def step_impl(context):
    context.login.blank_email()  
     
@then(u'Password is required should be show')
def step_impl(context):
    context.login.blank_pass()
