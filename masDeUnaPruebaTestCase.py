import unittest
from selenium import webdriver

class FindByIdName(unittest.TestCase):

	def setUp(self):
		global driver
		driver = webdriver.Firefox()
		driver.get("http://www.goodstartbooks.com/pruebas")

	def testId(self):
		elemento= driver.find_element_by_id("noImportante")
		if elemento is not None:
			print ("El elemento se encontro con el atributo id")


	def testName(self):
		elemento= driver.find_element_by_name("ultimo")
		if elemento is not None:
			print ("El elemento se encontro con el atributo name")

	def tearDown(self):
		driver.quit()

if __name__ == '__main__':
	unittest.main()