from django.urls import path
from investment import views

app_name = "investment"
urlpatterns = [
    # investment/
    path('', views.index, name="index"),
    # investment/1
    path('<int:category_id>/', views.list, name="list"),
]
