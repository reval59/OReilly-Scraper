from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from os import path, getcwd

class Scrapper:
    _driver = webdriver.Chrome(path.join(getcwd(), 'driver/chromedriver'))
    
    @staticmethod
    def get(url: str):
        return Scrapper._driver.get(url)
    
    @staticmethod
    def select_one(css_selector: str):
        return Scrapper._driver.find_element_by_css_selector(css_selector)
    
    @staticmethod
    def select_multiple(css_selector: str):
        return Scrapper._driver.find_elements_by_css_selector(css_selector)
    
    @staticmethod
    def driver():
        return Scrapper._driver
    
    @staticmethod
    def actions():
        return ActionChains(Scrapper.driver())