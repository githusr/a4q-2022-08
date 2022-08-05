import time

from selenium import webdriver

def test_windows():
    driver = webdriver.Chrome()
    driver.get("https://python.org")
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://perl.org")
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1]) # 2eme onglet
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0]) # 1er onglet
    time.sleep(2)