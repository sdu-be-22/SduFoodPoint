from .models import *
from django.forms import *
from django import forms

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['photo', 'user', 'comment']
        widgets = {
            "user": TextInput(attrs={'class': 'form-control','placeholder': 'Name'}),
            "comment": Textarea(attrs={'class': 'form-control','placeholder': 'Comments'})

        }



class OnlineOrder(forms.Form):
    name = forms.CharField(label = "Name", max_length=200)
    check = forms.BooleanField()


