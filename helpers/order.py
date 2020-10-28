a = [5, 8, 2, 1, 10, 25, 32, 45, 3, 8, 13, 7]
# Sort, ordena de manera ascendente los elementos del array.
#a.sort()
print('Array inicial:')
print(a)

# Vamos a utilizar con el ordenamiento Bubble sort
# Recorre el largo del Array, desde 1 hasta 12
for i in range(1, len(a)):
    # Se ejecuta desde 0 hasta 12 - i
    for j in range(0, len(a) - i):
        if a[j] > a[j+1]:
            temporal = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temporal
    print(a)
print('Array ordenado')
print(a)

