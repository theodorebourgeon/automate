from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import requests
from lxml import html
from bs4 import BeautifulSoup
import cfscrape


def isMyProxyEnoughFast(proxy):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Headless
    chrome_options.add_argument('--proxy-server=%s' % proxy)
    driver = webdriver.Chrome(
        ChromeDriverManager().install(), options=chrome_options)
    print('ip proxy : ', proxy.split(':')[0])
    print('port proxy : ', proxy.split(':')[1])
    driver.get('https://google.fr')
    try:
        selector = '#tsf > div:nth-child(2) > div > div > center > input:nth-child(1)'
        wait = WebDriverWait(driver, 1)
        check = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, selector))).getAttribute("aria-label")
        print('Fast Proxy : ', check)
        return True
    except:
        print('This proxy is too slow...')
        driver.close()
        return False


def isInFile(str, file):
    with open(file) as f:
        return str in f.read()


def get_proxies_hidemy():
    scraper = cfscrape.create_scraper()  # returns a CloudflareScraper instance
    page = scraper.get(
        'https://hidemy.name/en/proxy-list/?maxtime=800&type=hs&anon=34#list')
    soup = BeautifulSoup(page.content, 'html.parser')
    PROXIES = []
    for child in soup.find('tbody').children:
        result = []
        for td in child.children:
            result.append(td.text)
        proxy = result[0]+":"+result[1]
        if not isInFile(proxy, 'proxies.txt'):
            print("New IP, checking speed")
            if isMyProxyEnoughFast(proxy):
                PROXIES.append(proxy)
        else:
            print("Already there")
    if len(PROXIES) > 0:
        with open("proxies.txt", 'a') as file:
            for proxy in PROXIES:
                file.write(proxy + '\n')
    return


def get_proxies_selenium(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Headless
    driver = webdriver.Chrome(
        ChromeDriverManager().install(), options=chrome_options)
    driver.get(url)
    PROXIES = []
    selector_cells = 'tbody > tr'
    wait = WebDriverWait(driver, 30)
    proxies = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, selector_cells))).find_elements_by_css_selector('selector_cells')
    for p in proxies:
        result = p.text.split(" ")
        print(result)
        PROXIES.append(result[0]+":"+result[1])
    driver.close()
    return PROXIES
