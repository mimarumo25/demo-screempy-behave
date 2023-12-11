from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class CustomDriver:
    @staticmethod
    def chrome() -> webdriver:
        chrome_options = Options()
        # chrome_options.add_argument("--headless") #mode sin cabeza
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--start-maximized")
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
