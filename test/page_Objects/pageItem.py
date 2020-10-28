# Cada página va a tener su propia clase.
# Cada clase va a tener los elementos que va a utilizar
# y las interacciones que se va a tener sobre la página.


class PageItem:
    def __init__(self, my_driver):

        # Elemento caja de texto donde se ingresa la cantidad
        self.quantity = 'quantity_wanted'
        # Elemento botón donde se aumenta la cantidad ingresada en + 1, considerar que la cantidad
        # por deault es 1
        self.plus = 'icon-plus'

        self.driver = my_driver

    # Método para ingresar la cantidad
    def enter_quantity(self, quantity):
        # En la 1era ejecución cuando ingresamos 25, en la caja de texto se muestra 125
        # porque como se había comentado anteriormente la caja de texto de cantidad viene
        # con el valor por default 1.
        # Entonces antes de ingresar la cantidad, vamos a limpiar la caja de texto.
        self.driver.find_element_by_id(self.quantity).clear()
        # Ahora en send_keys, vamos a ingresar al parámetro quantity la cantidad,
        # considere, es diferente a la variable que tiene asignada al elemento quantity.
        self.driver.find_element_by_id(self.quantity).send_keys(quantity)

    # Vamos a crear un método donde vamos a clickear n veces y yo le diga cuantas veces se va a
    # clickear
    def add_elements(self, quantity):
        # Le vamos a pasar una cantidad y esta va a ser un integer porque vamos a realizar
        # una operación con esta.
        for i in range(quantity):
            self.driver.find_element_by_class_name(self.plus).click()

    # Mediante este método lo que voy a hacer es devolver el valor que tengo en tal campo de texto
    # para verificar que el valor es 28
    def get_number_of_elements(self):
        # Por tanto, como vamos a corroborar que es un valor y no un texto. Nos vamos a traer el valor.
        # get_attribute => no solo sirve para traer el atributo value, sino también para otro atributo
        # del elemento.
        return self.driver.find_element_by_id(self.quantity).get_attribute('value')