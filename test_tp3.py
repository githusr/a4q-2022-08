from selenium import webdriver
# from selenium.webdriver.chrome import webdriver
from HomePage import HomePage
from ProductCategoryPage import ProductCategoryPage
# from ProductPage import ProductPage

def test_page_object():
    driver = webdriver.Chrome()
    print("")
    print("############### TEST START ###############")
    print("Establish driver...done")
    driver.maximize_window()
    print("Maximise window...done")
    driver.get("https://www.carrefour.fr")
    print("Get website...done")
    home = HomePage(driver)
    print("Variable example (cookie close location): " + str(HomePage.close_cookie_button_selector))
    print("Call HomePage...establish variables...done")
    home.close_cookie()
    print("Accept cookies...done")
    home.open_menu()
    print("Open menu...done")
    home.open_category_salee()
    print("Go to epicerie salee on main menu...done")
    home.open_subcategory_pates()
    print("Go to subcategory menu...done")
    home.open_product_pates_page()
    print("Go to page pates...done")

    produit = ProductCategoryPage(driver)
    print("Call product category page, establish location variable...done")
    produit.open_product_page(3)
    print("Select the 4th product...done")

    print("A bientôt !...")
    driver.quit()
