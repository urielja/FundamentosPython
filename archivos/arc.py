#crear file object 
file = open("EjemploArchivo.txt", "w")
file.write("Este es el contenido del archivo.")
file.close()

lista = ["Fresa", "Mango", "Papaya"]

with open("EjemploArchivo.txt","a") as file:#se agrega al final del archivo, 
    for e in lista:                         #crea un contexto de trabajo y el interprete una vez que sale del contexto libera el archivo
        file.write("\n" + e + "\n")         #es la forma correcta de trabajar la lecture y escritura de un archivo

print("Lista escrita en el archivo")

lista2 = ["Honda", "Suzuki", "BMW"]

with open("EjemploArchivo.txt", "a") as file:
    file.writelines(lista2)

print("Lista escrita con writelines")

print("Imprimir todo el contenido del archivo. ")
with open("EjemploArchivo.txt", "r") as file:
    print(file.read())

print("Leer dos lineas y posteriormente 5 caracteres.")
with open("EjemploArchivo.txt", "r") as file:
    print(file.readline())
    print(file.readline())
    print(file.readline(5))

print("Almacenar el contenido en una lista y mostrar el ultimo elemento")
with open("EjemploArchivo.txt", "r") as file:
    contenido = file.readlines()
    print(contenido[-1])