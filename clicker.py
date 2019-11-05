from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--headless")


class Clicker():
    def __init__(self, URL,  CSS_SELECTOR):
        # self.browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options) #Headless
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.url = URL
        self.css_selector = CSS_SELECTOR

    def click(self):
        self.browser.get(self.url)
        try:
            WebDriverWait(self.browser, 3).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, self.css_selector))).click()
            print("Clicked")
        except:
            raise ValueError
        time.sleep(10)
        self.browser.close()

    def clickLoop(self, number):
        for i in range(number):
            self.click()
