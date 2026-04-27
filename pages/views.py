from django.shortcuts import render, get_object_or_404, redirect
from .models import Track
from .forms import FeedbackForm, TrackForm

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

def track_detail(request, pk):
    track = get_object_or_404(Track, pk=pk)
    return render(request, 'track_detail.html', {'track': track})

def contact_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('home')
    else:
        form = FeedbackForm()
    return render(request, 'contact.html', {'form': form})

def track_create(request):
    if request.method == 'POST':
        form = TrackForm(request.POST)
        if form.is_valid():
            track = form.save()
            return redirect('track_detail', pk=track.pk)
    else:
        form = TrackForm()
    return render(request, 'track_form.html', {'form': form, 'title': 'Добавить новый трек'})

def track_update(request, pk):
    track = get_object_or_404(Track, pk=pk)
    if request.method == 'POST':
        form = TrackForm(request.POST, instance=track)
        if form.is_valid():
            form.save()
            return redirect('track_detail', pk=track.pk)
    else:
        form = TrackForm(instance=track)
    return render(request, 'track_form.html', {'form': form, 'title': 'Редактировать трек'})