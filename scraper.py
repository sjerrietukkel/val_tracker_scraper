import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException        
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
data = []
URL = f"https://tracker.gg/valorant/profile/riot/sjonkie%23bluk/matches"


driver.get(URL)
driver.implicitly_wait(15) #allow some time to fully load, you may tweak accordingly

def get_text(text):
    text.text
    return text

def check_exists_by_xpath(xpath):
    time.sleep(2)
    try:
        driver.find_element_by_xpath(xpath)
        print(" func xpath")
    except NoSuchElementException:
        print("func NSE")
        return False
    return True


loadMoreButton = driver.find_element_by_xpath('//span[@class="trn-gamereport-list__group-more"]')
while check_exists_by_xpath('//span[@class="trn-gamereport-list__group-more"]') == True:
    # print('located')
    time.sleep(2)
    loadMoreButton.click()
    # print('clicked!')

if check_exists_by_xpath('//span[@class="trn-gamereport-list__group-more"]') == False:
    print('no more load button')
    time.sleep(2)
    matches = driver.find_elements_by_css_selector(r'[class="match__row"]')
    for match in matches:
        print('data append')
        print(match.text)
        match__name = match.find_elements_by_css_selector(r'[class="match__name"]')
        match__time = match.find_elements_by_css_selector(r'[class="match__time"]')
        match__subtitle = match.find_elements_by_css_selector(r'[class="match__subtile"]')
        score__won = match.find_elements_by_css_selector(r'[class="score__won"]')
        score_lost = match.find_elements_by_css_selector(r'[class="score_lost"]')
        badge = match.find_elements_by_css_selector(r'[class="badge"]')
        match__name = match__name.text
        match__time = match__time.text
        match__subtitle =  match__subtitle.text
        score__won = score__won.text
        score_lost = score_lost.text
        badge = badge.text
        match = {
            'map': match__name,
            'time': match__time, 
            'mode': match__subtitle,
            'score_won': score__won,
            'score_lost': score_lost, 
            'placement': badge,
        }
        data.append(match)
time.sleep(5)


filename = 'data/game_data.json'
with open (filename, 'w') as outfile:
    json.dump(data, outfile)
driver.quit()

# {
#     'map': match__name,
#     'time': match__time, 
#     'mode': match__subtitle,
#     'score_won': score__won,
#     'score_lost': score_lost, 
#     'placement': badge,
#     "kda": ,
#     'k/d': , 
#     'hs_perc': ,
#     'ADR': ,
#     'ACS': , 
# }