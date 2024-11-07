from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import AddForm
from .models import Todo

from django.views import View
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

"""
    Base Views examples

    View
"""
class HomeClass(View):
    def get(self, request):
        todoList = Todo.objects.all()
        return render(request=request, template_name="todos/list.html", context={'list':todoList})

class AddClass(View):
    def get(self, request):
        form = AddForm()
        return render(request=request, template_name="todos/add.html", context={'form':form})
    
    def post(self, request):
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todos-home'))
        
        return render(request=request, template_name="todos/add.html", context={'form':form})
    
"""
    Template Views
"""
class AboutView(TemplateView):
    template_name = 'todos/about.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["context_data"] = "Data inside context";

        if 'name' in kwargs:
            context["name"] = kwargs["name"];
        
        return context
    
"""
    Redirect Views
"""
class AboutRedirectView(RedirectView):
    # url = "/todos/about/"
    
    pattern_name = "todos-home"

    #  For send urls query to redirected page
    query_string = True


"""
    Generic Views examples
    
    Display Views

    ListView
"""
class IndexView(ListView):
    #  Fetch all data from model and rendered
    model = Todo

    # Use default template model_list.html
    # and send the data into variables model_list and object_list

    # for order list
    ordering = ['-id']

    # for custom template
    # template_name = ""

    # for custom context variable name
    # context_object_name=""

    # for custom query
    # def get_queryset(self):
    #     return super() \
    #         .get_queryset() \
    #         .filter(work__icontains='reboot')
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["extra_data"] = "This is the value of the extra data"
        
        return context

"""
    DetailView
"""
class DetailsTodoView(DetailView):
    #  Fetch the object by pk or slug specified in url
    model = Todo

    # Use default template model_detail.html
    # and send the data into variables modelname and object

    # for custom template
    # template_name = ""

    # for custom context variable name
    # context_object_name=""

"""
    FormView
"""
class AddTodoFormView(FormView):
    # form class
    form_class = AddForm

    # template to render form
    template_name = "todos/add.html"

    # success url
    success_url = '/todos/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

"""
    CreateView
"""
class CreateTodoCreateView(CreateView):
    # models where save the data
    # model = Todo

    # fields we will save
    # fields = '__all__'

    # for specify the model class, if specify model and fields
    # will be ommited and declare template_name instead
    form_class = AddForm

    # Use default template model_form.html
    # and send the data into variables form

    # template to render form
    template_name = "todos/todo_form.html"

    # for change suffix of template
    # template_name_suffix = "_new"

    # redirect when save object in db
    success_url = '/todos/'
    
"""
    UpdateView
"""
class UpdateTodoView(UpdateView):
    model = Todo

    # fields = ['work']       # '__all__'

    # for specify the model class, if specify it fields
    # will be ommited and declare template_name instead
    form_class = AddForm

    # Use default template {model}_form.html
    # and send the data into variables form

    # template to render form
    # template_name = "todos/todo_form.html"

    # redirect when save object in db
    success_url = '/todos/'

"""
    DeleteView
"""
class DeleteTodoView(DeleteView):
    model = Todo

    # Use default template {model}_confirm_delete.html
    # and send the data into variables {model} and object

    success_url = "/todos/"