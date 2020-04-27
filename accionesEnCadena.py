import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



class dropDownMenu(unittest.TestCase):

	def setUp(self):
		global driver
		driver = webdriver.Firefox()
		driver.get("http://www.goodstartbooks.com/pruebas/")
		# driver.implicitly_wait(15)

	def test1(self):
		botonMenu = driver.find_element_by_class_name("dropbtn")
		if botonMenu is not None:
			acciones = ActionChains(driver)
			acciones.move_to_element(botonMenu).perform()

		liga = driver.find_element_by_link_text("Link 1")
		if liga is not None:
			acciones.move_to_element(liga)
			acciones.click()
			acciones.perform()
		
                        time.sleep(3)


	def TearDown(self):
		driver.quit()

if __name__ == '__main__':
	unittest.main()
