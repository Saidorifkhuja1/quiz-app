from django import forms

from .models import Quiz

# forms.py

from django import forms
from .models import Exam, Quiz

class ExamUploadForm(forms.Form):
    exam_file = forms.FileField(label='Upload Exam File', help_text='Supported file types: PDF, DOCX')

class QuizCreationForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['question', 'option1', 'option2', 'option3', 'option4', 'correct_option']

class QuizResponseForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['user_response']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_response'].label = ''

    user_response = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


