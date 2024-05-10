from django.shortcuts import render
from .models import Film

# Create your views here.
def index(request):

    queryset = Film.objects.all()

    context = {
        'queryset': queryset
    }

    return render(request, 'index.html', context)
