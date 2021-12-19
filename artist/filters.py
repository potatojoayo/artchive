from django.db.models import Q
from django_filters import rest_framework as filters
import django_filters
from .models import Artist


class ArtistFilter(filters.FilterSet):

    name = django_filters.CharFilter(
        method='search_by_name', label='search_by_name')

    class Meta:

        model = Artist
        fields = {
            "born": ['gte', 'range', 'exact', 'lte'],
            "died": ['gte', 'range', 'exact', 'lte'],
            'period': ['icontains', 'iexact'],
            'profession': ['iexact', 'icontains'],
            'nationality': ['iexact', 'icontains']
        }

    def search_by_name(self, queryset, name, value):
        return Artist.objects.filter(
            Q(last_name__icontains=value) | Q(first_name__icontains=value)
        )
