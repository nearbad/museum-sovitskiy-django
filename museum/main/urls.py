from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('museum_of_Nukus/', nks_museum, name='nks_museum'),
    path('collections/', collections, name='collections'),
    path('sources/', sources, name='sources'),
    path('catalogue/', catalogue, name='catalogue'),
    path('credits/', credits_p, name='credits'),
    path('copyright/', copyright_p, name='copyright'),
    path('contact/', contact, name='contact'),
    path('authors/', AuthorList.as_view(), name='author_list'),
    path('association/', AssociationList.as_view(), name='association_list'),
    path('education/', EducationList.as_view(), name='education_list'),
    path('institution/', InstitutionList.as_view(), name='institution_list'),
    path('author/<int:pk>', author_detail, name='author_detail'),
    path('exhibit/<int:pk>', exhibition_detail, name='exhibition_detail'),
]