from selenium import webdriver

PATH = r"/Users/np/Z_Folder/web-driver/geckodriver"

driver = webdriver.Firefox(executable_path=PATH)
driver.get("https://www.techwithtim.net")
print(driver.title)
driver.quit()

