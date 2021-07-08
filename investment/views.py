from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from investment.models import Post, Category
from django.core.paginator import Paginator
from django.conf import settings
from .forms import PostForm
from hitcount.views import HitCountDetailView
from django.contrib.auth.decorators import login_required

login_url = "/accounts/signin"

def get_number_of_posts():
    number_of_rows = {}
    latest_category_list = Category.objects.all().order_by("-create_dt")
    for category in latest_category_list:
        post_list = Post.objects.all().filter(category_id=category.pk)
        count = post_list.count()
        number_of_rows[category.name] = count

    return number_of_rows

# Create your views here.
def index(request):
    # Get으로 페이지 번호 획득
    page = request.GET.get('page')
    
    # 템플릿 지정
    template_name = "investment/investment_index.html"
    
    # DB로부터 데이터 획득
    latest_category_list = Category.objects.all().order_by("-create_dt")
    latest_post_list = Post.objects.all().order_by("-create_dt")
    
    # 페이지 기능 사용하기
    paginator = Paginator(latest_post_list, 4)
    
    # Get으로 획득한 페이지번호로 해당하는 수의 포스트를 획득
    posts = paginator.get_page(page)
    
    context = {"latest_category_list":latest_category_list, "posts":posts, "number":get_number_of_posts()}

    return render(request, template_name, context)

def list(request, category_slug):

    # Get으로 페이지 번호 획득
    page = request.GET.get('page')
    
    # 템플릿 지정
    template_name = "investment/investment_index.html"

    # DB로부터 데이터 획득
    latest_category_list = Category.objects.all().order_by("-create_dt")
    category = Category.objects.get(slug=category_slug)
    latest_post_list = Post.objects.all().filter(category_id=category.pk).order_by("-create_dt")

    # 페이지 기능 사용하기
    paginator = Paginator(latest_post_list, 4)
    
    # Get으로 획득한 페이지번호로 해당하는 수의 포스트를 획득
    posts = paginator.get_page(page)

    context = {"latest_category_list":latest_category_list, "posts":posts, "number":get_number_of_posts()}

    return render(request, template_name, context)

class PostCountHitDetailView(HitCountDetailView):
    model = Post        # your model goes here
    count_hit = True    # set to True if you want it to try and count the hit
    template_name = "investment/investment_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # self.kwargs는 urls.py로부터 받아온 값
        post_id = self.kwargs['pk']
        category_slug = self.kwargs['category_slug']
        
        # DB로부터 데이터 획득
        latest_category_list = Category.objects.all().order_by("-create_dt")
        category = Category.objects.get(slug=category_slug)
        post = Post.objects.get(id=post_id)

        context = {"latest_category_list":latest_category_list, "post":post, "number":get_number_of_posts()}

        # Disqus 세팅
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post-{category.slug}-{post.id}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{post.get_absolute_url()}"
        context['disqus_title'] = f"{post.title}"
        return context

"""
def detail(request, category_slug, post_id):
    # 템플릿 지정
    template_name = "investment/investment_detail.html"

    # DB로부터 데이터 획득
    latest_category_list = Category.objects.all().order_by("-create_dt")
    category = Category.objects.get(slug=category_slug)
    post = Post.objects.get(id=post_id)

    context = {"latest_category_list":latest_category_list, "post":post, "number":get_number_of_posts()}

    # Disqus 세팅
    context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
    context['disqus_id'] = f"post-{category.slug}-{post.id}"
    context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{post.get_absolute_url()}"
    context['disqus_title'] = f"{post.title}"

    return render(request, template_name, context)
"""
@login_required(login_url=login_url)
def add(request):
    # 템플릿 지정
    template_name = "investment/investment_add.html"

    # DB로부터 데이터 획득
    latest_category_list = Category.objects.all().order_by("-create_dt")

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            category = Category.objects.get(pk=form.data['category'])
            obj = Post(title=form.data['title'], category_id=category, description=form.data['description'], content=form.data['content'])
            obj.save()
            return redirect("investment:index")
    else:
        form = PostForm()

    context = {"latest_category_list":latest_category_list, "form":form, "number":get_number_of_posts()}

    return render(request, template_name, context)

@login_required(login_url=login_url)
def edit(request, post_id):
    # 수정할 포스트 획득
    post = get_object_or_404(Post, pk=post_id)

    # 템플릿 지정
    template_name = "investment/investment_edit.html"
    
    # DB로부터 데이터 획득
    latest_category_list = Category.objects.all().order_by("-create_dt")

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            category = Category.objects.get(pk=form.data['category'])
            post.title = form.data['title']
            post.category_id = category
            post.description = form.data['description']
            post.content = form.data['content']
            post.save()
            return redirect("investment:index")
    else:
        initial = {'title':post.title, 'category':post.category_id, 'description':post.description, 'content':post.content}
        form = PostForm(initial=initial)

    context = {"latest_category_list":latest_category_list, "form":form, "number":get_number_of_posts()}
    return render(request, template_name, context)

@login_required(login_url=login_url)
def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect("investment:index")
