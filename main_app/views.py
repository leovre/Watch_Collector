from django.shortcuts import render

watches = [
    {'brand': 'Rolex', 'name': 'submariner', 'manufactured': 2005,
        'img': 'https://imageio.forbes.com/b-i-forbesimg/arieladams/files/2013/09/Rolex-SUBMARINER-NoDATE-047.jpg?format=jpg&width=400'},
    {'brand': 'Casio', 'name': 'Vintage', 'manufactured': 2012,
        'img': 'https://www.mastersintime.com/pictures/casio-classic-edgy-a700wem-7aef-10482584.jpg'},
    {'brand': 'G-Shock', 'name': 'CasiOak', 'manufactured': 2008,
        'img': 'https://wornandwound.com/library/uploads/2022/08/GM-B2100D-1A_front-scaled.jpg'}

]

# Create your views here.


def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')


def watches_index(request):
    return render(request, 'watches/index.html', {
        'watches': watches
    })
