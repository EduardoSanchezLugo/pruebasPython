import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class selectMetodos (unittest.TestCase):

	def setUp(self):
		global driver
		driver = webdriver.Firefox()
		driver.get("http://www.goodstartbooks.com/pruebas/")


	def test1(self):
		opcion = driver.find_element_by_xpath("//*[@id='noImportante']/td[2]")
		if opcion is not None:
			print("Texto", opcion.text)
		

	def test2(self):
		opcion2 = driver.find_element_by_id("importante")
		if opcion2 is not None:
			valorAtributo=opcion2.get_attribute("class")
			print("Clase", valorAtributo)
		


	
	def tearDown(self):
		driver.quit()

if __name__ == '__main__':
	unittest.main()