from django.urls import path
from study import views

app_name = "study"
urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
]
