from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Student

@receiver([post_delete,post_save],sender=Student)
def clear_student_cache(sender,instance,**kwargs):
    cache.delete_pattern('*student_list_api*')
    cache.delete_pattern('*student_detail_api*')
    print('student cache is deleted')
