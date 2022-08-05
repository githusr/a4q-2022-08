from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class HomePage:
    close_cookie_button_selector = (By.ID, "onetrust-accept-btn-handler")
    hamburger_button_selector = '#data-rayons'
    # print(hamburger_button_selector)
    epicerie_salee_selector = (".nav-item__menu-link [alt='Epicerie salée']")
    # print(epicerie_salee_selector)
    feculent_selector = "#data-menu-level-1_R12 > li:nth-child(7)"
    pates_selector = "#data-menu-level-2_R12F05 > li:nth-child(3)"

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.action = ActionChains(self.driver)

    # Close pop-up window
    def close_cookie(self):
        close_cookie_button = self.wait.until(
        expected_conditions.element_to_be_clickable(self.close_cookie_button_selector))
        close_cookie_button.click()
        self.wait.until(expected_conditions.invisibility_of_element_located(self.close_cookie_button_selector))

    # Click on hamburger button
    def open_menu(self):
        hamburger_button = self.driver.find_element(By.CSS_SELECTOR, self.hamburger_button_selector)
        hamburger_button.click()

    # Hover to epiciere salée
    def open_category_salee(self):
        epicerie_salee = self.wait.until(expected_conditions.element_to_be_clickable
                                         ((By.CSS_SELECTOR, self.epicerie_salee_selector)))
        self.action.move_to_element(epicerie_salee)
        self.action.perform()

    def open_subcategory_pates(self):
        feculent = self.wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.feculent_selector)))
        self.action.move_to_element(feculent)
        self.action.perform()

    # OpenProductCategoryPage(category)
    def open_product_pates_page(self):
        self.driver.find_element(By.CSS_SELECTOR, self.pates_selector).click()



