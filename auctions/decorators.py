from django.http import HttpResponse
from django.shortcuts import redirect

# Create your decorators here

def Unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect('auctions:index')

        return view_func(request, *args, **kwargs)

    return wrapper_func

def Authenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect('auctions:index')

        return view_func(request, *args, **kwargs)

    return wrapper_func
