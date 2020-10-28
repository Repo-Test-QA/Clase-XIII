#1 Escribir en un archivo y si el archivo existe entonces borrar todo y que se cree de la nada
#2 Añadir algo al final del archivo
#3 Leer algo
#4 Escribir en un archivo y sino existe crearlo

# Modos:
#1 - w (write)
#2 - a (append)
#3 - r (read)
#4 - w+ (write plus - escribe y sino existe crealo)


# Función para leer el archivo
def read_file(filename):
    my_file = open(filename, 'r')
    print(my_file.read())
    my_file.close()


# De acuerdo al modo w+ (Crear y escribir en el archivo, sino existe crealo) se va a llamar data.txt
my_file = open('data.txt', 'w+')
# Vamos a escribir en el archivo data.txt => Pablo, Ana, Jorge, Natalia => Agregamos salto de linea
my_file.write('Pablo\nAna\nJorge\nNatalia')
# Al final cerramos el archivo
my_file.close()
# Al ejecutar el programa, se debe mostrar el archivo creado data.txt

# Ahora vamos a Leer el archivo.
read_file('data.txt')

# Crear otros datos, modo write, se va a sobreescribir la información, solo debe mostrarse estos 3 nombres
my_file = open('data.txt', 'w')
my_file.write('Pepe\nJorge\nNorma')
my_file.close()

# Ahora vamos a Leer el archivo para verificar que se haya agregada la nueva data, modo read
read_file('data.txt')

# Agregamos nuevos datos y se muestren al final del archivo
my_file = open('data.txt', 'a')
my_file.write('\nAldo\nRomina\nRicardo')
my_file.close()

# Vamos a verificar que se haya agregado los nuevos nombre, deberían ser 6 nombres,
#read_file('data.txt')

# Ahora, lo que quiero es utilizar un cursor que vaya leyendo linea por linea, para trabajar
# con la información que encuentre en la misma
my_file = open('data.txt', 'r')
# Con esto ya no dependo del cursor
nombres = my_file.readlines()
# Recorre la lista de nombres
for nombre in nombres:
    # Ahora imprime nombre por nombre, deja un espacio por el salto de linea
    # Con esto ya puedo leer y escribir archivos
    print(nombre)

# Vamos a verificar que en este punto se trae la información de un elemento, mejoramos esto con lo de arriba
#print(my_file.readlines(2))


# Cuidado: Se muestra una colección
#print(my_file.readlines())
# En esta caso por segunda ves, muestra vacia la colección []
# porque en el caso anterior ya ha leído todos los elementos, posteriormente el cursor
# no encuentra nada. Es decir, el cursor llega al final y no puede volver (este es el problema)
#print(my_file.readlines())














