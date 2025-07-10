from django.shortcuts import render
from django.views.generic import ListView ,DetailView ,CreateView ,UpdateView ,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post


# UserPassesTestMixin: Checks if user is author of the post.

# test_func(): Prevents other users from editing someone else’s post.

# form_valid(): Again attaches the correct author.


class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3


class PostDetailView(DetailView):
    model = Post
    template_name ='post_detail.html'


class PostCreateView( LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title' , 'content']   
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView( UserPassesTestMixin, LoginRequiredMixin,UpdateView):
    model = Post
    fields = ['title' , 'content']   
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    

class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin ,DeleteView):
    model = Post
    success_url = '/'
    template_name = 'post_confirm_delete.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author