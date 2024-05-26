import os, time
import datetime
from pprint import pprint
from selenium.webdriver.remote.webelement import WebElement
import time
import pandas as pd
import chromedriver_autoinstaller
import os
import warnings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup

########################

warnings.simplefilter(action='ignore', category=FutureWarning)
chromedriver_autoinstaller.install()
service = Service()
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
# options.add_argument("--headless")  # hide GUI
# options.add_argument("--window-size=1920,1080")  # set window size to native GUI size
options.add_argument("start-maximized")  # ensure window is full-screen
# options.add_experimental_option("prefs",{"profile.managed_default_content_settings.images": 2})  # Load without images
# options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-dev-shm-usage")

# caps = DesiredCapabilities().CHROME
# caps["pageLoadStrategy"] = "none"  # Do not wait for full page load

driver = webdriver.Chrome(service=service, options=options)


def apply_filters():
    print("Applying filters...")
    openfilter_btn = driver.find_element(By.CLASS_NAME, "openfilter")
    print("Clicking openfilter button")
    openfilter_btn.click()
    time.sleep(0.2)

    ladentyp_checkboxes = driver.find_elements(By.XPATH, "//dd[@class='col-sm-11']//div[@class='checkbox']")

    print(f"No. of Ladentyp checkboxes in xpath://dd[@class='col-sm-11']:\n{len(ladentyp_checkboxes)}")

    time.sleep(0.1)
    print("Clicking 'Denner Satallit' checkbox")
    ladentyp_checkboxes[4].click()  # Click 'Denner Satallit' checkbox
    time.sleep(0.1)

    print("Clicking 'Denner Partner' checkbox")
    ladentyp_checkboxes[5].click()  # Click 'Denner Partner' checkbox
    time.sleep(0.1)

    print("Clicking 'Denner Express' checkbox")
    ladentyp_checkboxes[6].click()  # Click 'Denner Express' checkbox
    time.sleep(0.1)

    filiale_suchen_btn = driver.find_element(By.XPATH,
                                             "//div[@class='col-sm-5']//input[@class='btn btn-red' and @type='submit' and @value='Filiale suchen']")
    # filiale_suchen_btn.click() This didn't work properly, but execute_script should work
    print("Clicking 'Filiale suchen' button")
    driver.execute_script("arguments[0].click();", filiale_suchen_btn)


def expand_list():
    storeitems = driver.find_elements(By.CLASS_NAME, "storeitem")
    print(f"Expanding list by clicking 'Zeig mehr' ({len(storeitems)}/360)")
    # breakpoint()

    if len(storeitems) < 360:
        # print(len(storeitems))
        waytrigger_btn = driver.find_element(By.ID, "waytrigger")
        driver.execute_script("arguments[0].click();", waytrigger_btn)
        time.sleep(1.25)  # less than 1.25s pause breaks it
        expand_list()
    else:
        print("storeitems length has reached 360. Ready to scrape all values.")
        return storeitems


def scrape_values(storeitems):
    # full_address_div = sto
    pass


def run():
    driver.get("https://www.denner.ch/de/filialen/")

    apply_filters()
    time.sleep(2)

    storeitems = expand_list()

    breakpoint()

    scrape_values(storeitems)


run()
