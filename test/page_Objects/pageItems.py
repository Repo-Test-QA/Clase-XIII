# Cada página va a tener su propia clase.
# Cada clase va a tener los elementos que va a utilizar
# y las interacciones que se va a tener sobre la página.

# Página que obtiene los resultados, se va a llamar pageItems.py

# Importamos la librería By de Selenium
from selenium.webdriver.common.by import By

# Agregamos la librería para trabajar con selects
from selenium.webdriver.support.ui import Select


class PageItems:

    # Al constructor le pasamos el driver, porque vamos a hacer cosas con el driver.
    def __init__(self, my_driver):
        self.no_results_banner = '//*[@id="center_column"]/p'
        self.title_banner = '//*[@id="center_column"]/h1/span[1]'

        # Agregar ropa al carrito, elemento que muestra el color naranja
        self.orange_button = 'color_1'

        # Elemento select, en una Tupla
        self.order = (By.ID, 'selectProductSort')

        # Clase XII, localizar el elemento Chexbox (filtros de búsqueda Summer y M)
        self.checkbox = (By.CLASS_NAME, 'checkbox')

        # Clase XII, localizar el elemento checkbox (Filtros de búsqueda Color)
        self.colorcheck = (By.CLASS_NAME, 'color-option  ')

        self.driver = my_driver

    # Vamos a retornar los Textos y que el Caso de Prueba sea quien verifique las cosas.
    def return_no_element_text(self):
        return self.driver.find_element_by_xpath(self.no_results_banner).text

    def return_section_title(self):
        return self.driver.find_element_by_xpath(self.title_banner).text

    def click_orange_button(self):
        self.driver.find_element_by_id(self.orange_button).click()

    # Seleccionamos una opción de la lista desplegable
    def select_by_text(self, text):
        # Al select le paso el web element, para que pueda leer la Tupla, agregamos el asterisco adelante
        order = Select(self.driver.find_element(*self.order))
        # Seleccionar por el texto visible, le pasamos como parámetro texto
        order.select_by_visible_text(text)


    def select_by_value(self, value):
        # Al select le paso el web element, para que pueda leer la Tupla, agregamos el asterisco adelante
        order = Select(self.driver.find_element(*self.order))
        # Seleccionar por el valor, le pasamos como parámetro value
        order.select_by_value(value)


    def select_by_index(self, number):
        # Al select le paso el web element, para que pueda leer la Tupla, agregamos el asterisco adelante
        order = Select(self.driver.find_element(*self.order))
        # Seleccionar por el índice, le pasamos como parámetro number
        order.select_by_index(number)

        # Ahora vamos a crear nuestro método en searchItem


    def click_checkbox(self, number_filtro):
        # Estoy pasando como parámetro el índice, para seleccionar los filtros Summer y M
        self.driver.find_elements(*self.checkbox)[number_filtro].click()

    def click_color(self, number_color):
        # Estoy pasando como parámetro el índice, para selecconar los filtros de color
        self.driver.find_elements(*self.colorcheck)[number_color].click()




