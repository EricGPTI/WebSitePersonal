from selenium import webdriver


driver = webdriver.Firefox()
home = 'http://127.0.0.1:8000'


def access_home_page_test():
    driver.get(home)