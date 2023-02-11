from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def nks_museum(request):
    return render(request, 'main/nks_museum.html')


def collections(request):
    return render(request, 'main/collections.html')


def sources(request):
    return render(request, 'main/sources.html')


def catalogue(request):
    return render(request, 'main/catalogue.html')


def credits(request):
    return render(request, 'main/credits.html')


def copyright(request):
    return render(request, 'main/copyright.html')


def contact(request):
    return render(request, 'main/contact.html')