import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_carrefour_CSS_selector():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.carrefour.fr')
    time.sleep(4)

    accepter_cookies = driver.find_element(By.CSS_SELECTOR, '.banner-actions-container > button')
    accepter_cookies.click()
    time.sleep(2)

    barre_recherche = driver.find_element(By.CSS_SELECTOR, 'input[required]')
    barre_recherche.send_keys("1664")

    search_button = driver.find_element(By.CSS_SELECTOR, '[type=submit]')
    search_button.click()
    time.sleep(2)

    premiere_produit = driver.find_element(By.CSS_SELECTOR,'.product-grid-item:nth-child(1) .main-vertical--image')
    premiere_produit.click()
    time.sleep(2)

    acheter_button = driver.find_element(By.CSS_SELECTOR, '[aria-label=ACHETER]')
    acheter_button.click()
    time.sleep(2)

    drive = driver.find_element(By.CSS_SELECTOR, "div.push-services--pickers li:nth-child(1) label")
    delivery24 = driver.find_element(By.CSS_SELECTOR, "div.push-services--pickers li:nth-child(2) label")
    delivery1 = driver.find_element(By.CSS_SELECTOR, "div.push-services--pickers li:nth-child(3) label")

    assert drive.text == 'Drive\nRetrait gratuit en magasin'
    print('Selector "retrait en drive" is present')
    assert delivery24.text == 'Livraison\nVotre plein de course en 24h'
    print('Selector "livraison en 24h" is present')
    assert delivery1.text == 'Livraison 1h\nVos courses d’appoint en 1h'
    print('Selector "livraison en 1h" is present')

    driver.quit()

def test_carrefour_XPATH():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.carrefour.fr')
    time.sleep(2)
    accepter_cookies = driver.find_element(By.CSS_SELECTOR, '.banner-actions-container > button')
    accepter_cookies.click()
    time.sleep(2)
    barre_recherche = driver.find_element(By.XPATH, '//input[@role="combobox"]')
    barre_recherche.send_keys("1664" + Keys.ENTER)
    time.sleep(2)
    premiere_produit = driver.find_element(By.XPATH,'(//div[@class="main-vertical--image"])[1]')
    premiere_produit.click()
    time.sleep(2)
    acheter_button = driver.find_element(By.XPATH, '//button[@aria-label="ACHETER"]')
    acheter_button.click()
    driver.quit()


#def test_simon_css_correction():
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    # driver.get("https://www.carrefour.fr/%22")
    # time.sleep(2)
    # close_cookies = driver.find_element(By.CSS_SELECTOR, ".banner-actions-container > button")
    # close_cookies.click()
    # search_bar = driver.find_element(By.CSS_SELECTOR, "input[required]")
    # # possibilite utilisation [required]
    # search_bar.send_keys("1664")
    # search_button = driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
    # # possibilite utilisation [type=submit]
    # search_button.click()
    # first_result = driver.find_element(By.CSS_SELECTOR, ".product-grid-item:nth-child(1) .main-vertical--image")
    # first_result.click()
    # time.sleep(1)
    # buy_button = driver.find_element(By.CSS_SELECTOR, ".pdp-button-container")
    # # possibilite utilisation [aria-label='ACHETER'] : mais attention au changement de langue
    # buy_button.click()
    # time.sleep(2)
    # drive = driver.find_element(By.CSS_SELECTOR, "div.push-services--pickers > ul > li:nth-child(1) div.ds-body-text")
    # delivery24 = driver.find_element(By.CSS_SELECTOR, "div.push-services--pickers > ul > li:nth-child(2) div.ds-body-text")
    # delivery1 = driver.find_element(By.CSS_SELECTOR, "div.push-services--pickers > ul > li:nth-child(3) div.ds-body-text")
    # assert drive.text == 'Retrait gratuit en magasin'
    # print('Selector "retrait en drive" is present')
    # assert delivery24.text == 'Votre plein de course en 24h'
    # print('Selector "livraison en 24h" is present')
    # assert delivery1.text == 'Vos courses d’appoint en 1h'
    # print('Selector "livraison en 1h" is present')
    # # presence des 3 selectors
    # # time.sleep(2)
    # driver.quit()

def test_css_correction_03midi():
    driver = webdriver.Chrome()

    driver.maximize_window()
    driver.get("https://www.carrefour.fr/")

    wait = WebDriverWait(driver, 10)
    close_cookies_button = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#onetrust-accept-btn-handler")))
    close_cookies_button.click()

    search_bar = driver.find_element(By.CSS_SELECTOR, "input[required]")
    # possibilite utilisation [required]
    search_bar.send_keys("1664")
    search_button = driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
    # possibilite utilisation [type=submit]
    search_button.click()
    first_result = driver.find_element(By.CSS_SELECTOR, ".product-grid-item:nth-child(1) .main-vertical--image")
    first_result.click()

    buy_button = wait.until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".pdp-button-container")))
    # possibilite utilisation [aria-label='ACHETER'] : mais attention au changement de langue
    buy_button.click()

    retrait_en_magasin = wait.until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".push-services--pickers li:nth-child(1) label")))
    delivery24 = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(2) label")
    delivery1 = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(3) label")
    assert retrait_en_magasin.text == 'Drive\nRetrait gratuit en magasin'
    assert "Drive" in retrait_en_magasin.text
    assert delivery24.text == 'Livraison\nVotre plein de course en 24h'
    assert delivery1.text == 'Livraison 1h\nVos courses d’appoint en 1h'
    driver.quit()
