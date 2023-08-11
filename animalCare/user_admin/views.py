from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import render, redirect
from django.views import generic as view

from animal.models import Animal, MedicalExamination
from contacts.models import Contact
from profiles.models import ProfileModel


@user_passes_test(lambda user: user.groups.filter(name='Staff').exists())
def home_administration(request):
    return render(request, 'administration/home_administration.html')


@user_passes_test(lambda user: user.groups.filter(name='Staff').exists())
def user_list(request):
    userModel = get_user_model()
    users = userModel.objects.all()
    context = {'users': users}
    return render(request, 'administration/admin_user_list.html', context)


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


@user_passes_test(lambda user: user.groups.filter(name='Staff').exists())
def unanswered_contacts(request):
    unanswered_inquiries = Contact.objects.filter(is_answered=False)
    context = {
        'unanswered_inquiries': unanswered_inquiries
    }
    return render(request, 'administration/unanswered_inquiries.html', context)


@user_passes_test(lambda user: user.groups.filter(name='Staff').exists())
def mark_contact_answered(request, pk):
    inquiries = Contact.objects.get(pk=pk)
    inquiries.is_answered = True
    inquiries.save()
    return redirect('unanswered inquiries')


@user_passes_test(lambda user: user.groups.filter(name='Staff').exists())
def answered_contacts(request):
    answered_inquiries = Contact.objects.filter(is_answered=True)
    context = {
        'answered_inquiries': answered_inquiries
    }
    return render(request, 'administration/answered_inquiries.html', context)