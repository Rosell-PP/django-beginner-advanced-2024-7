"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from posts.views import indexView

# Personaliza los textos del sitio de administracion
admin.site.site_header = "Course Django Udemy"
admin.site.site_title = "Course Django Udemy"
admin.site.index_title = "Course Django Udemy"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexView),

    path('posts/', include("posts.urls")),
    path('session/', include("sessiontut.urls")),
    path('accounts/', include("accounts.urls")),
    
    # for user bultin django auth views
    path('users/', include("django.contrib.auth.urls")),

    # for file uploads 
    path('files/', include("fileuploads.urls")),

    # for practice class base views
    path('todos/', include("todos.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # for expose files to users  
 


