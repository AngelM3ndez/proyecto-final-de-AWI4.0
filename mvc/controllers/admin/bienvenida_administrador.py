import web # libreria para usar el framework web.py
import pyrebase # libreria para contecarse con firebase
import firebase_config as token # archivo con la configuracion de firebase
import json # libreria para manejar el formato JSON


render = web.template.render('mvc/view/admin', base="layout")


class Bienvenida_administrador:
    def GET(self): 
        if ( web.cookies().get('localid')) != "":
            return render.bienvenida_administrador() 
        else:
            return render.login() 