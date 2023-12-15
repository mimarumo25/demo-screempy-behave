from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class CustomDriver:

    def get_driver(self: str) -> webdriver:
        if self.lower() == "chrome":
            chrome_options = Options()
            # chrome_options.add_argument("--headless") #mode sin cabeza
            chrome_options.add_argument("--incognito")
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--allow-running-insecure-content --disable-popup-blocking")
            chrome_options.add_argument("--disable-infobars --test-type --disable-extensions --disable-translate")
            chrome_options.add_argument("--ignore-certificate-errors --no-sandbox --disable-download-notification")

            return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        elif self.lower() == "firefox":
            firefox_options = Options()
            # firefox_options.add_argument("--headless")
            firefox_options.add_argument("--start-maximized")

            return webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)
        elif self.lower() == "edge":
            edge_options = Options()
            # edge_options.add_argument("--headless")
            edge_options.add_argument("--start-maximized")

            return webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_options)
        else:
            raise ValueError(f"Unsupported: {self}")