import sys
import os
import pytest
from selenium import webdriver
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.config import BROWSER, HEADLESS

@pytest.fixture(scope="function")
def driver():
    if BROWSER == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        if HEADLESS:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(options=options)
    else:
        raise Exception("Unsupported browser!")

    yield driver

    driver.quit()
