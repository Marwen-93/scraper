
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


from time import sleep
import re
import pandas as pd

driver = webdriver.Firefox(executable_path="/home/marwen/Desktop/selenium/geckodriver")

link ='https://www.auto-plus.tn/voitures-d-occasion.html'
driver.get(link)
info_dict= {'prices':[],'car_names':[],'cv':[],'fuel':[],'trasmission':[]
    ,'date':[],'location':[],'type_seller':[],'km':[],'calender':[],'etat':[]}
nex = True
while nex:
	lists=['prices','car_names','cv','fuel','trasmission','date','location','type_seller','km','calender','etat']
	xpaths = ['//*[@id="lastadslistbox"]/div/div[3]/div[1]','//*[@id="lastadslistbox"]/div/div[3]/h2/a'
    ,'//*[@id="lastadslistbox"]/div/div[3]/ul/li[1]/span','//*[@id="lastadslistbox"]/div/div[3]/ul/li[2]/span'
    ,'//*[@id="lastadslistbox"]/div/div[3]/ul/li[3]/span','//*[@id="lastadslistbox"]/div/div[3]/div[2]/div[1]'
    ,'//*[@id="lastadslistbox"]/div/div[3]/div[2]/div[2]','//*[@id="lastadslistbox"]/div/div[3]/div[2]/div[3]'
    ,'//*[@id="lastadslistbox"]/div/div[3]/ul/li[4]/span','//*[@id="lastadslistbox"]/div/div[3]/ul/li[5]/span'
    ,'//*[@id="lastadslistbox"]/div/div[3]/ul/li[6]/span']
	
	driver.implicitly_wait(10)
	try:
		for liste, xpath in zip( lists,xpaths):
			for element in driver.find_elements(By.XPATH,xpath):
				info_dict[liste].append(element.text)
	except NoSuchElementException:
			element =-1
	try:
		driver.find_element(By.XPATH,"//*[contains(text(), 'Suiv ›')]").click()
		sleep(5)
	except (NoSuchElementException,ElementClickInterceptedException, ElementNotInteractableException):
			nex = False
df =  pd.DataFrame(info_dict)





print(df)
df.to_csv(r'/home/marwen/Desktop/selenium/voiture.csv')
driver.quit()