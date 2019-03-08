from django import forms
from .models import Post,Tag
from django.contrib.auth.models import User

'''
投稿
'''
class Contribution(forms.Form):
    title     = forms.CharField(label='タイトル',required=True,max_length=128)
    text      = forms.CharField(label='本文',required=False,max_length=1024,widget=forms.Textarea)
    term_start  = forms.DateTimeField(label='掲示開始日',required=True,widget=forms.DateInput(attrs={"type": "date"}))
    term_end    = forms.DateTimeField(label='掲示終了日',required=True,widget=forms.DateInput(attrs={"type": "date"}),)
    user        = forms.ModelChoiceField(label='名前',required=True,queryset=User.objects.all())
