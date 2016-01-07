from django.shortcuts import render

# Create your views here.
def home(self):
    nombre = "Jorge"
    desde = "Djnago"
    datos = [1,2,3,4,5,6,7,8,9]

    context = {
        'nombre': nombre,
        'desde': desde,
        'datos': datos,
    }

    return render(self, 'index.html',context)