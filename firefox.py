from selenium import webdriver
driver = webdriver.Firefox(executable_path='geckodriver')
driver.get("http://www.google.com")
driver.quit()
