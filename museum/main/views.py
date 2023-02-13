from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


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


def credits_p(request):
    return render(request, 'main/credits.html')


def copyright_p(request):
    return render(request, 'main/copyright.html')


def contact(request):
    return render(request, 'main/contact.html')


class AuthorList(ListView):
    model = Author
    template_name = 'author_list.html'
    context_object_name = 'authors'

    def get_queryset(self):
        return Author.objects.all().order_by('name')


class AssociationList(ListView):
    model = Education
    template_name = 'association_list.html'
    context_object_name = 'association'

    def get_queryset(self):
        return Association.objects.all().order_by('name')


class EducationList(ListView):
    model = Education
    template_name = 'education_list.html'
    context_object_name = 'education'

    def get_queryset(self):
        return Education.objects.all().order_by('name')


class InstitutionList(ListView):
    model = Education
    template_name = 'institution_list.html'
    context_object_name = 'institution'

    def get_queryset(self):
        return Institution.objects.all().order_by('name')


def get_pk(queryset):
    list_of_pk = []
    for query in queryset:
        list_of_pk.append(query.pk)
    return list_of_pk


def author_detail(request, pk):
    template_name = 'main/author_detail.html'
    author = Author.objects.get(pk=pk)
    exhibition = Exhibition.objects.filter(author__pk=pk)
    exhib_photo = ExhibitionPhoto.objects.filter(exhibition__pk__in=get_pk(exhibition))

    context = {'author': author, 'exhib': exhibition, 'photo': exhib_photo}

    return render(request, template_name, context)


def exhibition_detail(request, pk):
    template_name = 'main/exhibition_detail.html'
    exhibition = Exhibition.objects.get(pk=pk)
    exhib_photo = ExhibitionPhoto.objects.filter(exhibition=pk)

    context = {'exhib': exhibition, 'photo': exhib_photo}

    return render(request, template_name, context)
