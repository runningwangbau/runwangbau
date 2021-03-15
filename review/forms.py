from django import forms
from .models import Result



class AnswerForm(forms.Form):
    Answer_choice = ((1,'매우아니다'), (2,'아니다'), (3,'보통'), (4,'그렇다'), (5,'매우그렇다'))
    Name = forms.CharField(label='이름',required=False)
    Question = forms.IntegerField(label='질문1',required=False, widget=forms.RadioSelect(choices=Answer_choice))

class AnswerForm(forms.ModelForm):
    class Meta:
        model=Result
        fields=['Name','Question']

        def save(self, commit=True):
            post=Result(**self.cleaned_data)
            if commit:
                post.save()
            return post