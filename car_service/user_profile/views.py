from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .forms import UserUpdateForm, UserProfileUpdateForm


# Create your views here.

@csrf_protect
def register(request):
    return render(request, 'user_profile/register.html')


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, _("Profile updated succesfully"))
            return redirect(reverse_lazy('user_profile:profile'))
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'user_profile/profile.html', context)
