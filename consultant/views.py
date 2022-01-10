from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Appointments, AvailableDate, AvailableTimings
from datetime import datetime, date, time, timedelta
from django.http import JsonResponse, request
from django.contrib import messages
from django.contrib.auth.models import User
from accounts.models import Profile

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


def consultant_profile(request, name):
    profile = Profile.objects.get(user__username=name).status
    context = None
    if profile == "consultant":
        consultant_detail = get_object_or_404(Profile, user__username=name)
        context = {
            "consultant_detail": consultant_detail,
        }
    else:
        messages.warning(
            request, 'You do not have permissions to access this page !')
    return render(request, "consultant/consultant-profile.html", context)
