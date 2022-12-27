import time
from behave import *

from pages.test import LModel

@given('Collection of credentials')
def step_impl(context):
    model = getattr(context, "model", None)
    if not model:
      context.model = LModel()
   #iterate rows of table
    for r in context.table:
      context.model.usr_addition(r["username"], password=r["password"])
      
@then('user should be logged in')
def step_impl(context):
  time.sleep(5)
  pass