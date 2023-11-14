from django.shortcuts import render, get_object_or_404
from .models import Film

# Create your views here.
def home(request):

    queryset = Film.objects.all().order_by('naziv')

    context = {
        'objects': queryset
    }

    return render(request, 'home.html', context)
