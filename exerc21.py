from multiprocessing.connection import wait
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Firefox()

def abrir ():
    driver.get('https://www.palcomp3.com.br/')
try:
    abrir()
except:
    print('erro ao iniciar')
wait = WebDriverWait
driver.find_element(By.XPATH,'//*[@id="js-startInputSearch"]').click()
driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/div[2]/ul/li[1]/div/a').click()
driver.find_element(By.XPATH,'/html/body/div/div[1]/div/section/header/div[3]/div[1]/div/button[1]').click()