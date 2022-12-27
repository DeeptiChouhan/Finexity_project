from behave import *
@given(u'User is on Finexity Homepage')
def step_impl(context):
   pass

@when(u'user clicks on exclusive tab')
def step_impl(context):
    context.exclusive.click_on_exclusive_tab()


@when(u'Verify top menu content')
def step_impl(context):
    context.exclusive.menu_tab()


@when(u'Verify header of exclusive')
def step_impl(context):
    context.exclusive.check_exclusive_header()


@given(u'exclusive page should be open')
def step_impl(context):
    context.exclusive.content_of_exclusive()


@when(u'clicks on marketplace tab')
def step_impl(context):
   context.exclusive.marketplace_on_exclusive()

@when(u'marketplace page open with product')
def step_impl(context):
  context.exclusive.marketplace_product()
    