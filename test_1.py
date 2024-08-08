import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
driver_path = r"E:\Automation testing\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(driver_path)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(30)

###Test case ID:TC_PIM_01
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

username=driver.find_element(By.XPATH,'//input[@placeholder="Username"]')
username.send_keys("Admin")

forgotpassword=driver.find_element(By.XPATH,'//p[@class="oxd-text oxd-text--p orangehrm-login-forgot-header"]').click()

un=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/div/form/div[1]/div/div[2]/input')
un.send_keys("Admin")

resetpassword=driver.find_element(By.XPATH,'//button[@class="oxd-button oxd-button--large oxd-button--secondary orangehrm-forgot-password-button orangehrm-forgot-password-button--reset"]').click()
