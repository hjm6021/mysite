from django.shortcuts import render

app_name = "blog"
# Create your views here.
def index(request):
    return render(request, "index.html")