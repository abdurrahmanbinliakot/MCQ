from django import forms
from django_quill.forms import QuillFormField



from django import forms
from .models import Articless

from ckeditor.widgets import CKEditorWidget



class MyForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Articless
        fields = '__all__'


# from ckeditor.widgets import CKEditorWidget

# class MyForm(forms.Form):
#     content = forms.CharField(widget=CKEditorWidget())


class add_new_class(forms.Form):
    class_name = forms.CharField(label="Type a new class name: ",widget=forms.TextInput(attrs={
        # 'size': '40',
         'class': 'new_class',
         'placeholder':"Type a new class name.... ",
         'tabindex':1,
         'autocomplete': 'off'
         }))
class add_subject_name(forms.Form):
    subject_name = forms.CharField(label="Type a new subject name: ",widget=forms.TextInput(attrs={
        # 'size': '40',
         'class': 'subject_name',
         'placeholder':"Type a new subject name.... ",
         'tabindex':1,
         'autocomplete': 'off'
         }))
class add_chapter_name(forms.Form):
    chapter_name = forms.CharField(label="Type a new chapter name: ",widget=forms.TextInput(attrs={
        # 'size': '40',
         'class': 'chapter_name',
         'placeholder':"Type a new chapter name.... ",
         'tabindex':1,
         'autocomplete': 'off'
         }))

class add_mcq_form(forms.Form):
    # mcq_question = content = QuillFormField()
    mcq_question = forms.CharField(label="Type MCQ",widget=forms.Textarea(attrs={
        # 'size': '40',
         'class': 'mcq_question',
         'placeholder':"Type MCQ question here....",
         'tabindex':1,
         'autocomplete': 'off'
         }))
    option_a = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'option_a',
         'placeholder':"Type Option (A) here....",
         'tabindex':2,
         'autocomplete': 'off'
    }))
    option_b = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'option_b',
         'placeholder':"Type Option (B) here....",
         'tabindex':3,
         'autocomplete': 'off'
    }))
    option_c = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'option_c',
         'placeholder':"Type Option (C) here....",
         'tabindex':4,
         'autocomplete': 'off'
    }))
    option_d = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'option_d',
         'placeholder':"Type Option (D) here....",
         'tabindex':5,
         'autocomplete': 'off'
    }))
