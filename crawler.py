from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper import scroll_to_bottom
import json

URL = 'https://www.google.com/search?q=twitter+site:twitter.com&sca_esv=9f2ee88519d88278&sca_upv=1&sxsrf=ADLYWIIs5GRG8xo8P_UAeOek4N_FWo76wA:1716944212581&sa=X&ved=2ahUKEwjjjY_P07GGAxXjj4kEHU-5DNAQrAN6BAgIEAE&biw=1707&bih=898&dpr=1.5#ip=1'
URLS_TO_IGNORE = {'https://twitter.com/', 'https://twitter.com/i/flow/login', 'https://twitter.com/login', 'https://twitter.com/settings/account'}

CHROME_DRIVER_PATH = './drivers/chrome/chromedriver-win64/chromedriver.exe'
cService = webdriver.ChromeService(executable_path=CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service = cService)
driver.get(URL)

try:
    more_results_button = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "More results")]'))
    )
    
    scroll_to_bottom(driver)

    nodes = []
    for element in driver.find_elements(By.XPATH, '//div[@jscontroller]//span[@jscontroller]//a[@jsname]'):
        link = element.get_attribute('href')
        name = element.find_element(By.XPATH, './/h3').text
        if link not in URLS_TO_IGNORE:
            node = {'name': name, 'link': link}
            nodes.append(node)

    with open('data.json', 'w') as file:
        file.write(json.dumps(nodes))

except:
    print('she broke yo')
finally:
    driver.quit()

