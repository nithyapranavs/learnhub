from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = r"/Users/np/Z_Folder/web-driver/geckodriver"

driver = webdriver.Firefox(executable_path=PATH)
driver.get("https://www.techwithtim.net")

link = driver.find_element(By.LINK_TEXT,"Python Programming")
link.click()
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT,"Beginner Python Tutorials"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,"sow-button-19310003"))
    )
    element.click()
finally:
    driver.quit()

'''note

driver.forward()
driver.back()
'''