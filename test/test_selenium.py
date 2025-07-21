# Arquivo legado somente para testes, não tem qualquer influencia na LucIA

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

service = Service(executable_path="C:/devtools/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://127.0.0.1:5500/index.html")
driver.maximize_window()
sleep(2)
text_box = driver.find_element(by=By.ID, value='name')
text_box.send_keys('Renato')
sleep(2)
text_box = driver.find_element(by=By.ID, value='email')
text_box.send_keys('renato@techvista.com.br')
sleep(2)
text_box = driver.find_element(by=By.ID, value='address')
text_box.send_keys('Rua dos Gatos, n 888 - Nekolandia, NekoCity - SP')
sleep(2)

submit_button = driver.find_element(by=By.ID, value='btnSend')
submit_button.click()

sleep(60)