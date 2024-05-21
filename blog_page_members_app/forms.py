from django import forms
from .models import *

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'thumbnail', 'featured']   

