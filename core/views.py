from django.shortcuts import render
from core.forms import ContactForm
from core.models import Contact

# Create your views here.

def index(request):
    context = {
        'form': ContactForm(),
    }
    return render(request, 'index.html', context)


def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            contact = form.save()
            context = {'contact': contact}
            return render(request, 'partials/contact.html', context)
    return render(request, 'partials/form.html', {'form': ContactForm()})
