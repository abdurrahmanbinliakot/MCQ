from django.contrib import admin
from .models import MCQ,Class,Chapter,Subject,Articless


from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Articless
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(Articless, PostAdmin)
# Register your models here.

# admin.site.register(Articless)
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Chapter)
admin.site.register(MCQ)