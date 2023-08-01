from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/')

#find web element
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')

# click search button
driver.find_element(By.ID, 'nav-search-submit-button').click()

#setting our values for expected and actual results
expected_result = '"table"'  #need to have the quotation marks inside the string here
actual_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text


#checks that our expected and actual result match (test passed) - assert compares two values
assert expected_result == actual_result, f'Expected {expected_result} did not match {actual_result}' #adds a message in the pycharm console so that there is a custom/detailed descripton of what failed
print('Test case passed')

#close browser
driver.quit()