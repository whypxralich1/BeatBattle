from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Track, Tag
from .forms import TrackForm

def index(request):
    tracks = Track.objects.all()
    return render(request, 'index.html', {'tracks': tracks})

def about(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def track_detail(request, pk):
    track = get_object_or_404(Track, pk=pk)
    return render(request, 'track_detail.html', {'track': track})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def tracks_by_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    tracks = tag.tracks.all()
    return render(request, 'index.html', {'tracks': tracks, 'selected_tag': tag})

@login_required
def track_create(request):
    if request.method == 'POST':
        form = TrackForm(request.POST, request.FILES)
        if form.is_valid():
            track = form.save(commit=False)
            track.author = request.user
            track.save()
            form.save_m2m()
            return redirect('track_detail', pk=track.pk)
    else:
        form = TrackForm()
    return render(request, 'track_form.html', {'form': form, 'title': 'Добавить новый трек'})

@login_required
def track_update(request, pk):
    track = get_object_or_404(Track, pk=pk)
    if request.method == 'POST':
        form = TrackForm(request.POST, request.FILES, instance=track)
        if form.is_valid():
            form.save()
            return redirect('track_detail', pk=track.pk)
    else:
        form = TrackForm(instance=track)
    return render(request, 'track_form.html', {'form': form, 'title': 'Редактировать трек'})