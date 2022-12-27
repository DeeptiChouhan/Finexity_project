import json
from behave import *
from tests.pages.basepage import BasePage
    
@when(u'user select \'Green Tiny House Jan\' property from Investments tab')
def step_impl(context):
    context.investment.select_product_for_invesment()
    
@step("user select {product_name} property from Investments tab")
def step_impl(context,product_name):
    context.investment.select_other_product_for_investment(product_name)
    
@when(u'user click on Invest now button')
def step_impl(context):
    context.investment.clickOnInvestNow()
    
@when(u'user enter amount')
def step_impl(context):
    context.investment.enterYourInvestment()
  
@then(u'clicks on continue button')
def step_impl(context):
    context.basepage.click_on_continue()

@then(u'user clicks on start button')
def step_impl(context):
    context.investment.clickOnStart()

@when(u'user select payment method')
def step_impl(context):
    context.basepage.click_on_continue()

@then(u'user clicks on Costs and grants')
def step_impl(context):
    context.basepage.click_on_continue()

@then(u'User checks all tick boxes')
def step_impl(context):
    context.investment.acceptAlltermsAndCondition()

@then(u'User should be download that document')
def step_impl(context):
    context.investment.download_investment_doc()
    
@then(u'clicks on buy now on Overview page')
def step_impl(context):
    context.investment.clickOnBuyNow()
    
@then(u'user click on back to production page')
def step_impl(context):
    context.investment.back_to_product_page()

@step("User navigates to dashboard page")
def step_impl(context):
    context.dashboard.navigate_on_dashboard()
        
@step("Investment status is updated to {status} on user dashboard")
def step_impl(context,status):
    context.dashboard.is_investment_status_present(status)
    
@then(u'Verify data in investment tile on user dashboard')
def step_impl(context):
    table_data = context.table
    context.dashboard.verify_investment_tile_data(table_data)
           
@step('User closes investment sidebar')
def step_impl(context):
    context.basepage.click_on_cross_button()

@then(u'Aborted investment is not displayed on user dashboard')
def step_impl(context):  
   context.dashboard.verify_investment_is_displayed()

@step("Verify that {doc_name} investment document can be downloaded")
def step_impl(context, doc_name):
    context.investmentpage.download_investment_doc(doc_name)
