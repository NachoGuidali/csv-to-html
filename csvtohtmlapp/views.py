from django.shortcuts import render
from .models import Archivo
import csv


# Create your views here.



def home(request):
    with open("/home/nachogakd/importcsv/importcsv/csvtohtmlapp/precios_con_coma.csv", "r") as archivo:
        lector = csv.reader(archivo, delimiter=",")
        rows = []
        for row in lector:
           
        
            rows.append(row)

    return render(request, 'index.html',{'rows':rows})


    """ descmarca = fila[0] 
            producto = fila[1]
            descrip = fila[2]
            claseprod = fila[3]
            preciosiva = fila[4]
        

            #print(descmarca, producto, descrip, claseprod, preciosiva)"""
            

    """def home(request):
    context = {
        "archivos" : Archivo.objects.all()
    }
    return render(request, "index.html", context=context)"""



"""def home(request):
    csv_filepath = "/home/nachogakd/importcsv/importcsv/csvtohtmlapp/precios_con_coma.csv"

    with open(csv_filepath, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = []
        for row in csv_reader:
            rows.append(row)

    return render(request, 'index.html',{'rows':rows})"""        