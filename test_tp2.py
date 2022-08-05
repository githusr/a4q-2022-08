import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

def test_exercice_aprem():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.carrefour.fr/")
    wait = WebDriverWait(driver, 10)
    close_cookies_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#onetrust-accept-btn-handler")))
    close_cookies_button.click()
    hamburger_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#data-rayons')))
    hamburger_button.click()
    epicerie_salee_menu = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".nav-item__menu-link ["
                                                                                        "alt='Epicerie salée']")))
    action = ActionChains(driver)
    action.move_to_element(epicerie_salee_menu).perform()
    pates_riz_etc = driver.find_element(By.CSS_SELECTOR, "#data-menu-level-1_R12 > li:nth-child(7)")
    action = ActionChains(driver)
    action.move_to_element(pates_riz_etc).perform()
    pates = driver.find_element(By.CSS_SELECTOR, "#data-menu-level-2_R12F05 > li:nth-child(3)")
    pates.click()
    openProduct(driver, 3)
    acheter_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label=ACHETER]")))
    acheter_button.click()
    drive_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name=PICKING_DRIVE-picker] + label")))
    drive_button.click()
    code_postal_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-cs-mask=true]")))
    code_postal_input.send_keys("75001")
    time.sleep(2)
    code_postal_input.send_keys(Keys.ENTER)
    time.sleep(1)
    liste_magasins = driver.find_elements(By.CSS_SELECTOR, "[aria-label*='Choisir le Retrait en magasin']")
    liste_magasins[1].click()

def openProduct(driver, index):
     liste_produits = driver.find_elements(By.CSS_SELECTOR, ".product-grid-item:not(.storetail) .product-card-image")
     liste_produits[index].click()




