import web # se importa la libreria de web.py para hacer sus del framework
import pyrebase # se importa la libreria de firebase para hacer uso de la fire base creada de google
import firebase_config as token # se importa la libreria de firebase_comfig para hacer uso de nuestro token de fire base
import json # se importa la libreria de json para hacer uso y modificación de estos elementos


render = web.template.render('mvc/view/operador', base="layout")


class Bienvenida_usuario:
    def GET(self): 
        if ( web.cookies().get('localid')) != "": # cookie
            return render.bienvenida_usuario() # redirecinar a bienevenida
        else:
            return render.login() # redirecinar a login