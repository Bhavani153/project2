import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from io import StringIO
import sys
import time
driver_path = r"E:\Automation testing\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(driver_path)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(30)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

username=driver.find_element(By.XPATH,'//input[@placeholder="Username"]')
username.send_keys("Admin")

password=driver.find_element(By.XPATH,'//input[@placeholder="Password"]')
password.send_keys("admin123")

login=driver.find_element(By.XPATH,'//button[@type="submit"]')
login.click()

adminpage=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span').click()

###Test case ID:TC_PIM_02
####Title validation
def title_validation():
    given_title = "OrangeHRM"
    page_title = (driver.title)

    if given_title == page_title:
        print("Title validated sucessfully")
    else:
        print("Not a valid title")

title_validation()

####Header validation
def header_validation():
    given_h1= "User Management"
    given_h2= "Job"
    given_h3= "Organization"
    given_h4= "Qualifications"
    given_h5= "Nationalities"
    given_h6= "Corporate Banking"
    given_h7= "Configuration"
    adminpg_h1=(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span').text)
    adminpg_h2=(driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span').text)
    adminpg_h3=(driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]').text)
    adminpg_h4=(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span').text)
    adminpg_h5=(driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]/a').text)
    adminpg_h6=(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a').text)
    adminpg_h7=(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span').text)
    print("Header validation:")
    #H1
    if given_h1 == adminpg_h1: #and given_h2 == adminpg_h2 and given_h3 == adminpg_h3 and given_h4 == adminpg_h4 and given_h5 == adminpg_h5 and given_h6 == adminpg_h6 and given_h7 == adminpg_h7):
        print("h1-Header validated sucessfully")
    else:
        print("Not a valid Header")
    # H2
    if (given_h2 == adminpg_h2):
        print("h2-Header validated sucessfully")
    else:
        print("Not a valid Header")
    # H3
    if (given_h3 == adminpg_h3):
        print("h3-Header validated sucessfully")
    else:
        print("Not a valid Header")
    # H4
    if (given_h4 == adminpg_h4):
        print("h4-Header validated sucessfully")
    else:
        print("Not a valid Header")
    # H5
    if (given_h5 == adminpg_h5):
        print("h5-Header validated sucessfully")
    else:
        print("Not a valid Header")
    # H6
    if (given_h6 == adminpg_h6):
        print("h6-Header validated sucessfully")
    else:
        print("h6-Not a valid Header")
    # H7
    if (given_h7 == adminpg_h7):
        print("h7-Header validated sucessfully")
    else:
        print("Not a valid Header")
header_validation()

####Test case ID:TC_PIM_03
#####Menu validation
def Admin_pg_validation():
    m1 =(driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span').text)
    m2 =(driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').text)
    m3 =(driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a/span').text)
    m4 =(driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a/span').text)
    m5 =(driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span').text)
    m6 =(driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span').text)
    m7 =(driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span').text)
    m8 =(driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a/span').text)
    m9 =(driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a/span').text)
    m10=(driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a').text)
    m11=(driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a/span').text)
    m12=(driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a/span').text)

    # menu=print(m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12)

    given_menu=["Admin","PIM","Leave","Time","Recruitment","My Info","Performance","Dashboard","Directory","Maintenance","Buzz"]
#Menu_options:
    for i in given_menu:
        if m1 in i:
            print(i)
            print("m1:Menu Options Validated Sucessfully")
        if m2 in i:
            print(i)
            print("m2:Menu Options Validated Sucessfully")
        if m3 in i:
            print(i)
            print("m3:Menu Options Validated Sucessfully")
        if m4 in i:
            print(i)
            print("m4:Menu Options Validated Sucessfully")
        if m5 in i:
            print(i)
            print("m5:Menu Options Validated Sucessfully")
        if m6 in i:
            print(i)
            print("m6:Menu Options Validated Sucessfully")
        if m7 in i:
            print(i)
            print("m7:Menu Options Validated Sucessfully")
        if m8 in i:
            print(i)
            print("m8:Menu Options Validated Sucessfully")
        if m9 in i:
            print(i)
            print("m9:Menu Options Validated Sucessfully")
        if m10 in i:
            print(i)
            print("m10:Menu Options Validated Sucessfully")
        #m11 is "Claim", its not available in "i" so its not get printed in o/p"
        if m11 in i:
            print(i)
            print("m11:Menu Options Validated Sucessfully")
        if m12 in i:
            print(i)
            print("m12:Menu Options Validated Sucessfully")

Admin_pg_validation()