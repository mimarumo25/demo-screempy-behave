from screenpy_selenium import Target
from selenium.webdriver.common.by import By

THE_USERNAME_FIELD = Target.the("username field").located_by((By.ID,"LoginPanel0_Username"))
THE_PASSWORD_FIELD = Target.the("password field").located_by((By.ID,"LoginPanel0_Password"))
LOGIN_BUTTON = Target.the("login button").located_by((By.ID,"LoginPanel0_LoginButton"))
