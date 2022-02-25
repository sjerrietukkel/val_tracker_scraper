import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException        
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
data = []
URL = f"https://tracker.gg/valorant/profile/riot/sjonkie%23bluk/matches"
# LOAD_MORE_BUTTON_XPATH = '//*[@id="browse-itemsprimary"]/.trn-button' 


driver.get(URL)
driver.implicitly_wait(15) #allow some time to fully load, you may tweak accordingly

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
        # print(match.text)
        data.append(match.text)
time.sleep(5)


filename = 'data/game_data.json'
with open (filename, 'w') as outfile:
    json.dump(data, outfile)
driver.quit()