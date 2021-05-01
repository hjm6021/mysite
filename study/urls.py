from django.urls import path
from study import views

app_name = "study"
urlpatterns = [
    # study/
    path('', views.index, name="index"),

    # study/1
    path('<int:category_id>/', views.list, name="list")
]
