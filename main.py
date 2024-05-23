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


def apply_filters(driver: webdriver.Chrome):
    openfilter_btn = driver.find_element(By.CLASS_NAME, "openfilter")
    openfilter_btn.click()
    time.sleep(0.2)

    ladentyp_checkboxes = driver.find_elements(By.XPATH, "//dd[@class='col-sm-11']//div[@class='checkbox']")

    print(f"No. of checkboxes in xpath://dd[@class='col-sm-11']:\n{len(ladentyp_checkboxes)}\n\n")
    pprint(ladentyp_checkboxes)

    time.sleep(0.1)
    ladentyp_checkboxes[4].click()  # Click 'Denner Satallit' checkbox
    time.sleep(0.1)

    ladentyp_checkboxes[5].click()  # Click 'Denner Partner' checkbox
    time.sleep(0.1)

    ladentyp_checkboxes[6].click()  # Click 'Denner Express' checkbox
    time.sleep(0.1)

    filiale_suchen_btn = driver.find_element(By.XPATH, "//div[@class='col-sm-5']//input[@class='btn btn-red' and @type='submit' and @value='Filiale suchen']")
    # filiale_suchen_btn.click() This didn't work properly, but execute_script should work
    driver.execute_script("arguments[0].click();", filiale_suchen_btn)

    breakpoint()


def run():
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

    driver.get("https://www.denner.ch/de/filialen/")

    apply_filters(driver)


run()
