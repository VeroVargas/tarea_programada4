import web
import gestor

render = web.template.render('./templates')
global precio
precio = "r"

urls=(
    '/','index',
    '/','menu_Busk',
    '/','agregar_apartamentos',
    '/','buscar_apartamentos',
    '/','busquedaPrecio',
    '/','busquedaFacilidades',
    '/','busquedaCaracteristicas',
    '/menu_Busk','menu_Busk',
    '/agregar_apartamentos','agregar_apartamentos',
    '/buscar_apartamentos','buscar_apartamentos',
    '/busquedaPrecio','busquedaPrecio',
    '/busquedaFacilidades','busquedaFacilidades',
    '/busquedaCaracteristicas','busquedaCaracteristicas',
    )

app = web.application(urls,globals())

class index:
    def GET(self):
        return render.index()

class menu_Busk:
    def GET(self):
        return render.menu_Busk()
    def POST(self):
	i = web.input()
        raise web.seeother('/menu_Busk')

class agregar_apartamentos:
    def GET(self):
        return render.agregar_apartamentos()
    def POST(self):
	i = web.input()
	titulo = (i.txtTitulo)
	nombre = (i.txtnombre)
	telefono = (i.txtTelefono)
        correo = (i.txtcorreo)
        nCuartos = (i.txtnc)
        cComp = i.ccomp
        cochera = i.cochera
        bComp = i.bcomp
        amueble = i.amueblado
        caract = (i.caract)
        precio = (i.precio)
        tv = i.tv
        agua = i.agua
        luz = i.luz
        internet = i.internet
        ubicacion = (i.ubicacion)
        print(ubicacion)
        apartas = gestor.apartamentos(titulo,nombre,telefono,correo,nCuartos,cComp,cochera,bComp,amueble,caract,precio,tv,luz,agua,internet,ubicacion)
        apartas.agregarAparta()
        
        raise web.seeother('/agregar_apartamentos')

class buscar_apartamentos:
    def GET(self):
        return render.buscar_apartamentos()
    def POST(self):
	i = web.input()
        raise web.seeother('/buscar_apartamentos')

class busquedaFacilidades:
    def GET(self):
        return render.busquedaFacilidades(" ")
    def POST(self):
	i = web.input()
	luz = i.luz
	agua = i.agua
	tele = i.tv
	inter = i.internet
	dato = gestor.consultaFacilidad(luz,agua,tele,inter)
	lista = dato.consulFacilidades()
	nueva = dato.acomodar(lista)
        return render.busquedaFacilidades(nueva)
    
class busquedaPrecio:
    def GET(self):
        return render.busquedaPrecio(" ")
    def POST(self):
	i = web.input()
	precio = i.txt_precio
	dato = gestor.consultaPrecio(precio)
	lista = dato.consulPrecio()
	nueva = dato.acomodar(lista)
	return render.busquedaPrecio(nueva)
        
class busquedaCaracteristicas:
    def GET(self):
        return render.busquedaCaracteristicas(" ")
    def POST(self):
	i = web.input()
	numero = i.txtnc
	compartido = i.ccomp
	cochera = i.cochera
	bcomp = i.bcomp
	amuebla = i.amueblado
	dato = gestor.consultaCaract(numero,compartido,cochera,bcomp,amuebla)
	lista = dato.consulCaract()
	nueva = dato.acomodar(lista)
	return render.busquedaCaracteristicas(nueva)

    
if __name__ == "__main__":
        app.run()
