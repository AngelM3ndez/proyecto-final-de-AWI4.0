import web # se importa la libreria de web.py para hacer sus del framework
import pyrebase # se importa la libreria de firebase para hacer uso de la fire base creada de google
import firebase_config as token # se importa la libreria de firebase_comfig para hacer uso de nuestro token de fire base
import json # se importa la libreria de json para hacer uso y modificación de estos elementos


render = web.template.render("mvc/view/admin",base="layout")


class Activo:
    def GET(self, localId):
        try: 
            firebase = pyrebase.initialize_app(token.firebaseConfig) 
            db = firebase.database() 
            user = db.child("usuarios").child(localId).get()
            return render.activo(user)
        except Exception as error: 
            message = "Error en el sistema" 
            print("Error activo.GET: {}".format(error)) 
    
    def POST(self, localId):
       firebase = pyrebase.initialize_app(token.firebaseConfig)
       db = firebase.database()  
       formulario = web.input() 
       print(formulario)
       status = formulario.status 
       localid = formulario.localid  
       data = {
            "status": status,
        }
       results = db.child("usuarios").child(localid).update(data)
       return web.seeother("/user_list")