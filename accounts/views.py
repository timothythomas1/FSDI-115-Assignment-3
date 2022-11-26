from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Create your views here.
class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
class UserProfileUpdateView(UpdateView):
    template_name = "posts/user_profile.html"
    success_url = reverse_lazy("issue_list")
    model = CustomUser
    def get_initial(self):
        initial = super(UserProfileUpdateView, self).get_initial()
        try:
            current_group = self.object.groups.get()
        except:
            # exception can occur if the edited user has no groups
            # or has more than one group
            pass
        else:
            initial['group'] = current_group.pk
        return initial

    def get_form_class(self):
        return CustomUserChangeForm

    def form_valid(self, form):
        # self.object.groups.clear()
        # self.object.groups.add(form.cleaned_data['group'])
        return super(UserProfileUpdateView, self).form_valid(form)
    