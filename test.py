from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time


# returns a web driver
def getDriver():
    ser = Service("./chromedriver.exe")
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)
    return driver

def login_report(driver):
    username_id = 'username'        # username element ID
    password_id = 'password-button' # password element ID
    signin_id = 'signin-button'     # signin buttons element ID
    username_prompt = 'admin'
    password_prompt = 'password'


    driver.get("http://localhost:4295")
    delay = 3 # seconds
    username_login_form = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, username_id)))
    username_login_form.send_keys(username_prompt)
    password_login_form = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, password_id)))
    password_login_form.send_keys(password_prompt)
    signin_button = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, password_id)))
    signin_button.send_keys(Keys.ENTER)

    time.sleep(10)

def main():
    driver = getDriver()
    login_report(driver)

if __name__ == "__main__":
    main()