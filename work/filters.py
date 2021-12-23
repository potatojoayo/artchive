import django_filters
from django.db.models import Q
from django_filters import rest_framework as filters
from .models import Work


class WorkFilter(filters.FilterSet):

    name_and_artist = django_filters.CharFilter(
        method='search_by_name_and_artist', label='search')

    class Meta:

        model = Work
        fields = {
            'name': ['icontains', 'iexact'],
            'artist': ['exact'],
            'finish_year': ['gte', 'range', 'exact', 'lte'],
            'info': ['icontains'],
            'location': ['icontains']
        }

    def search_by_name_and_artist(self, queryset, name, value):
        return Work.objects.filter(
            Q(name__icontains=value) | Q(artist__last_name__icontains=value)
        )
