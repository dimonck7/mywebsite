from blog.models import Post,Ver
from django.views.generic import ListView, DetailView, TemplateView

class PostsListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

class CreatView(TemplateView):
    template_name = "blog/creat.html"

class ComingView(TemplateView):
    template_name = "blog/coming.html"

class VerListView(ListView):
   model =  Ver
