from django.shortcuts import render
from .models import Track

def index(request):
    tracks = Track.objects.all()
    
    context = {
        'welcome_title': 'Добро пожаловать в BeatBattle',
        'welcome_text': 'Твой слух — твоё оружие. Готов к битве?',
        'tracks': tracks
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')