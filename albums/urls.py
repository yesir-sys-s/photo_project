from django.urls import path
from .views import (
    HomeView, AlbumListView, AlbumCreateView, AlbumDetailView,
    AlbumUpdateView, AlbumDeleteView, PhotoCreateView,
    PhotoDeleteView, RegisterView, custom_logout, PhotoCaptionUpdateView, 
    AlbumPhotosView, LoginView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('albums/', AlbumListView.as_view(), name='album-list'),
    path('albums/new/', AlbumCreateView.as_view(), name='album-create'),
    path('albums/<int:pk>/', AlbumDetailView.as_view(), name='album-detail'),
    path('albums/<int:pk>/update/', AlbumUpdateView.as_view(), name='album-update'),
    path('albums/<int:pk>/delete/', AlbumDeleteView.as_view(), name='album-delete'),
    path('albums/<int:pk>/add-photo/', PhotoCreateView.as_view(), name='photo-create'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo-delete'),
    path('photo/<int:pk>/update-caption/', PhotoCaptionUpdateView.as_view(), name='photo-update-caption'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', custom_logout, name='logout'),
    path('albums/<int:pk>/photos/', AlbumPhotosView.as_view(), name='album-photos'),
]