from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Watch
from .forms import CleaningForm

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
    cleaning_form = CleaningForm()
    return render(request, 'watches/detail.html', {
        'watch': watch , 'cleaning_form' : cleaning_form})
    
def add_cleaning(request, watch_id):
    form = CleaningForm(request.POST)
    if form.is_valid():
        new_cleaning = form.save(commit=False)
        new_cleaning.watch_id = watch_id
        new_cleaning.save()
    return redirect('detail', watch_id = watch_id)

def bands(request):
    return render(request, 'bands/index.html')


class WatchCreate(CreateView):
    model = Watch
    fields = "__all__"
    success_url = '/watches'

class WatchUpdate(UpdateView):
    model = Watch
    fields = "__all__"

class WatchDelete(DeleteView):
    model = Watch
    success_url = '/watches'
    

