from django import forms
from .models import User, Note, Category
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('category', 'name', 'author', 'note', 'image')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('note_category', 'author')

