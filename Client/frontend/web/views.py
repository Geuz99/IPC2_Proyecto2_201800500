from django.shortcuts import render, redirect, HttpResponse
import requests
import csv
import os
import re


# Create your views here.

endpoint  = 'http://localhost:5000{}'


def inicio(request):    
    return render(request,'index.html')

def envio(request):
    pass

def index(request):
    if request.method == 'GET':        
        url = endpoint.format('/datos')  # http://localhost:5000/datos
        #data = requests.get(url)  # consulta a la API       
        data = open('importante.xml', 'r+')
        data_oficial = data.read
        context = {
            'output': data_oficial,
        }
        return render(request, 'data.html', context)

    elif request.method == 'POST':
        docs = request.FILES['document']
        data = docs.read()
        file = open('clientes.csv', "wb")
        file.write(data)
        file.close()  
        file_clientes = open('clientes.csv')
        csv_f1 = csv.reader(file_clientes)
        data_clientes = []
        for row in csv_f1:
            data_clientes.append(row)
        file_clientes.close()     
        for row in data_clientes[1:]:
            names = row[0].split(";")
            last = row[1].split(";")
            age = row[2].split(";")
            birth = row[3].split(";")
            date = row[4].split(";")
            if names[0].isalpha() and last[0].isalpha() and age[0].isalnum() and re.match(r'^([0-2][0-9]|3[0-1])(\/)(0[1-9]|1[0-2])\2(\d{4})$',birth[0]) and re.match(r'^([0-2][0-9]|3[0-1])(\/|-)(0[1-9]|1[0-2])\2(\d{4})$',date[0]):
                print('todo correcto')
            else:
                return render(request,'error.html')
        docs2 = request.FILES['document2']   
        data2 = docs2.read()
        file2 = open('mejoresClientes.csv', "wb")
        file2.write(data2)
        file2.close()
        file_mejoresClientes = open('mejoresClientes.csv')
        csv_f2 = csv.reader(file_mejoresClientes)
        data_mejoresClientes = []
        for row in csv_f2:
            data_mejoresClientes.append(row)
        file_mejoresClientes.close() 
        for row in data_mejoresClientes[1:]:
            names = row[0].split(";")
            date = row[1].split(";")
            cantidad1 = row[2].split(";")
            cantidad2 = row[3].split(";")
            if names[0].isalpha() and re.match(r'^([0-2][0-9]|3[0-1])(\/|-)(0[1-9]|1[0-2])\2(\d{4})$',date[0]) and cantidad1[0].isalnum() and cantidad2[0].isalnum():
                print('todo correcto')
            else:
                print('Existe un error')
                return render(request,'error.html')  
        docs3 = request.FILES['document3']   
        data3 = docs3.read()
        file3 = open('juegosMasVendidos.csv', "wb")
        file3.write(data3)
        file3.close() 
        file_juegosMasVendidos = open(path)
        csv_f3 = csv.reader(file_juegosMasVendidos)
        data_juegosMasVendidos = []
        for row in csv_f3:
            data_juegosMasVendidos.append(row)
        file_juegosMasVendidos.close()   
        for row in data_juegosMasVendidos[1:]:
            names = row[0].split(";")
            date = row[1].split(";")
            copias = row[2].split(";")
            stock = row[3].split(";")
            if names[0].isalpha() and re.match(r'^([0-2][0-9]|3[0-1])(\/|-)(0[1-9]|1[0-2])\2(\d{4})$',date[0]) and copias[0].isalnum() and stock[0].isalnum():
                print('todo correcto')       
            else:
                print('Existe un error')
                return render(request,'error.html')
        docs4 = request.FILES['document4']   
        data4 = docs4.read()
        file4 = open('juegos.csv', "wb")
        file4.write(data4)
        file4.close()
        file_juegos = open(path)
        csv_f4 = csv.reader(file_juegos)
        data_juegos = []
        for row in csv_f4:
            data_juegos.append(row)
        file_juegos.close()
        for row in data_juegos[1:]:
            names = row[0].split(";")
            plataforma = row[1].split(";")
            date = row[2].split(";")            
            clasificacion = row[3].split(";")
            if names[0].isalpha() and plataforma[0].isalpha() and re.match(r'^([0-2][0-9]|3[0-1])(\/|-)(0[1-9]|1[0-2])\2(\d{4})$',date[0]) and re.match(r'[ETM]',clasificacion[0]):
                print('todo correcto')       
            else:
                print('Existe un error')
                return render(request,'error.html')
        chet = open('importante.xml', 'w')
        chet.write("<Chet>" + os.linesep)        
        allData = clientes_a_xml('clientes.csv') + mejoresClientes_a_xml('mejoresClientes.csv') + juegosMasVendidos_a_xml('juegosMasVendidos.csv') + juegos_a_xml('juegos.csv')
        chet.write(allData + os.linesep) 
        chet.write("</Chet>") 
        url = endpoint.format('/datos')
        #requests.post(url, allData)
        return redirect('index')

