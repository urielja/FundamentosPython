import pickle

info = [35, 88, 3.14,15]

with open("./archivos/ArchivoSerial", "wb") as binFile: #archivos binarios
    pickle.dump(info,binFile)

print("El archivo binario escrito")

with open("./archivos/ArchivoSerial", "rb") as binFile: #archivos binarios
    lista = pickle.load(binFile)
    print(lista)

print("Archivo binario leido y reconstruido")
