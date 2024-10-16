from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.DashboardAppClassView.as_view(), name="dashboard"),
]

