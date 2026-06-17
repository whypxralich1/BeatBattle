from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.HomeView.as_view(), name='home'),

    path('track/<int:pk>/', views.TrackDetailView.as_view(), name='track_detail'),
    path('track/add/', views.TrackCreateView.as_view(), name='track_create'),
    path('track/<int:pk>/edit/', views.TrackUpdateView.as_view(), name='track_update'),
    path('track/<int:pk>/delete/', views.TrackDeleteView.as_view(), name='track_delete'),
    path('track/<int:pk>/comment/', views.add_comment, name='add_comment'),

    path('tag/<int:tag_id>/', views.tracks_by_tag, name='tracks_by_tag'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact_view, name='contact'),

    path('accounts/register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)