import web # libreria para usar el framework web.py
import pyrebase # libreria para contecarse con firebase
import firebase_config as token # archivo con la configuracion de firebase
import json # libreria para manejar el formato JSON

render = web.template.render('mvc/view/admin', base="layout")

class Actualizar_sucursales:
    def GET(self, localId): 
         try: 
            firebase = pyrebase.initialize_app(token.firebaseConfig) 
            db = firebase.database() 
            user = db.child("sucursales").child(localId).get()
            return render.actualizar_sucursales(user)
        except Exception as error: 
            print("Error actualizar_sucursales.GET: {}".format(error))  
    
    def POST(self, localId):
            firebase = pyrebase.initialize_app(token.firebaseConfig) 
            db = firebase.database() 
            formulario = web.input()
            print(formulario) 
            name= formulario.name
            temperatura= formulario.temperatura
            humedad = formulario.humedad 
            email = formulario.email 
            localid = formulario.localid  
            data = {
            "name": name,
            "temperatura": temperatura,
            "humedad": humedad,
            "email": email,
            }
           results = db.child("sucursales").child(localid).update(data)
           return web.seeother("/lista_sucursales")