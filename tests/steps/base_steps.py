from behave import when ,then,given


@then(u'Verify that footer is displayed')
def step_impl(context):
    context.basepage.footer()
    
@when(u'User clicks on Dashboard button')
def step_impl(context):
    context.basepge.footer()
    
    
@when("Page title is {title}")
def step_impl(context, title):
    title_matched = context.homepage.match_title(title)
    assert title_matched
