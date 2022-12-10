from urllib import request
from django.views.generic import ListView, DetailView, TemplateView, View
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # This is needed for object oriented programming. A class should only inherit one class. A Mixin is another class that can be inherited from allwoing for a class to inherit more classes essentially.
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .models import Post
from django.shortcuts import redirect

class MyFriendsListView(TemplateView):
    template_name = "friends/friends_list.html"
class MyDashboardView(TemplateView):
    template_name = "pages/dashboard.html"
class PasswordResetDoneView(TemplateView):
    template_name = "pages/password_reset_done.html"
class UserProfileView(TemplateView):
    template_name = "posts/new.html"

class PostDetailView(DetailView, LoginRequiredMixin):
    template_name = "posts/post_detail.html"
    model = Post
# Create your views here.
class MyPostedListView(ListView):
    template_name = "posts/post_list.html"
    model = Post 
    # Refer to class video for more information: FSDI 112-2 C30 @ 02hr:29min
    def get_context_data(self, **kwargs): #Keyword arguments. All list views have this get_context_data() method. 
        context = super().get_context_data(**kwargs) # The get method returns records that matched the name = "published". you can also use it like this, .get(name="published")
        context["post_list"] = Post.objects.filter(poster=self.request.user # Ensuring that the data is returned based on the author logged in.
        ).order_by("created_on"
        ).reverse()
        return context
class PostListView(ListView):
    template_name = "posts/post_list.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "posts/post_detail.html"
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html" 
    model = Post
    success_url = reverse_lazy("post_list")
    fields = ["body"]

    def form_valid(self, form): # This overrides the default form_valid() method of Django 
        form.instance.requester = self.request.user # Allows the requester to request the user model.
        return super().form_valid(form) # Super() calls the form method
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # REMEMBER, Mixin order matters for validations.
    template_name = "posts/edit.html"
    model = Post
    success_url = reverse_lazy("post_list") 
    fields = ["body"] # Fields will be showed on the page
    # Test for UserPassesTestMixin that the user needs to pass
    def test_func(self):
        Post_obj = self.get_object()
        return Post_obj.requester == self.request.user
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # REMEMBER, Mixin order matters for validations.
    model = Post
    # success_url ="/Posts" # You can specify success urlurl to redirect after successfully
    template_name = "posts/delete.html" # deleting object
    success_url = reverse_lazy("post_list") # From Django's urls module. Redirects after successfully deleting object
    # Test for UserPassesTestMixin that the user needs to pass
    def test_func(self):
        Post_obj = self.get_object()
        return Post_obj.requester == self.request.user

