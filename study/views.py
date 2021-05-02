from django.shortcuts import render
from study.models import Post, Category
from django.core.paginator import Paginator
from django.conf import settings

# Create your views here.
def index(request):
    # Get으로 페이지 번호 획득
    page = request.GET.get('page')
    
    # 템플릿 지정
    template_name = "index.html"
    
    # DB로부터 데이터 획득
    latest_category_list = Category.objects.all().order_by("-create_dt")
    latest_post_list = Post.objects.all().order_by("-create_dt")
    
    # 페이지 기능 사용하기
    paginator = Paginator(latest_post_list, 4)
    
    # Get으로 획득한 페이지번호로 해당하는 수의 포스트를 획득
    posts = paginator.get_page(page)
    
    context = {"latest_category_list":latest_category_list, "posts":posts}

    return render(request, template_name, context)

def list(request, category_slug):

    # Get으로 페이지 번호 획득
    page = request.GET.get('page')
    
    # 템플릿 지정
    template_name = "index.html"

    # DB로부터 데이터 획득
    latest_category_list = Category.objects.all().order_by("-create_dt")
    category = Category.objects.get(slug=category_slug)
    latest_post_list = Post.objects.all().filter(category_id=category.pk).order_by("-modify_dt")

    # 페이지 기능 사용하기
    paginator = Paginator(latest_post_list, 4)
    
    # Get으로 획득한 페이지번호로 해당하는 수의 포스트를 획득
    posts = paginator.get_page(page)

    context = {"latest_category_list":latest_category_list, "posts":posts}

    return render(request, template_name, context)

def detail(request, category_slug, post_id):
    # 템플릿 지정
    template_name = "detail.html"

    # DB로부터 데이터 획득
    latest_category_list = Category.objects.all().order_by("-create_dt")
    category = Category.objects.get(slug=category_slug)
    post = Post.objects.get(id=post_id)
    context = {"latest_category_list":latest_category_list, "post":post}

    # Disqus 세팅
    context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
    context['disqus_id'] = f"post-{category.name}-{post.id}"
    context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{post.get_absolute_url()}"
    context['disqus_title'] = f"{post.title}"

    return render(request, template_name, context)