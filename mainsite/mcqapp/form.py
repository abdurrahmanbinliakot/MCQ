from django import forms
from django_quill.forms import QuillFormField


class QuillFieldForm(forms.Form):
    content = QuillFormField()


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



class ContentEditableTextarea(forms.widgets.Widget):
    template_name = 'contenteditable_textarea.html'

    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.attrs['style'] = 'display: none;' # hide the textarea field

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['contenteditable_name'] = name # add the name to the context for the contenteditable div
        return context

class AddMCQForm(forms.Form):
    title=forms.CharField()
    mcq_question = forms.CharField(widget=ContentEditableTextarea(attrs={
        'class': 'mcq_question',
        'placeholder': 'Type MCQ question here....',
        'tabindex': 1,
        'required': True,
    }))

    def clean_mcq_question(self):
        contenteditable_name = self.fields['mcq_question'].widget.attrs['contenteditable_name']
        return self.cleaned_data[contenteditable_name]
   


class add_mcq_form(forms.Form):
    # mcq_question = content = QuillFormField()
    mcq_question = forms.CharField(widget=forms.Textarea(attrs={
        'contenteditable': 'true',
        "style":"display: none;",
        'class': 'mcq_question',
        'placeholder': 'Type MCQ question here....',
        'tabindex': '1',
        'required': True,
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
