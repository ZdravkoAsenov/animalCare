from django.shortcuts import render, redirect

from contacts.forms import ContactForm


def contact_form_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = ContactForm()

    context = {
        'form': form
    }

    return render(request, 'contacts/contact_form.html', context=context)
