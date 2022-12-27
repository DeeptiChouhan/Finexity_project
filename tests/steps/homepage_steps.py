
import time
from behave import *
@given(u'User is on Finexity website')
def step_impl(context):
    pass
@when(u'user clicks on logo')
def step_impl(context):
    context.homepage.click_on_logo()

@then(u'Verify top menu content')
def step_impl(context):
    context.homepage.top_menu()

@then(u'Verify that header is displayed')
def step_impl(context):
    context.basepage.header()

@when(u'Verify that footer is displayed')
def step_impl(context):
    context.basepage.footer()
    
@when(u'user click on personal tab')
def step_impl(context):
    context.homepage.click_on_personal()

@when(u'user click on join now botton on personal tab')
def step_impl(context):
    context.homepage.click_on_join_now_tab()
    
@when(u'user clicks on register now botton on personal tab')
def step_impl(context):
    context.homepage.click_on_register_now()
    
@when(u'user check that footer links')
def step_impl(context):
    context.basepage.ckeck_footer_links()
    
@when(u'user click on marketplace tab')
def step_impl(context):
    context.homepage.click_on_marketplace()

@when(u'user check marketplace cetagory tab')
def step_impl(context):
    context.homepage.marketpalce_tabs()

@when(u'user clicks on marketplace cetagory tab')
def step_impl(context):
    context.homepage.click_on_marketpalce_tabs()
    
@when(u'user check marketplace product')
def step_impl(context):
    context.homepage.product_availibility_on_marketpalce()
    
@when(u'user clicks on marketplace product details')
def step_impl(context):
    context.homepage.check_marketpalce_product_details()
    
@when(u'hoverover on digital wealth tab')
def step_impl(context):
    context.homepage.hoverover_on_digital_wealth()

@when(u'user click on digital wealth items')
def step_impl(context):
    context.homepage.check_digital_wealth_options()
    
@when(u'hoverover on company tab')
def step_impl(context):
    context.homepage.hoverover_on_company()

@when(u'user click on company items')
def step_impl(context):
    context.homepage.check_company_option()