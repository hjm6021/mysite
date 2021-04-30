from django.views.generic.base import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = "study/index.html"

class AboutView(TemplateView):
    template_name = "about.html"