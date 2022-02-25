import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException        
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
data = []
username = str(input("input username"))
hash = str(input("input hash"))
URL = f"https://tracker.gg/valorant/profile/riot/{username}%23{hash}/matches"


driver.get(URL)
driver.implicitly_wait(15) #allow some time to fully load, you may tweak accordingly


def check_exists_by_xpath(xpath):
    time.sleep(2)
    try:
        driver.find_element_by_xpath(xpath)
        print("Located and clicked 'Load More'...")
    except NoSuchElementException:
        print("Func NSE, proceed to retrieve data...")
        return False
    return True


loadMoreButton = driver.find_element_by_xpath('//span[@class="trn-gamereport-list__group-more"]')
while check_exists_by_xpath('//span[@class="trn-gamereport-list__group-more"]') == True:
    time.sleep(2)
    loadMoreButton.click()

if check_exists_by_xpath('//span[@class="trn-gamereport-list__group-more"]') == False:
    print('Retrieving data ...')
    time.sleep(2)
    matches = driver.find_elements_by_css_selector(r'[class="match__row"]')
    i = 1
    for match in matches:
        title = match.find_element_by_css_selector('span.match__name')
        title = title.text
        time_match = match.find_element_by_css_selector('span.match__time')
        time_match = time_match.text
        mode = match.find_element_by_css_selector('div.match__subtitle')
        mode = mode.text
        score_won = match.find_element_by_css_selector('span.score--won')
        score_won = score_won.text
        score_lost = match.find_element_by_css_selector('span.score--lost')
        score_lost = score_lost.text
        placement = match.find_element_by_css_selector('div.badge')
        placement = placement.text
        kda = match.find_element_by_css_selector('div.match__row-stats > div:nth-of-type(1) > div.value')
        kda = kda.text
        kd = match.find_element_by_css_selector('div.match__row-stats > div:nth-of-type(2) > div.value')
        kd = kd.text
        hs = match.find_element_by_css_selector('div.match__row-stats > div:nth-of-type(3) > div.value')
        hs = hs.text
        adr = match.find_element_by_css_selector('div.match__row-stats > div:nth-of-type(4) > div.value')
        adr = adr.text
        acs = match.find_element_by_css_selector('div.match__row-stats > div:nth-of-type(4) > div.value')
        acs = acs.text
        print('data append')

        kda = kda.split(sep="/")
        k = kda[0]
        d = kda[1]
        a = kda[2]

        match_json = {
            'id' : i,
            'map': title,
            'time': time_match, 
            'mode': mode,
            'score_won': score_won,
            'score_lost': score_lost, 
            'placement': placement,
            'kills' : k,
            'deaths' : d,
            'assists': a,
            'kd_percentage' : kd,
            'hs_percentage' : hs,
            'damage_per_round' : adr,
            'combat_score_total' : acs,
        }
        i = i + 1
        data.append(match_json)
time.sleep(5)


filename = 'data/game_data.json'
with open (filename, 'w') as outfile:
    json.dump(data, outfile)
driver.quit()
