import web # libreria para usar el framework web.py
import pyrebase # libreria para contecarse con firebase
import firebase_config as token # archivo con la configuracion de firebase
import json # libreria para manejar el formato JSON

render = web.template.render('mvc/view/admin', base="layout")


class Insert_sucursales:
    def GET(self): 
        try: 
            message = None 
            return render.insert_sucursales(message) 
        except Exception as error: 
            message = "Error en el sistema" 
            print("Error insert_sucursales.GET: {}") 
            return render.insert_sucursales(message) 
    

    def POST(self): 
        firebase = pyrebase.initialize_app(token.firebaseConfig) 
        auth = firebase.auth() 
        db = firebase.database() 
        formulario = web.input() 
        name= formulario.name
        temperatura= formulario.temperatura
        humedad = formulario.humedad 
        data = {
        "name": name,
        "temperatura": temperatura,
        "humedad": humedad,
        }
        results = db.child("sucursales").child(name).set(data)
        return web.seeother("/bienvenida_administrador") 
        