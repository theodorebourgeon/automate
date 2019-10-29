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

class entBot():
    def __init__(self, email, pwd):
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
        self.email = email
        self.password = pwd

    def signIn(self):     
        self.browser.get('https://cas.utc.fr/cas/login?service=https%3A%2F%2Fwebapplis.utc.fr%2Fent%2F')
        usernameInput = self.browser.find_element_by_css_selector('#username')
        passwordInput = self.browser.find_element_by_css_selector('#password')
        usernameInput.send_keys("thbourge")
        passwordInput.send_keys("M1c2h4p3")
        passwordInput.send_keys(Keys.ENTER)
        try :
            nameText = WebDriverWait(self.browser, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#LeUser'))).text
            print("Logged in ...", nameText)
        except:
            print("Not logged in")
    
    def close(self):
        self.browser.close()
