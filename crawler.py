from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

URL = 'https://www.google.com/search?q=twitter+site:twitter.com&sca_esv=9f2ee88519d88278&sca_upv=1&sxsrf=ADLYWIIs5GRG8xo8P_UAeOek4N_FWo76wA:1716944212581&sa=X&ved=2ahUKEwjjjY_P07GGAxXjj4kEHU-5DNAQrAN6BAgIEAE&biw=1707&bih=898&dpr=1.5#ip=1'
URLS_TO_IGNORE = {'https://twitter.com/', 'https://twitter.com/i/flow/login', 'https://twitter.com/login'}
SCROLL_PAUSE_TIME = 0.5

CHROME_DRIVER_PATH = './drivers/chrome/chromedriver-win64/chromedriver.exe'
cService = webdriver.ChromeService(executable_path=CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service = cService)
driver.get(URL)

try:
    more_results_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "More results")]'))
    )

    # Get scroll height
    initial_height = driver.execute_script('return document.body.scrollHeight')

    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script('return document.body.scrollHeight')

        if new_height == initial_height:
            break
        initial_height = new_height
    
    for element in driver.find_elements(By.XPATH, '//div[@jscontroller]//span[@jscontroller]//a[@jsname]'):
        link = element.get_attribute('href')
        name = element.find_element(By.XPATH, './/h3').text
        if link not in URLS_TO_IGNORE:
            node = json.dumps({'name': name, 'link': link})
            print(node)

finally:
    driver.quit()

