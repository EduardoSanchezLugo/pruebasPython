from selenium import  webdriver
driver = webdriver.Firefox()
driver.get("http://www.goodstartbooks.com/pruebas")

elemento = driver.find_element_by_id("noImportante")
if elemento is not None:
	print("El elemento fue encontrado")

elemento = driver.find_element_by_name("ultimo")
if elemento is not None:
	print("El elemento fue encontrado usando en atributo name")
	

driver.quit()
