from django.urls import path
from . import views_toppage

app_name = 'app'
urlpatterns = [
  path('home/', views_toppage.Index)
]
