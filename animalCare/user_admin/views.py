from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import render
from django.views import generic as view

from animal.models import Animal, MedicalExamination
from profiles.models import ProfileModel
from user_admin.forms import ChangeUserGroupForm


@user_passes_test(lambda user: user.groups.filter(name='Staff').exists())
def home_administration(request):
    return render(request, 'administration/home_administration.html')


@user_passes_test(lambda user: user.groups.filter(name='Staff').exists())
def user_list(request):
    userModel = get_user_model()

    current_user = request.user
    users = userModel.objects.exclude(id=current_user.id)

    if request.method == 'POST':
        form = ChangeUserGroupForm(request.POST)
        if form.is_valid():
            group = form.cleaned_data['group']
            user_id = request.POST.get('user_id')
            user = userModel.objects.get(pk=user_id)
            user.groups.clear()
            user.groups.add(group)
    else:
        form = ChangeUserGroupForm()

    context = {
        'users': users,
        'form': form
    }

    return render(request, 'administration/admin_user_list.html', context=context)


class AdminUserDetailView(auth_mixins.LoginRequiredMixin, auth_mixins.UserPassesTestMixin, view.DetailView):
    model = ProfileModel
    template_name = 'administration/admin_user_detail.html'

    def test_func(self):
        user = self.request.user
        return user.groups.filter(name='Staff').exists()


class AdminAnimalListView(auth_mixins.LoginRequiredMixin, auth_mixins.UserPassesTestMixin, view.ListView):
    model = Animal
    template_name = 'administration/admin_animal_list.html'

    def test_func(self):
        user = self.request.user
        return user.groups.filter(name='Staff').exists()


class AdminAnimalDetailView(auth_mixins.LoginRequiredMixin, auth_mixins.UserPassesTestMixin, view.DetailView):
    model = Animal
    template_name = 'administration/admin_animal_detail.html'

    def test_func(self):
        user = self.request.user
        return user.groups.filter(name='Staff').exists()


class AdminExaminationListView(auth_mixins.LoginRequiredMixin, auth_mixins.UserPassesTestMixin, view.ListView):
    model = MedicalExamination
    template_name = 'administration/admin_examination_list.html'

    def test_func(self):
        user = self.request.user
        return user.groups.filter(name='Staff').exists()


class AdminExaminationDetailView(auth_mixins.LoginRequiredMixin, auth_mixins.UserPassesTestMixin, view.DetailView):
    model = MedicalExamination
    template_name = 'administration/admin_examination_detail.html'

    def test_func(self):
        user = self.request.user
        return user.groups.filter(name='Staff').exists()
