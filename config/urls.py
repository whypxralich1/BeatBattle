from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('track/<int:pk>/', views.track_detail, name='track_detail'),
    path('track/<int:pk>/edit/', views.track_update, name='track_update'),
    path('contact/', views.contact_view, name='contact'),
    path('track/add/', views.track_create, name='track_create'),
    path('tag/<int:tag_id>/', views.tracks_by_tag, name='tracks_by_tag'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)