from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://localhost:8000/add-customer")
name = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.NAME,'name')))
name.send_keys("name")
email = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.NAME,'email')))
email.send_keys("mh@gmail.com")
company = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.NAME,'company')))
company.send_keys("company")
address = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.NAME,'address')))
address.send_keys("address")
phone = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.NAME,'phone')))
phone.send_keys("20")
clickBtn =  WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID,'x')))
clickBtn.click()
