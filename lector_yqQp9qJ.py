import csv

nombre_archivo = "precios_con_coma.csv"
def lector():
    with open("/home/nachogakd/importcsv/importcsv/csvtohtmlapp/precios_con_coma.csv", "r") as archivo:
        lector = csv.reader(archivo, delimiter=",")
    
        for fila in lector:
            descmarca = fila[0] 
            producto = fila[1]
            descrip = fila[2]
            claseprod = fila[3]
            preciosiva = fila[4]
        
            print(descmarca, producto, descrip, claseprod, preciosiva)
lector()            