from django.shortcuts import render
from core.forms import ContactForm
from core.models import Contact

# Create your views here.

def index(request):
    context = {
        'form': ContactForm(),
    }
    return render(request, 'index.html', context)
