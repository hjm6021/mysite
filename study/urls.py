from django.urls import path
from study import views

app_name = "study"
urlpatterns = [
    # study/
    path('', views.index, name="index"),

    # study/add
    path("add/", views.add, name='add'),

    # study/python
    path("<slug:category_slug>/", views.list, name="list"),

    # study/python/1
    path("<slug:category_slug>/<int:post_id>/", views.detail, name='detail'),
]
