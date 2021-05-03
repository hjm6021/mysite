from django.urls import path
from investment import views

app_name = "investment"
urlpatterns = [
    # investment/
    path('', views.index, name="index"),

    # inverstment/add
    path("add/", views.add, name='add'),

    # investment/python
    path("<slug:category_slug>/", views.list, name="list"),

    # investment/python/1
    path("<slug:category_slug>/<int:post_id>/", views.detail, name='detail')
]
