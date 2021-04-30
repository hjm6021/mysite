from django.urls import path
from investment import views

app_name = "investment"
urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
]
