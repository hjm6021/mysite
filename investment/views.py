from django.views.generic.base import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = "investment/index.html"

