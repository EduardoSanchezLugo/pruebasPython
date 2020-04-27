import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class atributoTexto(unittest.TestCase):

	def setUp(self):
		global driver
		driver = webdriver.Firefox()
		driver.get("http://www.goodstartbooks.com/pruebas/")


	def test1 (self):
		ingredientes = driver.find_element_by_name("ingrediente")
		if ingredientes is not None:
			ingredienteSel = Select(ingredientes)
			ingredienteSel.select_by_value("cebolla")

		time.sleep(5)


	def test2 (self):
		frutas = driver.find_element_by_name("Select1")
		if frutas is not None:
			frutasSel= Select(frutas)
			frutasSel.selct_by_index(1)
			frutasSel.select_by_visible_text("Sandia")

		time.sleep(5)

	def TearDown(self):
		quit()

if __name__ == '__main__':
	unittest.main()