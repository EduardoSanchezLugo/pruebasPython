import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class ByElementeIdName(unittest.TestCase):

	def setUp(self):
		global driver	
		driver = webdriver.Firefox()
		driver.get("http://www.goodstartbooks.com/pruebas")

	def testId(self):
		filas = driver.find_elements(By.XPATH,"//tr")
		if filas is not None:
			elementos = len(filas)
			print("Encontre:" , elementos)

	def testtag(self):
		filas = driver.find_elements_by_tag_name("tr")
		if filas is not None:
			elementos = len(filas)
			print("Encontre:" , elementos)


	def tearDown(self):
		driver.quit()

if __name__ == '__main__':
	unittest.main()		