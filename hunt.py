import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
chrome_options = Options()  
#chrome_options.add_argument("--headless")

#THIS LINE BELOW IS VERY IMPORTANT. Refer to https://www.youtube.com/watch?v=Xjv1sY630Uc at 9:15 to set up for windows
driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"),options=chrome_options)
driver.get("https://www.hunter-ed.com/accounts/sign_in/")

#logs into hunter safety website  

try:
	driver.find_element_by_id("account-username").send_keys('YOUR USERNAME HERE')
	driver.find_element_by_id("account-password").send_keys('YOUR PASSWORD HERE')
	driver.find_element_by_class_name("btn-lg").click()
except:
	print('login failed. Exiting.')
	exit()

try:
	
	cont = WebDriverWait(driver, 8).until(
	EC.element_to_be_clickable((By.CLASS_NAME, "btn-success")))
	cont.click()

except:
	print('continue where you left off FAILED. Exiting')
	exit()

#click the next page  button whenever it appears, and fails intentionally if nothing pops up after 200 seconds
try:
	while(1):
		next_course = WebDriverWait(driver, 200).until(
		EC.element_to_be_clickable((By.CLASS_NAME, "btn-success")))
		next_course.click()
except:
	print('form already submitted, or landing page did not load')
	exit()

