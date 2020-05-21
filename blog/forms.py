from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
# class Meta, where we tell Django which model should be used to create this form (model = Post).
#  In this scenario we want only title and text to be exposed – author should be the person who is currently logged in (you!) and created_date 
