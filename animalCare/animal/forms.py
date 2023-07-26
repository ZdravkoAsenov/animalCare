import datetime

from django import forms

from animal.models import Animal, SavedAnimal


class BaseAnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        exclude = ['owner', 'medical_history']


class CreateAnimalForm(BaseAnimalForm):
    pass


class EditAnimalForm(BaseAnimalForm):
    pass


class SavedAnimalForm(forms.ModelForm):
    class Meta:
        model = SavedAnimal
        fields = ['review_date', 'description']

        widgets = {
            'review_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_review_date(self):
        review_date = self.cleaned_data.get('review_date')
        if review_date:
            # Check if the selected date is a weekend (Saturday or Sunday)
            if review_date.weekday() in [5, 6]:  # 5: Saturday, 6: Sunday
                raise forms.ValidationError("You cannot book on weekends (Saturday or Sunday).")

            # Check if the selected date is in the past
            if review_date < datetime.date.today():
                raise forms.ValidationError("You cannot book a past date for review.")

            reservations_count = SavedAnimal.objects.filter(review_date=review_date).count()
            if reservations_count >= 8:
                raise forms.ValidationError("The maximum number of reservations for this date has been reached. "
                                            "Please choose another date.")
        return review_date



