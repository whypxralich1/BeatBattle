from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

from .models import Track, Tag, Comment
from .forms import TrackForm, CommentForm


class HomeView(ListView):
    model = Track
    template_name = 'index.html'
    context_object_name = 'tracks'
    ordering = ['-id']


class TrackDetailView(DetailView):
    model = Track
    template_name = 'track_detail.html'
    context_object_name = 'track'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class TrackCreateView(LoginRequiredMixin, CreateView):
    model = Track
    form_class = TrackForm
    template_name = 'track_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user

        messages.success(
            self.request,
            'Трек успешно добавлен!'
        )

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'track_detail',
            kwargs={'pk': self.object.pk}
        )


class TrackUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    UpdateView
):
    model = Track
    form_class = TrackForm
    template_name = 'track_form.html'

    def test_func(self):
        track = self.get_object()
        return track.author == self.request.user

    def get_success_url(self):
        return reverse_lazy(
            'track_detail',
            kwargs={'pk': self.object.pk}
        )


class TrackDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView
):
    model = Track
    template_name = 'track_confirm_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        track = self.get_object()
        return track.author == self.request.user


def about(request):
    return render(request, 'about.html')


def contact_view(request):
    return render(request, 'contact.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(
                request,
                'Регистрация прошла успешно!'
            )

            return redirect('home')

        messages.error(
            request,
            'Ошибка регистрации.'
        )

    else:
        form = UserCreationForm()

    return render(
        request,
        'registration/register.html',
        {'form': form}
    )


def tracks_by_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)

    tracks = tag.tracks.all()

    return render(
        request,
        'index.html',
        {
            'tracks': tracks,
            'selected_tag': tag
        }
    )


def add_comment(request, pk):
    track = get_object_or_404(
        Track,
        pk=pk
    )

    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)

        comment.track = track
        comment.author = request.user

        comment.save()

        messages.success(
            request,
            'Комментарий успешно добавлен!'
        )

    else:
        messages.error(
            request,
            'Ошибка при добавлении комментария.'
        )

    return redirect(
        'track_detail',
        pk=pk
    )