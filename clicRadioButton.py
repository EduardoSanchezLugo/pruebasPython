import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class radioButton(unittest.TestCase):

	def setUp(self):
		global driver
		driver = webdriver.Firefox()
		driver.get("http:www.goodstartbooks.com/pruebas/")


	def test1(self):
		print("Radio buttons")
		Boton1 = driver.find_element_by_id("RadioGroup1_0")
		if Boton1 is not None:
			Boton1.click()
		time.sleep(5)

		Boton2 = driver.find_element_by_id("RadioGroup1_1")
		if Boton2 is not None:
			Boton2.click()
		time.sleep(5)



	def  test2(self):
		print("Checkboxes")
		Check1 = driver.find_element_by_id("CheckboxGroup1_0")
		if Check1 is not None:
			Check1.click()
		time.sleep(5)	


		Check2 = driver.find_element_by_id("CheckboxGroup1_1")
		if Check2 is not None:
			Check2.click()
		time.sleep(5)

	def tearDown(self):
		driver.quit()

if __name__ == '__main__':
	unittest.main()