from django.urls import path, re_path
from investment import views

app_name = "investment"
urlpatterns = [
    # investment/
    path('', views.index, name="index"),

    # inverstment/add
    path("add/", views.add, name='add'),

    # investment/python
    # path("<slug:category_slug>/", views.list, name="list"),
    re_path(r'^(?P<category_slug>[-\w]+)/$', views.list, name="list"), 

    # investment/python/1
    # path("<slug:category_slug>/<int:post_id>/", views.detail, name='detail'),
    # re_path(r'^(?P<category_slug>[-\w]+)/(?P<post_id>\d+)/$', views.detail, name="detail"), 
    re_path(r'^(?P<category_slug>[-\w]+)/(?P<pk>\d+)/$', views.PostCountHitDetailView.as_view(), name="detail"),

    # investment/1/edit
    path("<int:post_id>/edit/", views.edit, name='edit'),

    # investment/1/delete
    path("<int:post_id>/delete/", views.delete, name='delete'),
]
