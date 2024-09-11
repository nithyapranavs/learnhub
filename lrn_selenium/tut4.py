from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

PATH = r"/Users/np/Z_Folder/web-driver/geckodriver"

driver = webdriver.Firefox(executable_path=PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID,"langSelect-EN"))
)
element.click()


driver.implicitly_wait(5)

cookie = driver.find_element(By.ID,"bigCookie")
cookie_count = driver.find_element(By.ID,"cookies")
items = [driver.find_element(By.ID,"productPrice" + str(i)) for i in range(1,-1,-1)]

actions = ActionChains(driver)


for i in range(5000):
    actions.click(cookie)
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()