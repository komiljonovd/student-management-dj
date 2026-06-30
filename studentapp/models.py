from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password, check_password,is_password_usable
# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    birth_date = models.DateField()
    is_active = models.BooleanField(default=True)
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def set_password(self, raw_password):
        """Хэширует пароль и сохраняет его в поле."""
        print(raw_password)
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        print(self.password)
        """Проверяет, совпадает ли введенный пароль с хэшем в базе."""
        return check_password(raw_password, self.password)
    
    def save(self, *args, **kwargs):
         super().save(*args, **kwargs)
    


    def __str__(self):
        return self.username

    class Meta:
        db_table = 'Student'
        verbose_name = 'Student'
        verbose_name_plural = 'Student'






