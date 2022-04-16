from django.http import HttpResponse
from django.shortcuts import redirect

def usuario_logeado(func_view):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')

        return func_view(request, *args, **kwargs):
        
    return wrapper

 