from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()



driver.get("http://localhost:8000/register")
email = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.NAME,'name')))
email.send_keys("mh")
email = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.NAME,'email')))
email.send_keys("mh@gmail.com")
password = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID,'password')))
password.send_keys("12345678")
password_confirmation = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID,'password_confirmation')))
password_confirmation.send_keys("12345678")
clickBtn =  WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID,'signup')))
clickBtn.click()
