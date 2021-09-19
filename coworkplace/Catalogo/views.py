from django.shortcuts import render
#Para imprimir mensajes sencillos de respuesta se importa la siguiente libreria:
from django.http import HttpResponse

# Create your views here.

def vistaEjemplo(request):
    """
    request -> contiene toda la información del usuario que hace la petición de acceso a la aplicación.  
               A través de métodos GET y POST, principalmente.
    
    GET     -> Método con el cual el usuario solicita acceder a una URL.

    POST    -> Método con el cual el usuario envía información a una URL.

    """
    return HttpResponse ("Hola, estás en la aplicación del catálogo!!!")
