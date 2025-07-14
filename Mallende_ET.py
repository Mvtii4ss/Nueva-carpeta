productos = {
'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {
'8475HD': [387990,10],
'2175HD': [327990,4], 
'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], 
'123FHD': [290890,32], 
'342FHD': [444990,7],
'GF75HD': [749990,2], 
'UWU131HD': [349990,1], 
'FS1230HD': [249990,0],
}

marca=""
modelo=""
p=0
p_min=0 
p_max=0

def stock_marca(marca):
    c=0
    marca=input("Ingrese marca a consultar: ")
    for i in productos:
         if marca==productos[i][0]:
            c+=stock[i][1]
    print(f"El stock es: {c}")
                        
         

def busqueda_precio(p_min, p_max):
    try:
        precio_encontrado=False
        p_min=int(input("Ingrese precio minimo: "))
        p_max=int(input("Ingrese precio maximo: "))
        modelos=[]
        for i in stock:
            if stock[i][0] in range(p_min, p_max) and stock[i][1]!=0:
                precio_encontrado=True
                marca=productos[i][0]
                m=i
                modelos.append(f"{marca}--{m}")

        if precio_encontrado==False:
            print("No hay notebooks en ese rango de precios.")
        else:
            print(f"Los notebooks entre los precios consultas son: {modelos}")
    except:
        print("Debe ingresar valores enteros!!")
    

def actualizar_precio(modelo, p):
    h=False
    while True:
        if h==True:
            repetir=input("Desea actualizar otro precio (s/n)?: ")
            if repetir=="n" or repetir=="N":
                break
            elif repetir=="n" or repetir=="N":
               modelo=input("Ingrese modelo a actualizar: ")
               p=input("Ingrese precio nuevo: ")
               if modelo in stock:
                   stock[modelo][0]=p
                   print("Precio actualizado!!")
                   h=True    
               else:
                    print("El modelo no existe!!")
                    break
            else:
               print("Opcion invalida")
               break
        else:
            modelo=input("Ingrese modelo a actualizar: ")
            p=input("Ingrese precio nuevo: ")
            if modelo in stock:
                stock[modelo][0]=p
                print("Precio actualizado!!")
                h=True    
            else:
                print("El modelo no existe!!")
                break
             




while True:
    try:
        op=int(input('''*** MENU PRINCIPAL ***
1. Stock marca.
2. Búsqueda por precio.
3. Actualizar precio.
4. Salir. 
Opcion: '''))
        match op:
            case 1:
                stock_marca(marca)
            case 2:
                busqueda_precio(p_min, p_max)
            case 3:
                actualizar_precio(modelo, p)
            case 4:
                print("Programa finalizado")
                break

    except:
        print("Debe seleccionar una opción válida!!")