from screenpy_selenium import Target
from selenium.webdriver.common.by import By

THE_DASHBOARD_TITLE = Target.the("Dashboard Title").located_by((By.XPATH, "//h1"))
BTN_ORGANIZATION = (Target.the("button organization").located_by((By.XPATH, "//i[@class='s-sidebar-icon fa fa-comments premium-feature']")))
BTN_BUSINESS_UNIT = (Target.the("button businessUnit").located_by((By.XPATH, "//i[@class='s-sidebar-icon fa fa-sitemap']")))
BTN_BUSINESS = (Target.the("button to select businessUnit").located_by((By.XPATH, "//div[@class='tool-button add-button icon-tool-button']")))
