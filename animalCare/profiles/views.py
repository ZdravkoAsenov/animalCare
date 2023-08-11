from django.contrib import messages
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from profiles.forms import CustomUserCreationForm, EditProfileForm, DeleteProfileForm
from profiles.models import ProfileModel, CustomUser


class ProfileCreateView(CreateView):
    template_name = 'profiles/create-profile.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "profiles/login.html"

    def get_success_url(self):
        return reverse_lazy('home page')


@login_required
def logout_view(request):
    logout(request)
    return redirect('home page')


@login_required
def profile_detail(request, user_pk):
    profile = ProfileModel.objects.get(pk=user_pk)

    context = {
        'profile': profile
    }

    return render(request, 'profiles/detail_profile.html', context=context)


@login_required
def profile_edit(request):
    profile = ProfileModel.objects.get(profile=request.user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('detail profile', user_pk=request.user.pk)
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
        'user': request.user
    }

    return render(request, 'profiles/edit_profile.html', context=context)


@login_required()
def profile_delete(request):
    user_model = get_user_model()

    user = user_model.objects.get(pk=request.user.pk)

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteProfileForm()

    context = {
        'form': form,
        'user': user
    }

    return render(request, 'profiles/delete_profile.html', context=context)
