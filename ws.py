# -*- coding: utf-8 -*-
__author__ = 'juliens'


from suds.client import Client
from suds.transport.http import HttpAuthenticated

url = 'http://academico.espoch.edu.ec/OAS_Interop/Infogeneral.wsdl'
#url adicional
urlCarrera = 'http://academico.espoch.edu.ec/OAS_Interop/Infocarrera.wsdl'

cliente = Client(url)
from suds.sax.element import Element

#Definimos el nombre de usuario
user = Element('acad:username').setText('webmail')

#Definimos la contraseña
pwd = Element('acad:password').setText('webmail')

#Creamos el elemento padre, y el espacio de nombres
reqsoapheader = Element('acad:credentials', ns=['acad','http://academico.espoch.edu.ec/'])

#agregamos usuario y contraseña al padre
reqsoapheader.children = [user, pwd]

#Seteamos los soapheaders con las credenciales de login
cliente.set_options(soapheaders=reqsoapheader)

#Llamamos a los servicios web
a = cliente.service.GetCiudades()

print a
