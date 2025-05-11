from selenium import webdriver

def teste_login_page():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")
    assert "Login Page" in driver.title
    driver.quit()