from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# serv_obj=Service("C:\\Users\\Admin\\Downloads\\chromedriver_win32 (5)\\chromedriver.exe")
driver=webdriver.Chrome()
# driver=webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.NAME,"username").clear()
driver.find_element(By.NAME,"username").send_keys("admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
act_title=driver.title
exp_title="OrangeHRM"
print(driver.title)

if act_title==exp_title:
    print("login test Pass")
else:
    print("login test Failed")
