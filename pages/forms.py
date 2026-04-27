from django import forms
from .models import Track

class FeedbackForm(forms.Form):
    subject = forms.CharField(
        label='Тема',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тема сообщения'})
    )
    email = forms.EmailField(
        label='Ваш Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'})
    )
    text = forms.CharField(
        label='Сообщение',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Ваш вопрос или предложение...'})
    )

class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['title', 'artist']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название трека'}),
            'artist': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Исполнитель'}),
        }