from rest_framework import generics,filters
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from studentapp.models import Student
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from studentapp.serializers.student_serializers import StudentSerializer,StudentPatchSerializer

class StudentListCreateApi(generics.ListCreateAPIView):
    queryset = Student.objects.order_by('-created_at')
    serializer_class = StudentSerializer

    @method_decorator(cache_page(60*15,key_prefix='student_list_api'))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter
    ]

    search_fields = ['username', 'email', 'first_name', 'last_name']
    
    filterset_fields = ['is_active']
    

    ordering_fields = ['created_at', 'username']
    ordering = ['-created_at','-updated_at']  

    
    
class StudentDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    http_method_names = ['put','delete','get']

    @method_decorator(cache_page(60*15,key_prefix='student_detail_api'))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    


class StudentPatchApi(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentPatchSerializer
    http_method_names = ['patch']
    parser_classes = [JSONParser, FormParser, MultiPartParser] 