# Diccionario de productos
productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['Lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjFfHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['Lenovo', 14, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['Lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

# Diccionario de stock: modelo → [precio, stock]
stock = {
    '8475HD': [387990, 10],
    '2175HD': [327990, 4],
    'JjFfHD': [424990, 1],
    'fgdxFHD': [664990, 21],
    '123FHD': [298090, 32],
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2],
    'UWU131HD': [349990, 1]
}

def mostrar_titulo(texto):
    print("\n" + "*" * (len(texto) + 4))
    print(f"* {texto} *")
    print("*" * (len(texto) + 4))

def stock_marca(marca):
    marca = marca.lower()
    encontrados = False
    print(f"\n Stock disponible para marca '{marca.title()}':")
    for modelo, datos in productos.items():
        if datos[0].lower() == marca:
            disponibles = stock.get(modelo, [None, 0])[1]
            print(f"  - Modelo: {modelo} | Stock: {disponibles}")
            encontrados = True
    if not encontrados:
        print(" No se encontraron notebooks de esa marca.")

def busqueda_precio(minimo, maximo):
    encontrados = []
    for modelo, datos in stock.items():
        precio = datos[0]
        if minimo <= precio <= maximo:
            encontrados.append((modelo, productos[modelo], precio, datos[1]))
    if encontrados:
        print(f"\n🔍 Resultados entre ${minimo:,} y ${maximo:,}:")
        for modelo, datos, precio, cantidad in sorted(encontrados):
            print(f"  - Modelo: {modelo} | Marca: {datos[0]} | Precio: ${precio:,} | Stock: {cantidad}")
    else:
        print("No hay notebooks en ese rango de precios.")

def actualizar_precio(modelo, nuevo_precio):
    if modelo in stock:
        stock[modelo][0] = nuevo_precio
        return True
    return False

def solicitar_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Entrada no válida. Debe ser un número.")

def main():
    while True:
        mostrar_titulo("MENÚ PRINCIPAL")
        print("1. Stock por marca")
        print("2. Búsqueda por precio")
        print("3. Actualizar precio")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == '1':
            marca = input("Ingrese la marca a buscar: ").strip()
            stock_marca(marca)

        elif opcion == '2':
            minimo = solicitar_numero("Ingrese precio mínimo: $")
            maximo = solicitar_numero("Ingrese precio máximo: $")
            if minimo > maximo:
                print("  El precio mínimo no puede ser mayor al máximo.")
            else:
                busqueda_precio(minimo, maximo)

        elif opcion == '3':
            modelo = input("Ingrese el modelo a actualizar: ").strip()
            if modelo in stock:
                nuevo_precio = solicitar_numero("Ingrese el nuevo precio: $")
                actualizar_precio(modelo, nuevo_precio)
                print(" ¡Precio actualizado correctamente!")
            else:
                print("El modelo no existe.")
                repetir = input("¿Desea intentar con otro modelo? (sí/no): ").strip().lower()
                if repetir != 'sí':
                    continue

        elif opcion == '4':
            print("👋 Programa finalizado.")
            break

        else:
            print(" Opción inválida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
