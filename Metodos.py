from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time



def iniciaChrome():
    url = "https://demoqa.com/webtables"
    chrome_options = Options()
    chrome_options.add_argument('--disable-cache')
    chrome_options.add_argument('--disk-cache-size=0')
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(url)
    return driver


#El metodo buscaTextos genera un arreglo con los Textos web
def buscaTextos(driver):
    textos = [6]
    firstname = driver.find_element(By.XPATH, "//input[@id=\"firstName\"]")
    textos.append(firstname)
    lastname = driver.find_element(By.XPATH, "//input[@id=\"lastName\"]")
    textos.append(lastname)
    email = driver.find_element(By.XPATH, "//input[@id=\"userEmail\"]")
    textos.append(email)
    age = driver.find_element(By.XPATH, "//input[@id=\"age\"]")
    textos.append(age)
    salary = driver.find_element(By.XPATH, "//input[@id=\"salary\"]")
    textos.append(salary)
    department = driver.find_element(By.XPATH, "//input[@id=\"department\"]")
    textos.append(department)
    return textos

def CasoPrueba02(driver,mail):
    mail.send_keys('111222333')
    time.sleep(1)
    doc = "CP-02-EvidenciaFormatoIncorrecto1.png"
    driver.save_screenshot(doc)
    mail.clear()
    mail.send_keys('1111@aaaaa')
    time.sleep(1)
    doc = "CP-02-EvidenciaFormatoIncorrecto2.png"
    driver.save_screenshot(doc)
    mail.clear()
    mail.send_keys('prueba@mail.com')
    time.sleep(1)
    doc = "CP-02-EvidenciaFormatoCorrecto.png"
    driver.save_screenshot(doc)
    return driver
def CasoPrueba03(driver,edad):
    edad.send_keys('aaaa')
    time.sleep(1)
    doc = "CP-03-EvidenciaFormatoIncorrecto.png"
    driver.save_screenshot(doc)
    edad.clear()
    edad.send_keys('29')
    doc = "CP-03-EvidenciaFormatoCorrecto.png"
    driver.save_screenshot(doc)
    return driver
def CasoPrueba04(driver,sueldo):
    sueldo.send_keys('aaaa')
    time.sleep(1)
    doc = "CP-04-EvidenciaFormatoIncorrecto.png"
    driver.save_screenshot(doc)
    sueldo.clear()
    sueldo.send_keys('5000')
    time.sleep(1)
    doc = "CP-04-EvidenciaFormatoCorrecto.png"
    driver.save_screenshot(doc)
    return driver

def CasoPrueba05(driver,nombre,apellido,departamento,submit):
    #submit = driver.find_element(By.XPATH, "//button[@id=\"submit\"]")
    res=0
    nombre.send_keys('Braulio')
    apellido.send_keys('Aguilera')
    departamento.send_keys('Informatica')
    time.sleep(1)
    doc = "CP-05-EvidenciaDatos.png"
    driver.save_screenshot(doc)
    submit.click()
    time.sleep(1)
    doc = "CP-05-EvidenciaTabla.png"
    driver.save_screenshot(doc)
    return driver

def CasoPrueba06(driver):
    btnEditar = driver.find_element(By.XPATH, "//*[@id=\"edit-record-4\"]")
    btnEditar.click()
    time.sleep(1)
    departamento = driver.find_element(By.XPATH, "//input[@id=\"department\"]")
    submit = driver.find_element(By.XPATH, "//button[@id=\"submit\"]")
    departamento.clear()
    departamento.send_keys('Sales')
    time.sleep(1)
    doc = "CP-06-EvidenciaIngreso.png"
    driver.save_screenshot(doc)
    submit.click()
    time.sleep(1)
    doc = "CP-06-EvidenciaTabla.png"
    driver.save_screenshot(doc)
    return driver

def CasoPrueba07(driver):
    btnEditar = driver.find_element(By.XPATH, "//*[@id=\"edit-record-4\"]")
    btnEditar.click()
    time.sleep(1)
    sueldo = driver.find_element(By.XPATH, "//input[@id=\"salary\"]")
    submit = driver.find_element(By.XPATH, "//button[@id=\"submit\"]")
    sueldo.clear()
    sueldo.send_keys('15000')
    time.sleep(1)
    doc = "CP-07-EvidenciaIngreso.png"
    driver.save_screenshot(doc)
    submit.click()
    time.sleep(1)
    doc = "CP-07-EvidenciaTabla.png"
    driver.save_screenshot(doc)
    return driver

def CasoPrueba08(driver):
    buscar = driver.find_element(By.XPATH, "//input[@id=\"searchBox\"]")
    buscar.send_keys('Braulio')
    time.sleep(1)
    doc = "CP-08-EvidenciaBusqueda.png"
    driver.save_screenshot(doc)
    return driver

def CasoPrueba09(driver):
    btnEliminar = driver.find_element(By.XPATH, "//*[@id=\"delete-record-4\"]")
    btnEliminar.click()
    time.sleep(1)
    doc = "CP-09-EvidenciaEliminar.png"
    driver.save_screenshot(doc)

def CasoPrueba10(driver):
    buscar = driver.find_element(By.XPATH, "//input[@id=\"searchBox\"]")
    buscar.send_keys('Braulio')
    time.sleep(1)
    doc = "CP-10-EvidenciaTabla.png"
    driver.save_screenshot(doc)
    return driver