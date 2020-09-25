import django_filters
from .models import nota


class notaFilter(django_filters.FilterSet):
    class Meta:
        model = nota
        fields = ['titulo']
        labels = ['']
