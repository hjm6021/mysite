from django import forms
from .models import Post, Category
from ckeditor_uploader.widgets import CKEditorWidget, CKEditorUploadingWidget

class PostForm(forms.Form):
    title = forms.CharField(widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': '80', 'rows': '3'}))
    content = forms.CharField(widget = CKEditorUploadingWidget())
