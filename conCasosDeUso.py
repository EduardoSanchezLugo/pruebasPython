import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class prueba (unittest.TestCase):
    def setUp (self):
        global driver
        driver = webdriver.Firefox(executable_path='geckodriver')
        driver.get("https://www.google.com/")
        
    def test_case_1 (self):
        prueba = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div/div[1]/div/div[1]/input")
        if prueba is not None:
            prueba.send_keys("prueba")
            print("SE HA INGRESADO EL ELEMENTO")
            time.sleep(5)

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
    unittest.main()
