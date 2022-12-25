from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://localhost:8000/new-order")
nameC = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID,'name')))
nameC.send_keys("1")
code = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.NAME,'code')))
code.send_keys("1")
nameP = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.NAME,'name')))
nameP.send_keys("1")
quantity = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.NAME,'quantity')))
quantity.send_keys("20")
clickBtn =  WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID,'x')))
clickBtn.click()
