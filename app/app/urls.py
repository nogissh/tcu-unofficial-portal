from django.urls import path
from . import views_toppage
from . import viewsikui

app_name = 'app'
urlpatterns = [
  path('home/', views_toppage.Index),
  path('post/home/', viewsikui.post_home),
  path('post/job/', viewsikui.post_job, name="post_job")
]
