from selenium.webdriver.chrome import webdriver
from selenium import webdriver

class ProductPage:

    def __int__(self, driver: webdriver.Chrome):
        self.driver = driver

    def buy(self):

