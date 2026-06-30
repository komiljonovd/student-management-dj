from django.apps import AppConfig


class StudentappConfig(AppConfig):
    name = 'studentapp'
    verbose_name = 'Student'


    def ready(self):
        from . import signals