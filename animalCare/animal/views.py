from django.contrib.auth.decorators import login_required
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic as view

from animal.forms import CreateAnimalForm, EditAnimalForm, SavedAnimalForm
from animal.models import Animal, SavedAnimal


class CreateAnimalView(view.CreateView):
    model = Animal
    form_class = CreateAnimalForm
    template_name = 'animal/animal_create.html'
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class AnimalListView(view.ListView):
    model = Animal
    template_name = 'animal/animal_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset


class AnimalEditView(view.UpdateView):
    model = Animal
    form_class = EditAnimalForm
    template_name = 'animal/animal_edit.html'
    success_url = reverse_lazy('list animal')


class AnimalDetailView(view.DetailView):
    model = Animal
    template_name = 'animal/animal_detail.html'
    context_object_name = 'animal'


def delete_animal(request, pk):
    animal = get_object_or_404(Animal, pk=pk)

    if request.method == 'POST':
        animal.delete()
        return redirect('list animal')

    return render(request, 'animal/animal_delete.html', {'animal': animal})


@login_required
def animal_save_hour(request, animal_pk):
    animal = get_object_or_404(Animal, id=animal_pk)

    if request.method == 'POST':
        form = SavedAnimalForm(request.POST)
        if form.is_valid():
            review_date = form.cleaned_data['review_date']
            description = form.cleaned_data['description']
            saved_animal, created = SavedAnimal.objects.get_or_create(
                user=request.user, animal=animal, review_date=review_date, description=description
            )
            if created:
                pass
            return redirect('detail animal', pk=animal.id)
    else:
        form = SavedAnimalForm()

    context = {
        'animal': animal,
        'form': form
    }

    return render(request, 'animal/animal_saved_hour.html', context=context)


class SavedAnimalListView(auth_mixins.LoginRequiredMixin, view.ListView):
    model = SavedAnimal
    template_name = 'animal/saved_animal_detail.html'
    context_object_name = 'saved_animals'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = SavedAnimal.objects.filter(user=self.request.user)
        return queryset
