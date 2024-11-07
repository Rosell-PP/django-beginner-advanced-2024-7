# Custom middlewares
# Function vs Class based

### 
### Function Based Middleware
###
def MyCustomFunctionMiddleware(get_response):
    # code executed one time in configuration or initialization
    print("One time conf")

    ###
    ### Funcion middleware
    ###
    def middleware(request):
        # Code executed before the view  is called
        print("Before the view  is called")

        response = get_response(request)

        # Code executed after the view  is called
        print("After the view  is called")

        return response
    
    return middleware

### 
### Class Based Middleware
###
### Hooks :
###  - process_view
###  - process_exception
###  - process_template_response
class MyCustomClassMiddleware:
    # Constructor
    def __init__(self, get_response):
        self.get_response = get_response;
        
        # code executed one time in configuration or initialization
        print("CBM - One time conf")

    def __call__(self, request):
        # Code executed before the view  is called
        print("CBM - Before the view  is called")

        response = self.get_response(request)

        # Code executed after the view  is called
        print("CBM - After the view  is called")

        return response

    # Hook
    def process_view(
            self,
            request,    # La solitud
            view_func,  # Funcion que se ejecuta en la vista
            view_args,  # Los argumentos que recibe la vista
            view_kargs  # Los argumentos en forma de diccionario 
        ):
        print("Called just before calling the view")
        return None
    
    # Hook
    def process_exception(
            self,
            request,    # La solitud
            exception   # La excepcion capturada
        ):
        print("Called just after raise an exception in the view")
        return None
    
    # Hook
    def process_template_response(
            self,
            request,    # La solitud
            response    # La respuesta
        ):
        print("Called just after the view has finished executing")
        return response
