from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Watch


# Create your views here.


def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')


def watches_index(request):
    watches = Watch.objects.all()
    return render(request, 'watches/index.html', {
        'watches': watches
    })


def watches_detail(request, watch_id):
    watch = Watch.objects.get(id=watch_id)
    return render(request, 'watches/detail.html', {'watch': watch})


def bands(request):
    return render(request, 'bands/index.html')


class WatchCreate(CreateView):
    model = Watch
    fields = "__all__"
    success_url = '/watches'
