
def nuevo_Tema(tema:str):
    print(f"\n--------{tema}---------\n")

if __name__== "__main__":
    #Tarea 1
    nuevo_Tema("Operadores aritmeticos")
    print("Operador suma, 5+6",5+6)
    print("Operador resta, 9-8",9-8)
    print("Operador multiplicacion, 4*4",4*4)
    print("Operador potencia, 6**2",6**2)
    print("Operador division, 20/4",20/4)
    print("Operador division sin decimal, 20//4",20//4)
    print("Operador modulo, 20%8",20%8)
    print("Operador cambio de signo, -20",-20)
    
    nuevo_Tema("Operadores Logicos")
    print("True and True",True and True)
    print("True or False",True or False)
    print("Not False", not False)

    nuevo_Tema("Tablas de verdad")
    nuevo_Tema("-----AND-----")
    print("True and True",True and True)
    print("True and False",True and False)
    print("False and True",False and True)
    print("False and False",False and False)
    nuevo_Tema("-----OR-----")
    print("True or False",True or False)
    print("False or True",False or True)
    print("False or False",False or False)
    nuevo_Tema("-----Not-----")
    print("False or False",False or False)
    print("Not False", not False)
    print("Not True", not True)

    
    print("5 == 5",5 == 5)    
    print("10 == 5",10 != 5)    
    print("2 < 5", 2 < 5)    
    print("2 <= 5", 5 <= 5)   
    print("2 > 5", 2 > 5)   
    print("2 >= 5", 2 >= 5)   

    nuevo_Tema("Variables")
    variable = 10
    _variable2 = 3.1416
    variable3 = "Pepe"
    nombreVariable = 8
    NOMBRE_VARIABLE = 34.12
    print(variable,_variable2,variable3,nombreVariable,NOMBRE_VARIABLE)
    a, b, c = 12, 1.2, "Hola"
    print(a)
    print(b)
    print(c)

    nuevo_Tema("Enteros")

    w = 105
    x = 123456578798654
    y = 0b00111011
    h = 0xFF

    print(w, type(w))
    print(x, type(x))
    print(y, type(y))
    print(h, type(h))

    nuevo_Tema("Flotantes")
    x =  12345.56
    print(x, type(x))
    y = -0.285
    print(y, type(y))

    nuevo_Tema("Numers complejos")
    y = -45j
    x = 12 + 45j
    z = 2j
    c = y + z
    print(y,type(y)) 
    print(x,type(x)) 
    print(z,type(z)) 
    print(c,type(c))

    nuevo_Tema("Booleanos")
    x = True
    print(x,type(x))

    nuevo_Tema("Datos Secuenciales")
    nuevo_Tema("Listas")
    lista = [10, 20.5, "Lista de Python"]
    print(lista)
    print(lista[2])
    lista.append(34) #inserta dato al final
    lista.insert(0, 1) #inserta dato al inicio
    print(lista)
    lista.append([3, 4, 5, 6, 13])
    print(lista)
    print(lista[5])
    print(lista[5][2])
    print(lista[3][3])

    nuevo_Tema("Tuplas")
    tupla = (25, "Tupla",1+20j)
    print(tupla) #tuplas son inmutables e iterables
    print(tupla[0])

    nuevo_Tema("Conjuntos")
    conjunto = {10,20,30,40,50} #son desordenados
    conjunto.add(80)
    print(conjunto)
    print(50 in conjunto) #busca el elemento

    nuevo_Tema("Diccionarios")
    diccionario = {"Nombre": "Uriel",
                    "Edad": 31,
                    "Telefono":12354654,
                    90: 4 + 3}
    print(diccionario)
    print(diccionario["Nombre"])
    print(diccionario["Edad"])

    nuevo_Tema("Cadenas")
    cadena1 = "Esta es una cadena"
    cadena2 = 'Esta es otra cadena'
    cadena_multilinea = '''Esta es una cadena muy locochona '''
    print(cadena_multilinea)
    print(cadena_multilinea[5:])
    print(cadena_multilinea[:-5])
    print(cadena_multilinea[::-1])