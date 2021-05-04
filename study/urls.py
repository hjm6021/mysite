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

    # study/1/edit
    path("<int:post_id>/edit/", views.edit, name='edit'),

    # study/1/delete
    path("<int:post_id>/delete/", views.delete, name='delete'),
]
