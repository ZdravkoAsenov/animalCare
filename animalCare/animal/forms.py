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


class DeleteAnimalForm(BaseAnimalForm):
    class Meta:
        model = Animal
        fields = []

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance


def get_free_hours(date):
    available_hours = [hour for hour in range(9, 19)
                       if hour != 12 and not SavedAnimal.objects.filter(review_date=date, review_hour=hour).exists()]
    return available_hours


class SavedAnimalForm(forms.ModelForm):
    class Meta:
        model = SavedAnimal
        fields = ['review_date', 'review_hour', 'review_type', 'description']

        widgets = {
            'review_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_review_hour(self):
        review_date = self.cleaned_data.get('review_date')
        review_hour = self.cleaned_data.get('review_hour')

        existing_reviews = SavedAnimal.objects.filter(
            review_date=review_date,
            review_hour=review_hour,
        )

        available_hours = get_free_hours(review_date)

        if existing_reviews.exists():
            raise forms.ValidationError(
                f"The selected hour ({review_hour}) is already booked for this date. "
                f"Available hours for {review_date} are: {', '.join(map(str, available_hours))}."
            )

        if not review_hour:
            raise forms.ValidationError("Select hour for review.")

        return review_hour

    def clean_review_date(self):
        review_date = self.cleaned_data.get('review_date')
        if review_date:
            if review_date.weekday() in [5, 6]:
                raise forms.ValidationError("You cannot book on weekends (Saturday or Sunday).")

            if review_date < datetime.date.today():
                raise forms.ValidationError("You cannot book a past date for review.")

            reservations_count = SavedAnimal.objects.filter(review_date=review_date).count()
            if reservations_count >= 9:
                raise forms.ValidationError("The maximum number of reservations for this date has been reached."
                                            "Please choose another date.")
        return review_date


class EditSaveAnimalForm(SavedAnimalForm):
    pass
