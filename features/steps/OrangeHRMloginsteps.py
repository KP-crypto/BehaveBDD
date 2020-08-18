from behave import*
from selenium import webdriver

@given(u'I Launch Chrome Browser')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="C:/Users/Acer/Downloads/chromedriver_win32/chromedriver.exe")

@when(u'open Homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    context.driver.maximize_window()

@when(u'Enter username "{user}" and password "{pwd}"')
def step_impl(context,user,pwd):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(pwd)

@when(u'Click on Submit Button')
def step_impl(context):
    context.driver.find_element_by_id("btnLogin").click()

@then(u'I should see the Dashboard Page')
def step_impl(context):
    try:
        text=context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text
    except:
        context.driver.quit()
        assert False

    if text== "Dashboard":
        context.driver.quit()
        assert True



