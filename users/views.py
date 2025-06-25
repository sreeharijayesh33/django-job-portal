from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm
from .models import User
from django.contrib import messages

class CustomSignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, "Account created successfully! Please log in.")
        return super().form_valid(form)
