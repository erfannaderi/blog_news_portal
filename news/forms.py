from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from news.models import CommentsModel


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


class CommentsForm(forms.ModelForm):

    class Meta:
        model = CommentsModel
        fields = ('comment',)
        widgets = {
            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your comment here',
                    'rows': 4,  # Set the number of visible text lines
                    'cols': 50,  # Set the visible width of the text area
                    'style': 'resize: vertical;',  # Allow vertical resizing of the text area
                    'autofocus': True,  # Automatically focus on the comment field when the page loads
                    'autocomplete': 'on',  # Enable browser autocomplete for the comment field
                    'spellcheck': True,  # Enable spell checking for the comment field
                }
            ),
        }


