from behave import *
from selenium import webdriver

@given(u'launch Chrome Browser')
def launchBrowser(context):
    context.driver=webdriver.Chrome(executable_path="C:/Users/Acer/Downloads/chromedriver_win32/chromedriver.exe")

@when(u'User is on HomePage')
def OpenHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    context.driver.maximize_window()

@then(u'OrangeHRM logo should be present')
def VerifyLogo(context):
    status=context.driver.find_element_by_xpath("//div[@id='divLogo']//img").is_displayed()
    assert status is True

@then(u'Close Browser')
def CloseBrowser(context):
    context.driver.quit()


