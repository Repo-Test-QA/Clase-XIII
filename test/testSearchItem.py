from selenium import webdriver

# Librerías de python
import unittest
import time

# Del archivo pageIndex, importame la clase PageIndex,
# Entonces ya puedo crear objetos en esta clase de tipo PageIndex.
from test.page_Objects.pageIndex import PageIndex

# Del archivo pageItems, importame la clase PageItems,
# Entonces ya puedo crear objetos en esta clase de tipo PageItems.
from test.page_Objects.pageItems import PageItems

# Del archivo pageItem, importame la clase PageItem,
# Entonces ya puedo crear objetos en esta clase de tipo PageItem.
from test.page_Objects.pageItem import PageItem

# Clase XI, importamos chrome options para poder pasarle opciones al explorador Chrome
from selenium.webdriver.chrome.options import Options


class SearchCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Creando nuestra bd...')
        print('BD creada')

    @classmethod
    def tearDownClass(cls):
        print('Eliminando nuestra bd...')
        print('BD eliminada')

        
    # Método que tiene las Precondiciones
    def setUp(self):

        # Clase XI, instanciamos la clase Options
        option = Options()
        # Podemos ahora pasarle argumentos, en este caso el navegador se va a mostrar maximizado
        option.add_argument('start-maximized')
        # 2do argumento, podemos testear en modo incognito
        option.add_argument('incognito')

        # Considerar, levantar un browser en modo gráfico con su ventanita, es muy pesado y usa tiempo.
        # por eso existe algo llamado Modo Headless, no se va a ver, pero si se va a ejecutar de manera
        # rápida, entonces no se deben ejecutar las pruebas en modo gráfico.
        # 4to Argumento, se debe empezar a ejecutar en Modo Headless. Para este caso, vamos habilitar
        # todos los casos de pruebas
        # Comentamos por un momento, para hacer una prueba, cuando estemos programando el caso de prueba
        # no debemos trabajar en modo headless, cuando ya este listo el testcase, activamos tal modo
        #option.add_argument('--headless')

        # 3er argumento, sino queremos que chrome use el gpu (hardware de la tarjeta gráfica)
        #option.add_argument('--disable-gpu')

        # Por tanto, tenemos dos formas o maneras de controlar ciertas cosas del browser.
        # - A partir de Selenium
        # - A partir de las opciones de Chrome (Recomendable)

        # Ahora voy a pasar al webdriver.Chrome un segundo argumento con esto comentamos los maximize, size y position
        #self.driver = webdriver.Chrome('../chromedriver.exe', chrome_options=option)
        self.driver = webdriver.Chrome('test/chromedriver.exe', options=option)

        # Clase XI, se va a presentar maximizada la pantalla del navegador
        # self.driver.maximize_window()
        # También, podemos personalizar el tamaño de la ventana del navegador, ancho x alto
        #self.driver.set_window_size(200, 240)
        # Podemos indicar la posición donde se va a mostrar el navegador
        #self.driver.set_window_position(150, 150)

        # Abrir el browser
        self.driver.get('http://automationpractice.com/index.php')
        # Agregando el implicit wait, tu timeout a partir de acá son 5''
        self.driver.implicitly_wait(5)

        # Creamos un objeto de la clase PageIndex, le vamos a pasar el parámetro driver.
        self.indexPage = PageIndex(self.driver)

        # Creamos un objeto de la clase PageItems, le vamos a pasar el parámetro driver.
        self.itemsPage = PageItems(self.driver)

        # Creamos un objeto de la clase PageItem, le vamos a pasar el parámetro driver.
        self.itemPage = PageItem(self.driver)

    @unittest.skip("Not needed now")
    def test_search_no_elements(self):
        #try:
        self.indexPage.search('hola')
        # Vamos a esperar dos segundos, para que cargue la página
        # con sus elementos.
        #time.sleep(2)

        #self.assertEqual(self.itemsPage.return_no_element_text(), 'No results were found for your search "saludo"') # hola
        self.assertEqual(self.itemsPage.return_no_element_text(), 'No results were found for your search "hola"')

        # Verificamos que si ingreso un texto que no existe,
        # se muestre el mensaje en la página  => No results were found for your search "hola"
        # Mediante el assertEqual, comparamos si las dos variables son iguales.
        # Cuando encontremos el xpath, vamos a extraer el texto, para asignarlo a la variable
        # result y así compararla con el texto de la variable expected_result
        # result = driver.find_element_by_xpath('//*[@id="center_column"]/p').text
        # expected_result = 'No results were found for your search "hola"'

        # Comentamos las dos variables de arriba, en el assert reemplazamos los valores de las
        # variables y nos ahorramos dos lineas de código
        #self.assertEqual(self.driver.find_element_by_xpath('//*[@id="center_column"]/p').text, 'No results were found for your search "hola"')

        # Clase XI, para capturar la pantalla de evidencia, hacemos lo siguiente, agregamos un nombre con su extensión
        # Otro caso sería que si la prueba falla se va a tomar la evidencia, cambiamos "hola" por "Saludo"
        # Agregamos el try.
        # Recomendación, no se debe utilizar try para los Assert.
        self.driver.save_screenshot('no_element.jpg')
        #except:
            # Si hay un error debe generar una evidencia de la misma
            #self.driver.save_screenshot('errorss.jpg')


    @unittest.skip("Not needed now")
    def test_search_find_dresses(self):
        self.indexPage.search('dress')
        #time.sleep(2)

        self.assertTrue("DRESS" in self.itemsPage.return_section_title())

        # Mediante el assertTrue.
        # cuando encontremos el xpath, vamos a extraer el texto, para asignarlo a la variable
        # result y así compararla con el texto de la variable expected_result
        #result = driver.find_element_by_xpath('//*[@id="center_column"]/h1/span[1]').text
        #expected_result = "DRESS"

        # el texto DRESS se encuentra en el texto que tiene la variable result.
        # Comentamos las dos variables de arriba, en el assert reemplazamos los valores de las
        # variables y nos ahorramos dos lineas de código
        #self.assertTrue("DRESS" in self.driver.find_element_by_xpath('//*[@id="center_column"]/h1/span[1]').text)

    @unittest.skip("Not needed now")
    def test_search_find_tshirts(self):
        self.indexPage.search('t-shirts')
        #time.sleep(2)

        self.assertTrue('T-SHIRTS' in self.itemsPage.return_section_title(), self.itemsPage.return_section_title())

        # El 3er parámetro es un mensaje, el cual muestra lo que tiene como texto encontrado
        # mediante el xpath.
        # Si no se encuentra el texto que ingresamos "T-SHIRTS" en el texto que encuentra el xpath
        # muestra el texto que ha encontrado.
        # Este es el error que se muestra => AssertionError: False is not true : "T-SHIRT"
        #self.assertTrue('T-SHIRTS' in self.driver.find_element_by_xpath('//*[@id="center_column"]/h1/span[1]').text, self.driver.find_element_by_xpath('//*[@id="center_column"]/h1/span[1]').text)


    # Ejercicio de meter ropa en el carro
    @unittest.skip("Not needed now")
    def test_tarea(self):
        self.indexPage.search('T-Shirts')
        #time.sleep(2)

        self.itemsPage.click_orange_button()

        # Como vamos a otra página, agregamos 2'' para que carguen los elementos
        self.itemPage.enter_quantity('25')
        # Vamos a clickear 3 veces, pasamos al parámetro el valor 3.
        self.itemPage.add_elements(3)

        # Asigno a una variable lo que devuelve el método, en este caso el valor del elemento
        number = self.itemPage.get_number_of_elements()
        # Verificamos me diante el assert si el valor es igual a 28
        self.assertTrue(number == '28')

        # Vamos a agregar unos segundos para verificar que se muestre la cantidad ingresada
        #time.sleep(3)


    @unittest.skip("Not needed now")
    def test_selection(self):
        # Ingresamos T-shirts
        self.indexPage.search('t-shirts')

        # Seleccionamos el elemento por el texto, es decir el parámetro text
        self.itemsPage.select_by_text('Product Name: A to Z')
        time.sleep(3)

        # Seleccionamos el elemento por el value, es decir el parámetro value
        self.itemsPage.select_by_value('reference:asc')
        time.sleep(3)

        # Seleccionamos el elemento por el índice, es decir el parámetro number
        self.itemsPage.select_by_index(4)
        time.sleep(3)


    def test_dresses_options(self):
        # Elegir la opción Dresses
        self.indexPage.click_dresses()
        # Agregamos un tiempo para verificar que llegamos a la página Dresses
        #time.sleep(3)
        # Seleccionar el filtro Summer
        self.itemsPage.click_checkbox(2)
        # Seleccionamos el filtro M
        self.itemsPage.click_checkbox(4)
        # Seleccionamos el filtro Color Negro
        self.itemsPage.click_color(2)
        time.sleep(3)


    # Método que tiene las Postcondiciones, que quiero que pase, cuando termina una prueba.
    def tearDown(self):
        # Cerrar el browser
        self.driver.close()
        # Cerrar la sesión del webdriver
        self.driver.quit()



if __name__ == '__main__':
    # Las pruebas que encuentre acá, las va a ir ejecutando.
    unittest.main()
