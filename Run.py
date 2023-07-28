import Metodos
from selenium.webdriver.common.by import By
import time

driver = Metodos.iniciaChrome()
btnAdd = driver.find_element(By.XPATH, "//button[@id=\"addNewRecordButton\"]")
res = 0
while res == 0:
    btnAdd.click()
    btnSubmit = driver.find_element(By.XPATH, "//button[@id=\"submit\"]")
    if btnSubmit.is_enabled:
#VALIDA CP-01 Validar datos obligatorios al ingresar usuario
        btnSubmit.click()
        time.sleep(1)
        doc = "CP-01-Evidencia.png"
        driver.save_screenshot(doc)
#FIN VALIDA CP-01
        time.sleep(1)
#SE GENERA ARREGLO CON LOS ELEMENTOS WEB (TEXTFIELDS) QUEDANDO CON EL INDICE EN EL SIGUIENTE ORDEN
#textosWeb[1]= TEXT FIRSTNAME
#textosWeb[2]= TEXT LASTNAME
#textosWeb[3]= TEXT EMAIL
#textosWeb[4]= TEXT AGE
#textosWeb[5]= TEXT SALARY
#textosWeb[6]= TEXT DEPARTMENT
        textosWeb = Metodos.buscaTextos(driver)
#VALIDA CP-02 Validar formato Mail
        try:
                Metodos.CasoPrueba02(driver, textosWeb[3])
                print("Caso de Prueba 02 Aprobado")
        except Exception as e:
                # Si la espera alcanza el tiempo límite y el elemento no es visible, maneja la excepción aquí.
                print("Hubo un error al ejecutar el Caso de Prueba 02", e)
#FIN VALIDA CP-02
#VALIDA CP-03 Validar formato Age
        try:
                Metodos.CasoPrueba03(driver, textosWeb[4])
                print("Caso de Prueba 03 Aprobado")
        except Exception as e:
                # Si la espera alcanza el tiempo límite y el elemento no es visible, maneja la excepción aquí.
                print("Hubo un error al ejecutar el Caso de Prueba 03", e)
#FIN VALIDA CP-03
#VALIDA CP-04 Validar formato Salary
        try:
                Metodos.CasoPrueba04(driver, textosWeb[5])
                print("Caso de Prueba 04 Aprobado")
        except Exception as e:
                # Si la espera alcanza el tiempo límite y el elemento no es visible, maneja la excepción aquí.
                print("Hubo un error al ejecutar el Caso de Prueba 04", e)
#FIN VALIDA CP-04
#VALIDA CP-05 Ingresar Usuario Braulio
        try:
                Metodos.CasoPrueba05(driver,textosWeb[1], textosWeb[2], textosWeb[6],btnSubmit)
                print("Caso de Prueba 05 Aprobado")
        except Exception as e:
                # Si la espera alcanza el tiempo límite y el elemento no es visible, maneja la excepción aquí.
                print("Hubo un error al ejecutar el Caso de Prueba 05", e)
#FIN VALIDA CP-05
#VALIDA CP-06 Editar Department usuario Braulio
        try:
                Metodos.CasoPrueba06(driver)
                print("Caso de Prueba 06 Aprobado")
        except Exception as e:
                # Si la espera alcanza el tiempo límite y el elemento no es visible, maneja la excepción aquí.
                print("Hubo un error al ejecutar el Caso de Prueba 06", e)
#FIN VALIDA CP-06
#VALIDA CP-07 Editar Salary usuario Braulio
        try:
                Metodos.CasoPrueba07(driver)
                print("Caso de Prueba 07 Aprobado")
        except Exception as e:
                # Si la espera alcanza el tiempo límite y el elemento no es visible, maneja la excepción aquí.
                print("Hubo un error al ejecutar el Caso de Prueba 07   ", e)
#FIN VALIDA CP-07
#VALIDA CP-08 Buscar usuario Braulio y guardar datos
        try:
                Metodos.CasoPrueba08(driver)
                print("Caso de Prueba 08 Aprobado")
        except Exception as e:
                # Si la espera alcanza el tiempo límite y el elemento no es visible, maneja la excepción aquí.
                print("Hubo un error al ejecutar el Caso de Prueba 08   ", e)
#FIN VALIDA CP-0 8
#VALIDA CP-0 9 Eliminar Usuario Braulio
        try:
                Metodos.CasoPrueba09(driver)
                print("Caso de Prueba 09 Aprobado")
        except Exception as e:
                # Si la espera alcanza el tiempo límite y el elemento no es visible, maneja la excepción aquí.
                print("Hubo un error al ejecutar el Caso de Prueba 09   ", e)
#FIN VALIDA CP-0 9
#VALIDA CP-0 10 Confirmar eliminación UsuarioBraulio
        try:
                Metodos.CasoPrueba10(driver)
                print("Caso de Prueba 10 Aprobado")
        except Exception as e:
                # Si la espera alcanza el tiempo límite y el elemento no es visible, maneja la excepción aquí.
                print("Hubo un error al ejecutar el Caso de Prueba 10   ", e)
#FIN VALIDA CP-0 10

# Cierra el navegador después de la interacción
        driver.quit()


