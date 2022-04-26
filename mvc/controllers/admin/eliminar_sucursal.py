import web # libreria para usar el framework web.py
import pyrebase # libreria para contecarse con firebase
import firebase_config as token # archivo con la configuracion de firebase
import json # libreria para manejar el formato JSON

render = web.template.render('mvc/view/admin', base="layout")

class Eliminar_sucursal:
    def GET(self, localId): 
        try: 
            message = None 
            return render.eliminar_sucursal(message) 
        except Exception as error: 
            message = "Error en el sistema" 
            print("Error eliminar_sucursal.GET: {}") 
            return render.eliminar_sucursal(message) 
    

    def POST(self, localId): 
        firebase = pyrebase.initialize_app(token.firebaseConfig) 
        db = firebase.database() 
        formulario = web.input() 
        name= formulario.name
        temperatura= formulario.temperatura
        humedad = formulario.humedad 
        email = formulario.email
        data = {
        "name": name,
        "email": email,
        "temperatura": temperatura,
        "humedad": humedad,
        }
        results = db.child("sucursales").child(localId).remove(data)
        return web.seeother("/bienvenida_administrador") 
        