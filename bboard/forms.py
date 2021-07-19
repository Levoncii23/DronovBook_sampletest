from django.forms import ModelForm, fields

from .models import Bb

class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric')