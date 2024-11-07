# El contexto definido aca se adiciona a cada template
# desde las vistas, muy util para enviar la misma
# info en todas las vistas
#
# @see blog/settings.py TEMPLATES.OPTIONS.context_processors

def something(request):
    return {
        "username":"Rosell Pupo Polanco"
    }