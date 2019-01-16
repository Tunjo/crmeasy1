from django import forms

from .models import ItemStorage


class ItemForm(forms.ModelForm):
    class Meta:
        model = ItemStorage
        fields = ('name', 'disc', 'choice')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'disc': forms.Textarea(attrs={'placeholder': 'Description'}),
            'choice': forms.Select(attrs={'placeholder': 'Select'})
        }
