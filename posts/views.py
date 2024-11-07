from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Post, Tag
from .forms import PostForm
from django.core.paginator import Paginator
from .forms import CommentForm
from django.db.models import Q

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView


# Devuelve la vista del listado de los posts
def indexView(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('posts-guest'))

    # order objects before paginate them
    allPosts = Post.objects.all().order_by("-id")

    # orphans => Si en la ultima pagina quedan esa cantidad o menos se muestran en la pagina anterior
    paginator = Paginator(allPosts, 3, orphans=2)

    # dont raise any except
    posts = paginator.get_page(request.GET.get("p", 1))

    response = render(request, "posts/posts.html", {
        "posts": posts
    })

    # for set cookies
    response.set_cookie("testcookie", "cookie1_without_max_age")
    response.set_cookie("testcookie_2", "cookie1_with_max_age", max_age=120, secure=True, httponly=True)
    # when a cookie is httponly=true cant be listed from client using document.cookie

    # for access cookies
    # request.COOKIES['cookie_name']

    # for delete cookie
    # request.delete_cookie("")

    # for update cookie
    # request.set_cookie("")

    return response

"""
    Listado de todos los posts utilizando CBV ListView
"""
class IndexViewListClass(ListView):
    model = Post
    ordering = ['-id']
    template_name = "posts/posts.html"
    context_object_name = "posts"

    # for paginate results
    # when paginate django send page_obj variable to template with pagination info
    paginate_by = 3
    paginate_orphans = 1

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        return context


def guestView(request):
    return render(request, "posts/guest.html")

# Devuelve la vista de detalles de un post especificado
def detailView(request, id):
    try:
        post = Post.objects.get(id=id)

        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.save()
                return HttpResponseRedirect(reverse('post-detail', args=[id]))
        
        commentForm = CommentForm()
        return render(request, "posts/post-details.html", {
            "post": post,
            "commentForm": commentForm,
        })
    except:
        raise Http404()

"""
    Detalles de un post utilizando CBV DetaiView
"""
class PostDetailsClass(DetailView):
    model = Post
    template_name = "posts/post-details.html"

    # self.object is relative with object model post

    # Modify context info
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["commentForm"] = CommentForm()
        return context
    
    # Override post method
    def post(self, request, pk):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.save()
            return HttpResponseRedirect(reverse('post-detail', args=[pk]))


# Devuelve vista para registrar un nuevo post
def savePostView(request):
    #  Debe estar autenticado para registrar un nuevo post
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('posts-guest'))
    
    if request.method == "POST":
        # Si el formulario tiene archivos se deben pasar como segundo argumento
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # title = form.cleaned_data["title"]
            # content = form.cleaned_data["content"]
            # post = Post.objects.create(post_title=title, post_content=content)
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            # Relaciono las etiquetas seleccionadas
            for tag in request.POST.getlist("tags"):
                post.tags.add(Tag.objects.get(name=tag))
            post.save()

            return HttpResponseRedirect(reverse('posts-home'))
    else:
        form = PostForm()

    context = {
        'form': form,
        'tags': Tag.objects.all(),
    }

    return render(request=request, template_name="posts/create.html", context=context)

def thanksView(request):
    return HttpResponse("Form enviado !!")

def updateView(request, id):
    post = Post.objects.get(id=id)

    if request.method == "POST":
        # using form class
        # form = PostForm(request.POST)

        # using formModel class
        form = PostForm(request.POST, instance=post, files=request.FILES)
        
        if form.is_valid():
            # post.post_title = form.cleaned_data["title"];
            # post.post_content = form.cleaned_data["content"];
            post = form.save(commit=False);

            print(request.POST.getlist("tags"))

            # Relaciono las etiquetas seleccionadas
            for tag in request.POST.getlist("tags"):
                post.tags.add(Tag.objects.get(name=tag))
            post.save()
    
            return HttpResponseRedirect('/posts/home')
    else:
        # using form class
        # form = PostForm(
        #     initial={
        #         'post_title': post.post_title,
        #         'post_content': post.post_content,
        #     }
        # );
    
        # using formmodel class
        form = PostForm(
            instance=post
        );
        context = {
            'tags': Tag.objects.all(),
            'form': form,
        }
    
    return render(request, "posts/update.html", context=context)

def deleteView(request, id):
    if request.method == "POST":
        post = Post.objects.get(id=id)
        post.delete()

    return HttpResponseRedirect('/posts/home')

# Vista de detalles de una etiqueta
def tagDetails(request, name):
    tag = Tag.objects.get(name=name)

    return render(request, "tags/tag_details.html", {
        'tag':tag
    })

"""
    Detalles de una etiqueta utilizando CBV DetaiView
"""
class TagDetailsClass(DetailView):
    model = Tag
    template_name = "tags/tag_details.html"


def search(request):
    filter = request.GET.get("filter", None)
    allPosts = Post.objects.filter(Q(post_title__icontains=filter) | Q(post_content__icontains=filter)).order_by("-id")

    paginator = Paginator(allPosts, 3)

    # dont raise any except
    posts = paginator.get_page(request.GET.get("p", 1))

    response = render(request, "posts/search.html", {
        "posts": posts,
        "filter": filter,
    })

    return response

"""
    Filtrado de los posts utilizando CBV ListView
"""
class SearchViewClass(ListView):
    model = Post
    ordering = ['-id']
    template_name = "posts/search.html"
    context_object_name = "posts"

    # for paginate results
    # when paginate django send page_obj variable to template with pagination info
    paginate_by = 3
    paginate_orphans = 1

    # for custom query
    def get_queryset(self):
        filter = self.request.GET.get("filter", None)
        return super() \
            .get_queryset() \
            .filter(Q(post_title__icontains=filter) | Q(post_content__icontains=filter))

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        filter = self.request.GET.get("filter", None)
        context["filter"] = filter
        return context