def convert_row(row):
    return """<clientes>
    <nombre>%s</nombre>
    <apellido>%s</apellido>
    <edad>%s</edad>
    <fechaCumpleagnos>%s</fechaCumpleagnos>
    <fechaPrimeraCompra>%s</fechaPrimeraCompra>
</clientes>""" % (row[0], row[1], row[2], row[3], row[4])

def convert_row2(row):
    return """<mejoresClientes>
    <nombre>%s</nombre>
    <fechaUltimaCompra>%s</fechaUltimaCompra>
    <cantidadComprada>%s</cantidadComprada>
    <cantidadGastada>%s</cantidadGastada>
</mejoresClientes>""" % (row[0], row[1], row[2], row[3])

def convert_row3(row):
    return """<juegosMasVendidos>
    <nombre>%s</nombre>
    <fechaUltimaCompra>%s</fechaUltimaCompra>
    <copiasVendidas>%s</copiasVendidas>
    <stock>%s</stock>
</juegosMasVendidos>""" % (row[0], row[1], row[2], row[3])

def convert_row4(row):
    return """<juegos>
    <nombre>%s</nombre>
    <plataforma>%s</plataforma>
    <agnoLanzamiento>%s</agnoLanzamiento>
    <clasificacion>%s</clasificacion>
</juegos>""" % (row[0], row[1], row[2], row[3])

def err(x):
    return x

def clientes_a_xml(path):
    file_clientes = open(path)
    csv_f1 = csv.reader(file_clientes)
    data_clientes = []
    for row in csv_f1:
        data_clientes.append(row)
    file_clientes.close()               
    datos1 = '\n'.join([convert_row(row) for row in data_clientes[1:]])    
    return datos1       

def mejoresClientes_a_xml(path):
    file_mejoresClientes = open(path)
    csv_f2 = csv.reader(file_mejoresClientes)
    data_mejoresClientes = []
    for row in csv_f2:
        data_mejoresClientes.append(row)
    file_mejoresClientes.close()
    datos2 = '\n'.join([convert_row2(row) for row in data_mejoresClientes[1:]])
    return datos2

def juegosMasVendidos_a_xml(path):
    file_juegosMasVendidos = open(path)
    csv_f3 = csv.reader(file_juegosMasVendidos)
    data_juegosMasVendidos = []
    for row in csv_f3:
        data_juegosMasVendidos.append(row)
    file_juegosMasVendidos.close()
    datos3 = '\n'.join([convert_row3(row) for row in data_juegosMasVendidos[1:]])
    return datos3

def juegos_a_xml(path):
    file_juegos = open(path)
    csv_f4 = csv.reader(file_juegos)
    data_juegos = []
    for row in csv_f4:
        data_juegos.append(row)
    file_juegos.close()
    datos4 = '\n'.join([convert_row4(row) for row in data_juegos[1:]])
    return datos4

def ayuda(request):    
    return render(request,'ayuda.html')

def error(request):        
    return render(request,'error.html')





    