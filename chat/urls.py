from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse_lazy


app_name = 'chat'
urlpatterns = [
    path('chat/video_call/', views.video_call, name='video_call'),
    path('chat/voice_call/', views.voice_call, name='voice_call'),


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
