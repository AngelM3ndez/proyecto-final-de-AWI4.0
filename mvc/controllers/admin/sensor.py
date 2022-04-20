import web
import app
import web # se importa la libreria de web.py para hacer sus del framework
import pyrebase # se importa la libreria de firebase para hacer uso de la fire base creada de google
import firebase_config as token # se importa la libreria de firebase_comfig para hacer uso de nuestro token de fire base

render = web.template.render('mvc/view/admin', base="layout")


class Sensor:
    def GET(self):
        if ( web.cookies().get('localid')) == "": # se pone una condicional si localid es igual a vacio que esta nos vuelva a mandar a la pagina login
            return web.seeother("/inicio")
        else :
         return render.sensor() # nos devuelve el render bienvendia 


    def POST(self):
       firebase = pyrebase.initialize_app(token.firebaseConfig) # se inicializa la configuración del fire base
       db = firebase.database()  # se inicializa el metodo de base de datos en firebase
       formulario1 = web.input(id ="formulario1") # se crea una variable formulario para recibir los datos del registrar.html
       valor=formulario1.btn_encendido
       print("valor",valor)
       data = { "enfriamiento": valor
       }
       results = db.child("sensor").child("sucursal1").update(data)
       return web.seeother("/sensor")