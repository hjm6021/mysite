from django.urls import path, re_path
from study import views

app_name = "study"
urlpatterns = [
    # study/
    path('', views.index, name="index"),

    # study/add
    path("/add", views.add, name='add'),

    # study/edit/post_id
    path("/edit/<int:post_id>", views.edit, name='edit'),

    # study/delete/post_id
    path("/delete/<int:post_id>", views.delete, name='delete'),

    # study/python
    # path("<slug:category_slug>/", views.list, name="list"),
    re_path(r'^/(?P<category_slug>[-\w]+)$', views.list, name="list"), 

    # study/python/1
    # path("<slug:category_slug>/<int:post_id>/", views.detail, name='detail'),
    #re_path(r'^(?P<category_slug>[-\w]+)/(?P<post_id>\d+)/$', views.detail, name="detail"),
    re_path(r'^/(?P<category_slug>[-\w]+)/(?P<pk>\d+)$', views.PostCountHitDetailView.as_view(), name="detail"),
]
