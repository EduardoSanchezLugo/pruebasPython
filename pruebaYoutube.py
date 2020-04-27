import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class buscarYoutube(unittest.TestCase):


        def setUp(self):
                global driver
                driver = webdriver.Firefox()
                driver.get("https://www.youtube.com/")
                driver.implicitly_wait(20)


	
        def test1(self):

                

                Cancion = driver.find_element_by_name("search_query")
                if Cancion is not None:
                        Cancion.send_keys("infinity")

                

                Url = driver.find_element_by_id("search-icon-legacy")
                if Url is not None:
                        Url.click()
                        
             

                Reproducir = driver.find_element_by_link_text("dj tiesto - infinity")
                if Reproducir is not None:
                        Reproducir.click()

                        time.sleep(3)


       

		
        def test2(self):

                

                Nombre = driver.find_element_by_name("search_query")
                if Nombre is not None:
                        Nombre.send_keys("Creep cover ")

                

                Liga = driver.find_element_by_id("search-icon-legacy")
                if Liga is not None:
                        Liga.click()
                        
             

                Clic = driver.find_element_by_partial_link_text(" by Daniela Andrade")
                if Clic is not None:
                        Clic.click()

                        time.sleep(240)

        


        def tearDown(self):
            driver.quit()

if __name__ == '__main__':
	unittest.main()

