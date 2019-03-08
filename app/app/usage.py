import datetime


def regist_post(request, Post, User):
    """
    データを登録する。
    """

    # Status
    status = False

    try:
        # 情報の整理
        title = request.POST['title']
        text = request.POST['text']
        date_update = datetime.datetime.now()
        term_start = request.POST['term_start']
        term_end = request.POST['term_end']
        user = User.objects.get(id=request.POST['user'])

        # データ登録
        contribution = Post(title=title,text=text,date_update=date_update,term_start=term_start,term_end=term_end,user=user)#,date_post=date_postdate_update=date_update,
        contribution.save()

        # 状態を変更
        status = True
    except:
        pass

    return status
