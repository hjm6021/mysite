from django.shortcuts import render
from investment.models import Post, Category

# Create your views here.
def index(request):
    template_name = "investment/index.html"
    latest_category_list = Category.objects.all().order_by("-create_dt")
    #latest_post_list = Post.objects.all().order_by("-modify_dt")
    context = {"latest_category_list":latest_category_list}
    return render(request, template_name, context)

def list(request, category_id):
    template_name = "investment/index.html"
    latest_category_list = Category.objects.all().order_by("-create_dt")
    #latest_post_list = Post.objects.all().order_by("-modify_dt")
    context = {"latest_category_list":latest_category_list}
    return render(request, template_name, context)

