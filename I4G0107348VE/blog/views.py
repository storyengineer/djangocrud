from django.shortcuts import render
from blog.models import Post
from django.views import generic
from django.urls import reverse_lazy

class PostListView(generic.ListView):
    model = Post
    template_name = "blog/post_list.html"

class PostCreateView(generic.CreateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")
    template_name = "blog/post_form.html"

class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

class PostUpdateView(generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")
    template_name = "blog/post_form.html"

class PostDeleteView(generic.DeleteView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")
    template_name = "blog/post_confirm_delete.html"