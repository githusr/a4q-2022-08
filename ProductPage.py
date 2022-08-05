from selenium.webdriver.chrome import webdriver

class ProductPage:

    def __int__(self, driver: webdriver.Chrome):
        self.driver = driver

    def buy(self):

