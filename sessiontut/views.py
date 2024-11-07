from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # To access to session variables
    request.session["name"] = {"name1":"rosell", "name2":"pepito"}
    request.session["lastname"] = "pupo polanco"

    return HttpResponse("Home Session App")

def get(request):
    # To access and update session variables
    request.session["name"] = "roselito"
    name = request.session["name"]
    lastname = request.session["lastname"]

    print(name, lastname)

    return HttpResponse("GET view")

def delete(request):
    # To delete to session variables
    del request.session["name"]
    del request.session["lastname"]

    # To complete remove session
    request.session.flush()
    # Delete expired session from db
    request.session.clear_expired()

    return HttpResponse("DELETE view")

def update(request):
    # This dont work directly
    request.session["name"]["name1"] = "daryanis"
    request.session.modified = True

    return HttpResponse("UPDATE view")