import django_filters
from django import forms

from .models import *


class ProductFilter(django_filters.FilterSet):
    brand = django_filters.ModelMultipleChoiceFilter(queryset=Brand.objects.all(), widget=forms.CheckboxSelectMultiple)
    type = django_filters.ModelMultipleChoiceFilter(queryset=Type.objects.all(), widget=forms.CheckboxSelectMultiple)
    application = django_filters.ModelMultipleChoiceFilter(queryset=Application.objects.all(), widget=forms.CheckboxSelectMultiple)
    industry = django_filters.ModelMultipleChoiceFilter(queryset=Industry.objects.all(), widget=forms.CheckboxSelectMultiple)

    # class Meta:
    #     model = Product
    #     fields = ['type', 'brand', 'application', 'industry']
