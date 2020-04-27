import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClicAndSend (unittest.TestCase):

	def setUp (self):
		global driver
		driver = webdriver.Firefox()
		driver.get("http:www.goodstartbooks.com/pruebas/")


	def testClicAndSendKeys (self):
		Clic = driver.find_element(By.XPATH,"//a[contains(text(),'Pagina 2')]")
		if Clic is not None:
			Clic.click()

		nombre = driver.find_element_by_id("Segundo")
		if nombre is not None:
			nombre.send_keys("Eduardo")

		time.sleep(5)
		
	def tearDown(self):
		driver.quit()

if __name__ == '__main__':
	unittest.main()