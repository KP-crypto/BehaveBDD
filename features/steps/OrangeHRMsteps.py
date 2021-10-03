from behave import *
from selenium import webdriver
from webdriver-manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.option import Options

chrome_option = Options()
chrome_option.add_argument('--hedless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

@given(u'launch Chrome Browser')
def launchBrowser(context):
    context.driver=webdriver.Chrome(ChromeDriverManager().install(),options=chrome_option)

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


