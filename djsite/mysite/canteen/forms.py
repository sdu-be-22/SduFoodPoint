from .models import *

from django.forms import *


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['photo', 'user', 'comment']
        widgets = {
            "user": TextInput(attrs={'class': 'form-control','placeholder': 'Name'}),
            "comment": Textarea(attrs={'class': 'form-control','placeholder': 'Comments'

            })

        }


class UserRegisterForm:
    pass