from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.common.keys import Keys
import time


def login_report(driver):
    driver.get("http://localhost:4295")
    delay = 3 # seconds
    username_login_form = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'username')))

def main():
    #driver = webdriver.Chrome('./chromedriver.exe')
    ser = Service("./chromedriver.exe")
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)
    login_report(driver)

if __name__ == "__main__":
    main()