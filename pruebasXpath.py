
import unittest
from selenium import webdriver


class FindByIdName(unittest.TestCase):

	def setUp(self):
		global driver
		driver = webdriver.Firefox()
		driver.get("http:www.goodstartbooks.com/pruebas")

	def testId(self):
		elementById = driver.find_element_by_xpath("//tr[@id='noImportante']") 
		#//*[@id="noImportante"] con el asterisco busca en todo el codigo.
		#//tr[@id="noImportante"] con tr solo busca en las lineas del codigo.
		if elementById is not None:
			print("El elemento se encontro con el atributo id=noImportante")

	def testName(self):
		elementByName = driver.find_element_by_class_name("rojo")
		if elementByName is not None:
			print("El elemento se encontro con el atributo class name = rojo")

	def tearDown(self):
		driver.quit()

if __name__ == '__main__':
	unittest.main()