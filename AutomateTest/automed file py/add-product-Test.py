from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://localhost:8000/add-product")
code = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.NAME,'code')))
code.send_keys("123")
name = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.NAME,'name')))
name.send_keys("fdhfdh")
category = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.NAME,'category')))
category.send_keys("category")
stock = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.NAME,'stock')))
stock.send_keys("stock")
unit_price = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.NAME,'unit_price')))
unit_price.send_keys("20")
sale_price = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.NAME,'sale_price')))
sale_price.send_keys("10")
clickBtn =  WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID,'x')))
clickBtn.click()
