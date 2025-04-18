from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .models import Album, Photo
from .forms import UserRegistrationForm
from django.contrib.auth.views import LoginView as AuthLoginView

class HomeView(TemplateView):
    template_name = 'albums/home.html'

class AlbumListView(LoginRequiredMixin, ListView):
    model = Album
    template_name = 'albums/album_list.html'
    
    def get_queryset(self):
        return Album.objects.filter(created_by=self.request.user)

class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    fields = ['title', 'description']
    template_name = 'albums/album_form.html'
    success_url = reverse_lazy('album-list')
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class AlbumDetailView(LoginRequiredMixin, DetailView):
    model = Album
    template_name = 'albums/album_detail.html'

class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    model = Album
    fields = ['title', 'description']
    template_name = 'albums/album_form.html'
    success_url = reverse_lazy('album-list')

class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = Album
    template_name = 'albums/album_confirm_delete.html'
    success_url = reverse_lazy('album-list')

class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['image', 'caption']
    template_name = 'albums/photo_form.html'
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'accept': 'image/*',
            'required': True
        })
        form.fields['caption'].widget.attrs.update({'class': 'form-control'})
        return form
    
    def form_valid(self, form):
        album = Album.objects.get(pk=self.kwargs['pk'])
        if album.created_by != self.request.user:
            return self.handle_no_permission()
        form.instance.album = album
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('album-detail', kwargs={'pk': self.kwargs['pk']})

class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    template_name = 'albums/photo_confirm_delete.html'
    
    def get_queryset(self):
        # Only allow deleting photos from user's own albums
        return Photo.objects.filter(album__created_by=self.request.user)
    
    def get_success_url(self):
        return reverse_lazy('album-detail', kwargs={'pk': self.object.album.pk})

@method_decorator(csrf_exempt, name='dispatch')
class PhotoCaptionUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['caption']
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.album.created_by != self.request.user:
            return self.handle_no_permission()
        
        data = json.loads(request.body)
        self.object.caption = data.get('caption', '')
        self.object.save()
        
        return JsonResponse({
            'status': 'success',
            'caption': self.object.caption
        })

class AlbumPhotosView(LoginRequiredMixin, View):
    def get(self, request, pk):
        album = get_object_or_404(Album, pk=pk, created_by=request.user)
        photos = [{
            'id': photo.id,
            'image': photo.image.url,
            'caption': photo.caption
        } for photo in album.photos.all()]
        return JsonResponse({'photos': photos})

class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Registration successful. Please login.')
        return response
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_flipped'] = 'flip' in self.request.GET
        return context

def custom_logout(request):
    logout(request)
    return redirect('home')

class LoginView(AuthLoginView):
    template_name = 'registration/login.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_flipped'] = 'flip' in self.request.GET
        return context