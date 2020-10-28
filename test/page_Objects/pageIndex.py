# Cada página va a tener su propia clase.
# Cada clase va a tener los elementos que va a utilizar
# y las interacciones que se va a tener sobre la página.

# Importamos la librería By de Selenium
from selenium.webdriver.common.by import By

# Importamos dos librerías de selenium
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PageIndex:

    # Al constructor le pasamos el driver, porque vamos a hacer cosas con el driver.
    def __init__(self, my_driver):
        # Asignamos los valores de los elementos por id (textbox) y name (botón) a las propiedades/variables

        # Vamos a trabajar con la librería By para localizar los elementos,
        # Por tanto, comentamos los elementos.
        #self.query_top = 'search_query_top'
        #self.query_button = 'submit_search'

        # Ya no van a ser cadenas, sino Tuplas
        # Lo que voy a hacer es decirle porque tiene que buscar (id,name, etcétera)
        # y lo va a ser usando un Objeto de tipo By
        # Por tanto, tendríamos una Tupla y no necesito andar diciendole a
        # Selenium que tiene que andar buscando, porque toda la información
        # esta en la Tupla
        self.query_top = (By.ID, 'search_query_top')         # Cambiamos el id del elemento, para que no lo encuentre
        self.query_button = (By.NAME, 'submit_search')       # Despues de haber agregado la excepción, corregimos el id

        # Clase XII, agregando el elemento
        self.dresses_link = (By.XPATH, '//*[@title="Dresses"]')

        # Estoy pasando el parámetro my driver a driver.
        self.driver = my_driver

    def search(self, item):
        # Estoy pasando el parámetro item (el texto que se va a ingresar en la caja
        # de búsqueda 'search_query_top') a sendkeys

        # Comentamos porque ahora estamos trabajando con By, se detalla arriba
        #self.driver.find_element_by_id(self.query_top).send_keys(item)
        #self.driver.find_element_by_name(self.query_button).click()


        # Agregando la condición del explicit wait => 5'' máximo Timeout,
        # Espera hasta que el elemento exista, de que elemento, query_top (caja de texto)
        # por tanto, lo que va a devolver es un web element, con el cual voy a poder
        # hacer algo, lo vamos a asignar a una variable, search_box, el cual pasa a ser
        # un web element

        # Al no encontrar el elemento, vamos a agregar un Try, que intente de realizar esto,
        # posteriomente agregamos una excepción.
        try:
            search_box = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.query_top))
            search_box.send_keys(item)

            # Agregando la condición del explicit wait => 4'' máximo Timeout,
            # Espera hasta que el elemento sea visible, de que elemento, query_button (botón)
            # por tanto, lo que va a devolver es un web element, con el cual voy a poder
            # hacer algo, lo vamos a asignar a una variable, search_button, el cual pasa a ser
            # un web element
            search_button = WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located(self.query_button))
            search_button.click()

        # Al no poder realizar lo anterior, ingresa a la excepción y muestra el mensaje.
        except:
            print('No se encuentra el elemento')



        # Ahora no necesito andar diciendole a Selenium que tiene que andar buscando,
        # porque toda la información esta en la Tupla.
        # Cuando vamos a poner una Tupla como elemento que le pasan a un método, en este
        # caso => find_element
        # se tiene que poner un asterisco antes, sino no va a funcionar.
        # Ese asterisco hace que la Tupla se desarme para poder investigarla.
        #self.driver.find_element(*self.query_top).send_keys(item)
        #self.driver.find_element(*self.query_button).click()


        # Con esto le estamos pasando la responsabilidad al que tiene que realizar las
        # interacciones, es decir mi page object

        # Vamos a crear otro archivo, el cual va a tener una clase, la cual es la página
        # que obtiene los resultados, se va  llamar pageItems.py


    def click_dresses(self):
        # Cickeame el elemento que se encuentra en el índice 1
        self.driver.find_elements(*self.dresses_link)[1].click()