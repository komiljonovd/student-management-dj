from django.contrib import admin
from .models import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['username','first_name','last_name','email','phone','address','birth_date','is_active','created_at','updated_at']
    search_fields = ['username','first_name','last_name','email','phone','address']
    list_filter = ('is_active', 'created_at','updated_at')
    ordering = ('-created_at',)
    actions = ['activate','deactivate']

    def save_model(self, request, obj, form, change):
        if 'password' in form.changed_data:
            obj.set_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)

    @admin.action(description='Активировать пользователя')
    def activate(self,request,queryset):
        queryset = queryset.filter(is_active=False).update(is_active=True)
        return self.message_user(request,f'Активировано : {queryset}')
    

    @admin.action(description='Деактивировать пользователя')
    def deactivate(self,request,queryset):
        queryset = queryset.filter(is_active=True).update(is_active=False)
        return self.message_user(request,f'Деактивировано : {queryset}')
