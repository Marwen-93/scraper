
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
#driver.get('https://www.flashscore.fr/equipe/real-madrid/W8mj7MDD/resultats/')	
	# Open the link

#last_height=driver.execute_script("return document.body.scrollHeight")
# Use visible text on screen to load all games 
  
# Use visible text on screen to load all games
link ='https://www.flashscore.fr/equipe/real-madrid/W8mj7MDD/resultats/'


def scroll_down(l):
	driver.get(l)
	show_more = True
	while show_more:
		try:
			driver.implicitly_wait(10)
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			driver.find_element(By.XPATH,'//*[@class="event__more event__more--static"]').click()
			sleep(5)
			
	
			show_more = True
		except(NoSuchElementException,ElementClickInterceptedException, ElementNotInteractableException):
			show_more=False
	
	return driver


def get_stat(driver):
	live_table = driver.find_element_by_css_selector('#live-table')
	# make empty lists 
	date_time=[]
	home_team=[]
	away_team=[]
	home_team_score =[]
	away_team_score =[]
	first_half_score =[]


	# get  date and time
	games= live_table.find_elements(By.XPATH,'//*[@title="Cliquez pour les détails du match!"]/div[1]')
	for game in games:
		
		date_time.append(game.text)
	# get home team
	games= live_table.find_elements(By.XPATH,'//*[@title="Cliquez pour les détails du match!"]/div[2]')
	for game in games:
		
		home_team.append(game.text)

	# get away team
	games= live_table.find_elements(By.XPATH,'//*[@title="Cliquez pour les détails du match!"]/div[3]')
	for game in games:
		
		away_team.append(game.text)
	# get team home score
	games= live_table.find_elements(By.XPATH,'//*[@title="Cliquez pour les détails du match!"]/div[4]/span[1]')
	for game in games:
		
		home_team_score.append(game.text)
	# get team away score and team home score
	games= live_table.find_elements(By.XPATH,'//*[@title="Cliquez pour les détails du match!"]/div[4]')
	for game in games:
		
		home_team_score.append(game.text.split('\n')[0])
		away_team_score.append(game.text.split('\n')[2])

	# get first time score
	games= live_table.find_elements(By.XPATH,'//*[@title="Cliquez pour les détails du match!"]/div[5]')
	for game in games:
		
		first_half_score.append(game.text)






	df = pd.DataFrame(list(zip(date_time, home_team,away_team,home_team_score,away_team_score,first_half_score)),columns =['date_time', 'home_team','away_team','home_team_score','away_team_score','first_half_score'])

	return df
driver =scroll_down(link)
df = get_stat(driver)
print(df)
df.to_csv(r'/home/marwen/Desktop/selenium/flashscor.csv', index = False)

driver.quit()
	

