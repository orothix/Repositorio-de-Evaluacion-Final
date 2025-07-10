from Evaluacion_base import menu_principal
## codigo Principal

productos = [
    {"marca": "HP", "modelo" :{'8475HD', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'}},
    {"marca":"lenovo", "modelo":{ '2175HD', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'}},
    {"marca":"Asus", "modelo":{ 'JjfFHD', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'}},
    {"marca":"HP", "modelo":{ 'fgdxFHD', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'}},
    {"marca":"Asus", "modelo":{ 'GF75HD', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'}},
    {"marca":"Lenovo", "modelo":{ '123FHD', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'}},
    {"marca":"Lenovo", "modelo":{ '342FHD', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'}},
    {"marca":"Dell", "modelo":{ 'UWU131HD', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'}},
]


stock = [
    {"marca": "HP", "modelo": "8475HD", "precio": 450000,"cantidad": 15},
    {"marca":"lenovo", "modelo": "2175HD", "precio": 350000,"cantidad": 20},
    {"marca":"Asus", "modelo": "JjfFHD", "precio": 600000,"cantidad": 7},
    {"marca":"HP", "modelo": "fgdxFHD", "precio": 285000,"cantidad": 2},
    {"marca":"Asus", "modelo": "GF75HD", "precio": 500000,"cantidad": 31},
    {"marca":"Lenovo", "modelo": "123FHD", "precio": 320000,"cantidad": 23},
    {"marca":"Lenovo", "modelo": "342FHD", "precio": 400000,"cantidad": 17},
    {"marca":"Dell", "modelo": "UWU131HD", "precio": 300000,"cantidad": 1}
]

salir = False
contador = 0

while salir is False:
    menu_principal()
    
    opc = input("ingrese la operacion: ")
    match opc:
        case "1": #busqueda de stock de marca
            busqueda_stock = input("ingrese la marca a consultar: ")
            
            for marca in stock:
                if marca["marca"].lower() == busqueda_stock.lower():
                    contador += 1     
                    print(f"{contador}.- Modelo:",marca["modelo"],"con un stock de:" ,marca["cantidad"])
            if contador == 0:
                print("no tenemos stock de la marca")
            
            contador = 0
             
        case "2": #busqueda de precio
            busqueda_precio_minimo = int(input("ingrese el precio minimo: "))
            busqueda_precio_maximo = int(input("ingrese el precio maximo: "))
            
            print("----------")
            for precio in stock:
                if precio["precio"] > busqueda_precio_minimo:
                    if precio["precio"] < busqueda_precio_maximo:
                        contador += 1 
                        print(f"{contador}.- modelo:",precio["modelo"],"precio:",precio["precio"])
            if contador == 0:
                print(f"no se encontraron productos con un precio entre {busqueda_precio_minimo} y {busqueda_precio_maximo}")
            contador = 0
                 
        case "3": #actualizar el precio
            modelo_buscar = input("ingrese el modelo a actualizar (0 para cancelar): ")
            if modelo_buscar == 0:
                break
            for actualizar_precio in stock:
                if actualizar_precio["modelo"].lower() == modelo_buscar.lower():
                    cambiar_precio = input("ingrese el precio a cambiar: ")
                    contador += 1
                
                    stock[contador] = cambiar_precio
                    
                    
            if contador == 0:
                print(f"no se encontro el modelo '{modelo_buscar}'")
            contador = 0
        case "4": #salir
            print("hasta luego")
            salir = True
        case _:
            print("opcion no valida, ingrese opciones del 1 al 4")