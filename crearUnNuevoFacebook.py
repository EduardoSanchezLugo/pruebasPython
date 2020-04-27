import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select



class CrearCuentaFacebook(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("https://www.facebook.com/")
        driver.implicitly_wait(20)




    def test1 (self):

        
        Nombre = driver.find_element_by_name("firstname")
        if Nombre is not None:
            Nombre.send_keys("Rubi")
            time.sleep(3)

        Apellido = driver.find_element_by_name("lastname")
        if Apellido is not None:
            Apellido.send_keys("Zaragoza Sanchez")
            time.sleep(3)
            

        Correo = driver.find_element_by_name("reg_email__")
        if Correo is not None:
            Correo.send_keys("ale_fire666@hotmail.com")
            time.sleep(3)
            

        ConfirmarCorreo = driver.find_element_by_name("reg_email_confirmation__")
        if ConfirmarCorreo is not None:
            ConfirmarCorreo.send_keys("ale_fire666@hotmail.com")
            time.sleep(3)
            

        Contraseña = driver.find_element_by_name("reg_passwd__")
        if Contraseña is not None:
            Contraseña.send_keys("Abc$123")
            time.sleep(3)
            
        
        PorqueFecha = driver.find_element_by_id("birthday-help")
        if PorqueFecha is not None:
           acciones = ActionChains(driver)
           acciones.move_to_element(PorqueFecha).click().perform()
           time.sleep(8)
           

      


                                            

    def tearDown(self):
        driver.quit()



if __name__== '__main__':
    unittest.main()
