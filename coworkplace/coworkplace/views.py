from django.views import View   
from django.shortcuts import render

#=> sirve para especificar la lógica del frontend desde Django a través
# de peticiones de usuario. GET, POST, PUT, PATCH y DELETE


class LandingPage(View):
    template = "index.html"
    def get(self, request):
        return render(request, self.template, {})

class Reserva(View):
    template = "reserva.html"
    def get(self, request):
        return render(request, self.template, {})

class Acerca(View):
    template = "acerca_de.html"
    def get(self, request):
        return render(request, self.template, {})

class Contactos(View):
    template = "contactenos.html"
    def get(self, request):
        return render(request, self.template, {})

class Registro(View):
    template = "registro.html"
    def get(self, request):
        return render(request, self.template, {})

class ReservaUser(View):
    template = "reserva_usr.html"
    def get(self, request):
        return render(request, self.template, {})

