from django.shortcuts import render
from .forms import FileUploadForm
from django.http import HttpResponse
from .models import UserData

# Create your views here.

def uploadFile(request):
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Form saved OKOK")
    else:
        form = FileUploadForm()
        context = {'form':form}
        return render(request, "files/upload.html", context)
    
def server(request):
    userData = UserData.objects.all();

    context = {
        'data': userData
    }
    return render(request, "files/server.html", context)