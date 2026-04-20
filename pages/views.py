from django.shortcuts import render

def index(request):
    context = {
        'welcome_title': 'Добро пожаловать в BeatBattle',
        'welcome_text': 'Твой слух — твоё оружие. Готов к битве?'
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')