from django.db.models import Q
from django.shortcuts import render, redirect
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
    exhibitions = author.exhibitions.select_related('author').prefetch_related('photos')
    context = {
        'author': author,
        'exhibitions': exhibitions
    }
    return render(request, template_name, context)


def exhibition_detail(request, pk):
    template_name = 'main/exhibition_detail.html'
    exhibition = Exhibition.objects.get(pk=pk)
    exhib_photo = ExhibitionPhoto.objects.filter(exhibition=pk)

    context = {'exhib': exhibition, 'photo': exhib_photo}

    return render(request, template_name, context)


class AssociationDetail(DetailView):
    model = Association
    template_name = 'main/detail.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Author.objects.filter(association=self.object.pk)
        return context


class EducationDetail(DetailView):
    model = Education
    template_name = 'main/detail.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Author.objects.filter(education=self.object.pk)
        return context


class InstitutionDetail(DetailView):
    model = Institution
    template_name = 'main/detail.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Author.objects.filter(institution=self.object.pk)
        return context


class SearchView(ListView):
    model = Author
    template_name = 'main/search.html'
    context_object_name = 'authors'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Author.objects.filter(
            Q(name__icontains=query) | Q(bio__icontains=query)
        )
        return object_list


def set_theme(request):
    theme = request.GET.get('theme', None)
    if theme == 'dark':
        response = redirect(request.META.get('HTTP_REFERER'))
        response.set_cookie('theme', 'dark')
        return response
    elif theme == 'light':
        response = redirect(request.META.get('HTTP_REFERER'))
        response.delete_cookie('theme')
        return response
    else:
        return redirect(request.META.get('HTTP_REFERER'))
