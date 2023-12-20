from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    commenter = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control mb-2',
        'placeholder':'Your name'
    }))
    body = forms.CharField(max_length=100, widget=forms.Textarea(attrs={
        'class': 'form-control mb-3',
        'placeholder':'Comment here',
        'rows': 3
    }))
    class Meta:
        model = Comment
        fields = ['commenter','body']