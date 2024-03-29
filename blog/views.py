from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

@login_required
def home(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView): 
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(kwargs["object"].content)
        context['content_list'] = kwargs["object"].content.splitlines()
        return context

    

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post    
    fields = ['title','content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post    
    fields = ['title','content','image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)      

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False        

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post  
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False    


def about(request):
    return render(request, 'blog/about.html',{'title':'About'}),

