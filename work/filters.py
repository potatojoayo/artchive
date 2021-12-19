from django_filters import rest_framework as filters
from .models import Work


class WorkFilter(filters.FilterSet):

    class Meta:

        model = Work
        fields = {
            'name': ['icontains', 'iexact'],
            'artist': ['exact'],
            'finish_year': ['gte', 'range', 'exact', 'lte'],
            'info': ['icontains'],
            'location': ['icontains']
        }
