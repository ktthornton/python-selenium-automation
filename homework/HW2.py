from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep



#-----Locators-----
#Amazon logo - search by $x("//i[@class = 'a-icon a-icon-logo']")
#Email field - search by id="ap_email"
#Continue button - search by id="continue"
#Conditions of use link - search by $x("//a[text()='Conditions of Use']") or $x("//a[@href='https://www.amazon.com/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")
#Privacy Notice link - search by $x("//a[text()='Privacy Notice']") or $x("//a[@href='https://www.amazon.com/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']")
#Need help link - search by $x("//span[@class='a-expander-prompt']")
#Forgot your password link - search by id="auth-fpp-link-bottom"
#Other issues with Sign-In link - search by id="ap-other-signin-issues-link"
#Create your Amazon account button - search by id="createAccountSubmit"


#-----Sign In page test script-----

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

#open Amazon
driver.get('https://www.amazon.com/')

#click Orders
driver.find_element(By.ID, 'nav-orders').click()

#verify Sign In header/email input fields are visible
expected_result_header = 'Sign in'
actual_result_header = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text

expected_result_input_field = 'Email or mobile phone number'
actual_result_input_field = driver.find_element(By.XPATH, "//label[@for='ap_email']").text

assert expected_result_header == actual_result_header, f'Expected {expected_result_header} did not match {actual_result_header}'
print('Header test case passed')

assert expected_result_input_field == actual_result_input_field, f'Expected {expected_result_input_field} did not match {actual_result_input_field}'
print('Input field test case passed')

#close browser
driver.quit()
