# -*- coding: utf-8 -*-
import sqlite3

class apartamentos:
    def __init__(self,titulo,nombre,telefono,correo,cuartos,ccomp,cochera,bano,amueblado,caract,precio,tv,luz,agua,internet,ubicacion):
        self.titulo=titulo
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.cuartos = cuartos
        self.ccomp = ccomp
        self.cochera = cochera
        self.bano = bano
        self.amueblado = amueblado
        self.caract = caract
        self.precio = precio
        self.tv = tv
        self.luz = luz
        self.agua = agua
        self.internet = internet
        self.ubicacion = ubicacion

    def agregarAparta(self):
        con = sqlite3.connect("base_aparta")
        cursor = con.cursor()
        cursor.execute("insert into APARTAMENTOS values('"+self.titulo+ "','"+self.nombre+ "','"
                       +self.telefono+"','"+self.correo+"','"+self.cuartos+"','"+self.ccomp+"','"+self.cochera+"','"+self.bano+"','"+self.amueblado+"','"+self.caract+"','"+self.precio+"','"+self.tv+"','"+self.luz+"','"+self.agua+"','"+self.internet+"','"
                       +self.ubicacion+"')")
        con.commit()
        con.close()

class consultaFacilidad:
    def __init__(self,luz,agua,tv,internet):
        self.luz = luz
        self.agua = agua
        self.tv = tv
        self.internet = internet

    def consulFacilidades(self):
        con = sqlite3.connect("base_aparta")
        cursor = con.cursor()
        cursor.execute("Select * from APARTAMENTOS where TV = '"+self.tv+"' and LUZ = '"+self.luz+"' and AGUA = '"+self.agua+"' and INTERNET = '"+self.internet+"'")
        lista = []
        for tabla in cursor.fetchall():
            print (tabla)
            lista.append(tabla)
        return lista

    def acomodar(self,lista):
        nueva = []
        indice = 0
        largo = len(lista)
        while(indice!=largo):
            nueva.append("Lista de apartamentos")
            nueva.append("")
            nueva.append("Caracteristicas: ")
            nueva.append("")
            nueva.append("Titulo: "+lista[indice][0])
            nueva.append("Cantidad de cuarto: " +str(lista[indice][4]))
            if(lista[indice][5] == "true"):
                nueva.append("Cuartos compartidos")
            if(lista[indice][7] == "true"):
                nueva.append("Baño compartido")
            if(lista[indice][8] == "true"):
                nueva.append("Amueblado")
            if(lista[indice][6] == "true"):
                nueva.append("Tiene cochera")
            if(lista[indice][11] == "true" and lista[indice][12] == "true" and lista[indice][13] == "true" and lista[indice][14] == "true"):
                nueva.append("Precio "+str(lista[indice][10])+" incluye TV, luz, agua e internet")
            if(lista[indice][11] == "true" and lista[indice][12] == "true" and lista[indice][13] == "true" and lista[indice][14] == "false"):
                nueva.append("Precio "+str(lista[indice][10])+" incluye TV, luz y agua")
            if(lista[indice][11] == "true" and lista[indice][12] == "true" and lista[indice][13] == "false" and lista[indice][14] == "true"):
                nueva.append("Precio "+str(lista[indice][10])+" incluye TV, luz e internet")
            if(lista[indice][11] == "true" and lista[indice][12] == "false" and lista[indice][13] == "true" and lista[indice][14] == "true"):
                nueva.append("Precio "+str(lista[indice][10])+" incluye TV, agua e internet")
            if(lista[indice][11] == "false" and lista[indice][12] == "true" and lista[indice][13] == "true" and lista[indice][14] == "true"):
                nueva.append("Precio "+str(lista[indice][10])+" incluye luz, agua e internet")
            else:
                nueva.append("Precio "+str(lista[indice][10]))
            
            nueva.append("")
            nueva.append("Contacto:")
            nueva.append("")
            nueva.append("Nombre: "+lista[indice][1])
            nueva.append("Telefono: "+str(lista[indice][2]))
            nueva.append("Correo: "+lista[indice][3])
            indice = indice + 1
            nueva.append("-----------------------------------------------")
        return nueva
    
