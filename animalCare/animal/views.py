from django.contrib.auth.decorators import login_required
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic as view

from animal.decorators import allowed_groups
from animal.forms import CreateAnimalForm, EditAnimalForm, SavedAnimalForm, EditSaveAnimalForm, \
    DeleteAnimalForm, ExaminationForm
from animal.models import Animal, SavedAnimal, MedicalExamination
from core.mixins import AllowedGroups


class CreateAnimalView(auth_mixins.LoginRequiredMixin, view.CreateView):
    model = Animal
    form_class = CreateAnimalForm
    template_name = 'animal/animal_create.html'
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class AnimalListView(auth_mixins.LoginRequiredMixin, view.ListView):
    model = Animal
    template_name = 'animal/animal_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset


class AnimalEditView(auth_mixins.LoginRequiredMixin, view.UpdateView):
    model = Animal
    form_class = EditAnimalForm
    template_name = 'animal/animal_edit.html'
    success_url = reverse_lazy('list animal')


class AnimalDetailView(auth_mixins.LoginRequiredMixin, view.DetailView):
    model = Animal
    template_name = 'animal/animal_detail.html'
    context_object_name = 'animal'


@login_required()
def delete_animal(request, pk):
    animal = get_object_or_404(Animal, pk=pk)

    if request.method == 'POST':
        form = DeleteAnimalForm(request.POST, instance=animal)
        form.save()
        return redirect('list animal')
    else:
        form = DeleteAnimalForm(instance=animal)

    context = {
        'animal': animal,
        'form': form,
    }

    return render(request, 'animal/animal_delete.html', context=context)


@login_required
def animal_save_hour(request, animal_pk):
    animal = get_object_or_404(Animal, id=animal_pk)

    if request.method == 'POST':
        form = SavedAnimalForm(request.POST)
        if form.is_valid():
            review_date = form.cleaned_data['review_date']
            description = form.cleaned_data['description']
            review_hour = form.cleaned_data['review_hour']
            review_type = form.cleaned_data['review_type']
            saved_animal, created = SavedAnimal.objects.get_or_create(
                user=request.user,
                animal=animal,
                review_date=review_date,
                description=description,
                review_hour=review_hour,
                review_type=review_type,
            )
            return redirect('saved animal hour detail')
    else:
        form = SavedAnimalForm()

    context = {
        'animal': animal,
        'form': form
    }

    return render(request, 'animal/record_animal_hour.html', context=context)


class SavedAnimalListView(auth_mixins.LoginRequiredMixin, view.ListView):
    model = SavedAnimal
    template_name = 'animal/record_animal_detail.html'
    context_object_name = 'saved_animals'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = SavedAnimal.objects.filter(user=self.request.user)
        return queryset


class EditSavedAnimalView(auth_mixins.LoginRequiredMixin, view.UpdateView):
    model = SavedAnimal
    form_class = EditSaveAnimalForm
    template_name = 'animal/record_hour_edit.html'
    success_url = reverse_lazy('saved animal hour detail')

    def get_object(self, queryset=None):
        animal_pk = self.kwargs.get('animal_pk')
        return get_object_or_404(SavedAnimal, id=animal_pk)


class SavedAnimalDeleteView(auth_mixins.LoginRequiredMixin, view.DeleteView):
    model = SavedAnimal
    template_name = 'animal/record_animal_hour_delete.html'
    success_url = reverse_lazy('saved animal hour detail')

    def get_object(self, queryset=None):
        animal_pk = self.kwargs.get('animal_pk')
        return get_object_or_404(SavedAnimal, id=animal_pk)


@login_required()
@allowed_groups(['Vet'])
def examination_list(request):
    selected_date = request.GET.get('date')  # Get the selected date from query parameters

    if selected_date:
        selected_date = timezone.datetime.strptime(selected_date, '%Y-%m-%d').date()  # Convert the string date to a date object

        saved_animals = SavedAnimal.objects.filter(review_date=selected_date)
    else:
        today = timezone.localdate()  # Get the current date
        saved_animals = SavedAnimal.objects.filter(review_date=today)

    context = {
        'saved_animals': saved_animals,
    }

    return render(request, 'animal/examination_list.html', context=context)


class AddExamination(auth_mixins.LoginRequiredMixin, auth_mixins.UserPassesTestMixin, view.CreateView):
    model = MedicalExamination
    form_class = ExaminationForm
    template_name = 'animal/add_examination.html'
    success_url = reverse_lazy('list examination')

    def get_form_kwargs(self):
        kwargs = super(AddExamination, self).get_form_kwargs()
        saved_animal = get_object_or_404(SavedAnimal, user_id=self.kwargs['user_pk'],
                                         animal_id=self.kwargs['animal_pk'])
        kwargs['instance'] = MedicalExamination(user=saved_animal.user, animal=saved_animal.animal)
        return kwargs

    def test_func(self):
        user = self.request.user
        return user.groups.filter(name='Vet').exists()


@login_required()
def user_examinations(request):
    examinations = MedicalExamination.objects.filter(user=request.user)

    context = {
        'examinations': examinations
    }

    return render(request, 'animal/user_examinations.html', context=context)
