from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

PATH = r"/Users/np/Z_Folder/web-driver/geckodriver"

driver = webdriver.Firefox(executable_path=PATH)
driver.get("https://duckduckgo.com/")
print(driver.title)


search = driver.find_element(By.ID,"search_form_input_homepage")
print(search)
search.send_keys("it works")
search.send_keys(Keys.RETURN)


time.sleep(5)
driver.quit()