class consultaPrecio:
    def __init__(self,atributo):
        self.atributo = atributo
  
    def consulPrecio(self):
        precioMin = int(self.atributo)
        precioMin = precioMin - 10000
        minpre = str(precioMin)
        lista = []
        con = sqlite3.connect("base_aparta")
        cursor = con.cursor()
        cursor.execute("Select * from APARTAMENTOS where PRECIO = '"+self.atributo+"'")
        for tabla in cursor.fetchall():
            print (tabla)
            lista.append(tabla)
        return lista
        con.close()
    
    def acomodar(self,lista):
        nueva = []
        indice = 0
        largo = len(lista)
        while(indice!=largo):
            nueva.append("Lista de apartamentos")
            nueva.append("")
            nueva.append("Caracteristicas: ")
            nueva.append("")
            nueva.append("Titulo: "+lista[indice][0])
            nueva.append("Cantidad de cuarto: " +str(lista[indice][4]))
            if(lista[indice][5] == "true"):
                nueva.append("Cuartos compartidos")
            if(lista[indice][7] == "true"):
                nueva.append("Baño compartido")
            if(lista[indice][8] == "true"):
                nueva.append("Amueblado")
            if(lista[indice][6] == "true"):
                nueva.append("Tiene cochera")
            if(lista[indice][11] == "true" and lista[indice][12] == "true" and lista[indice][13] == "true" and lista[indice][14] == "true"):
                nueva.append("Precio "+str(lista[indice][10])+" incluye TV, luz, agua e internet")
            if(lista[indice][11] == "true" and lista[indice][12] == "true" and lista[indice][13] == "true" and lista[indice][14] == "false"):
                nueva.append("Precio "+str(lista[indice][10])+" incluye TV, luz y agua")
            if(lista[indice][11] == "true" and lista[indice][12] == "true" and lista[indice][13] == "false" and lista[indice][14] == "true"):
                nueva.append("Precio "+str(lista[indice][10])+" incluye TV, luz e internet")
            if(lista[indice][11] == "true" and lista[indice][12] == "false" and lista[indice][13] == "true" and lista[indice][14] == "true"):
                nueva.append("Precio "+str(lista[indice][10])+" incluye TV, agua e internet")
            if(lista[indice][11] == "false" and lista[indice][12] == "true" and lista[indice][13] == "true" and lista[indice][14] == "true"):
                nueva.append("Precio "+str(lista[indice][10])+" incluye luz, agua e internet")
            else:
                nueva.append("Precio "+str(lista[indice][10]))
            
            nueva.append("")
            nueva.append("Contacto:")
            nueva.append("")
            nueva.append("Nombre: "+lista[indice][1])
            nueva.append("Telefono: "+str(lista[indice][2]))
            nueva.append("Correo: "+lista[indice][3])
            indice = indice + 1
            nueva.append("-----------------------------------------------")
        return nueva

class consultaCaract:
    def __init__(self,num,cuarto,cochera,bano,amueblada):
        self.num = num
        self.cuarto = cuarto
        self.cochera = cochera
        self.bano = bano
        self.amueblada = amueblada

    def consulCaract(self):
        lista = []
        con = sqlite3.connect("base_aparta")
        cursor = con.cursor()
        cursor.execute("Select * from APARTAMENTOS where CUARTOS = '"+self.num+"' or CCOMPARTIDO = '"+self.cuarto+
                       "'or COCHERA = '"+self.cochera+"'or BANO = '"+self.bano+"'or AMUEBLADO = '"+self.amueblada+"'")
        for tabla in cursor.fetchall():
            print (tabla)
            lista.append(tabla)
        return lista
        con.close()

    def acomodar(self,lista):
        nueva = []
        indice = 0
        largo = len(lista)
        while(indice!=largo):
            nueva.append("Lista de apartamentos")
            nueva.append("")
            nueva.append("Caracteristicas: ")
            nueva.append("")
            nueva.append("Titulo: "+lista[indice][0])
            nueva.append("Cantidad de cuarto: " +str(lista[indice][4]))
            if(lista[indice][5] == "true"):
                nueva.append("Cuartos compartidos")
            if(lista[indice][7] == "true"):
                nueva.append("Baño compartido")
            if(lista[indice][8] == "true"):
                nueva.append("Amueblado")
            if(lista[indice][6] == "true"):
                nueva.append("Tiene cochera")
            if(lista[indice][11] == "true" and lista[indice][12] == "true" and lista[indice][13] == "true" and lista[indice][14] == "true"):
                nueva.append("Precio "+str(lista[indice][10])+" incluye TV, luz, agua e internet")
            if(lista[indice][11] == "true" and lista[indice][12] == "true" and lista[indice][13] == "true" and lista[indice][14] == "false"):
                nueva.append("Precio "+str(lista[indice][10])+" incluye TV, luz y agua")
            if(lista[indice][11] == "true" and lista[indice][12] == "true" and lista[indice][13] == "false" and lista[indice][14] == "true"):
                nueva.append("Precio "+str(lista[indice][10])+" incluye TV, luz e internet")
            if(lista[indice][11] == "true" and lista[indice][12] == "false" and lista[indice][13] == "true" and lista[indice][14] == "true"):
                nueva.append("Precio "+str(lista[indice][10])+" incluye TV, agua e internet")
            if(lista[indice][11] == "false" and lista[indice][12] == "true" and lista[indice][13] == "true" and lista[indice][14] == "true"):
                nueva.append("Precio "+str(lista[indice][10])+" incluye luz, agua e internet")
            else:
                nueva.append("Precio "+str(lista[indice][10]))
            
            nueva.append("")
            nueva.append("Contacto:")
            nueva.append("")
            nueva.append("Nombre: "+lista[indice][1])
            nueva.append("Telefono: "+str(lista[indice][2]))
            nueva.append("Correo: "+lista[indice][3])
            indice = indice + 1
            nueva.append("-----------------------------------------------")
        return nueva
