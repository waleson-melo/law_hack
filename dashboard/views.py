from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


# Create your views here.
class Index(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('usuarios-login')
    template_name = 'paginas/index.html'
