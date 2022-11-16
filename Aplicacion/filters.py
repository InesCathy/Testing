import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class CitaFiltrar(django_filters.FilterSet):
    start_date = DateFilter(field_name="fecha_creada", lookup_expr='gte')
    end_date = DateFilter(field_name="fecha_creada", lookup_expr='lte')
    medico = CharFilter(field_name='medico', lookup_expr='icontains')
    class Meta:
        model =Cita
        fields = '__all__'
        exclude = ['paciente', 'fecha_creada']