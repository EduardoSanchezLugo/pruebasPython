import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class IngresarAFacebook(unittest.TestCase):


    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://www.facebook.com/")
        driver.implicitly_wait(20)
        


    def test1 (self):
        Email = driver.find_element_by_name("email")
        if Email is not None:
            Email.send_keys("alefire666@aol.com")
            time.sleep(10)

        
        iniciarSesion = driver.find_element_by_xpath("//*[@id='u_0_2']")
        if iniciarSesion is not None:
            iniciarSesion.click()



    def tearDown(self):
        driver.quit()


if __name__ == '__main__':
    unittest.main()
