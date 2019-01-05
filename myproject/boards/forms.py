from django import forms
from django.views.i18n import null_javascript_catalog

from .models import Question,Answer

from django.contrib.auth.models import User
class NewQuestionForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(), max_length=400)
    content = forms.CharField(widget=forms.Textarea(), max_length=4000)





    class Meta:
        model = Question
        fields = ['title', 'content']

class NewAnswerForm(forms.ModelForm):

            content = forms.CharField(widget=forms.Textarea(), max_length=4000)

            class Meta:
                model = Answer
                fields = ['content']

