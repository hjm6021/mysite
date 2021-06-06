from django.urls import path, re_path
from medicine import views

app_name = "medicine"
urlpatterns = [
    # investment/
    path('', views.index, name="index"),
    path('take/', views.take, name="take")
]
