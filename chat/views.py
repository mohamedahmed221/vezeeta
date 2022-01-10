from django.shortcuts import render

# Create your views here.


def video_call(request):
    return render(request, "chat/video-call.html")


def voice_call(request):
    return render(request, "chat/voice-call.html")
