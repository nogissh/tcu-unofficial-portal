from django.shortcuts import render
from app.models import Post
import datetime


def Index(request):
  """
  トップページ
  """

  # 掲載期間中のイベントを抽出
  today = datetime.date.today()
  posts = Post.objects.filter(term_start__lte=today, term_end__gte=today)

  # ページ番号を定義
  page = request.GET.get('page', None)
  if page is None:
    page = 1
  try:
    page = int(page)
    if page <= 0:
      page = 1
  except:
    page = 1

  # 表示するイベントを抽出
  start_num = (page - 1) * 15
  detail = [{
    'id'   : post.id,
    'title': post.title,
    'text' : post.text
  } for post in posts[start_num:start_num + 15]]

  # テンプレートに送るオブジェクト
  contents = {
    'events'       : detail,
    'page_forward' : page + 1,
    'page_backword': page - 1
  }

  return render(request, 'app/index.html', contents)
