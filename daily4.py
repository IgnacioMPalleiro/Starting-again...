# Solicitar al usuario que ingrese la palabra a contar
palabra = input("Ingrese la palabra a contar: ")

# Inicializar el contador
contador = 0

# Intentar abrir el archivo book.txt
try:
    # Usar barras invertidas dobles o barras normales en la ruta
    # Empieza abriendo el archivo en UTF-8
    with open("C:/Users/ignac/Desktop/programación/book.txt", 'r', encoding='utf-8') as archivo:
        # Leer el contenido del archivo
        texto = archivo.read()
        # Contar cuántas veces aparece la palabra en el texto
        contador = texto.lower().split().count(palabra.lower())
except FileNotFoundError:
    print("El archivo 'book.txt' no se encontró. Asegúrate de que el archivo esté en la ruta especificada.")
except Exception as e:
    print(f"Ocurrió un error: {e}")

# Mostrar el resultado en consola
print(
    f"La palabra '{palabra}' aparece {contador} veces en el archivo 'book.txt'.")
