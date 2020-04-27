import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class ElemenByIdName(unittest.TestCase):

	def setUp(self):
		global driver
		driver = webdriver.Firefox()
		driver.get("http://www.goodstartbooks.com/pruebas")



	def testId(self):
		elementById = driver.find_element(By.XPATH,"//*[@id='importante']")
		if  elementById is not None:
			print ("El elemento se encontro con tag_name h3")


	def tearDown(self):
		driver.quit()


if __name__ == '__main__':
	unittest.main()