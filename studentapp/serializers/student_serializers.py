from rest_framework import serializers
from studentapp.models import Student
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
import re

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','first_name','last_name','email','phone','address','birth_date','username','password','is_active']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_active': {'read_only': True},
            

        }

    def validate_phone(self, value):
        
        clean_phone = re.sub(r'[^\d+]', '', value)
        
        if re.search(r'[a-zA-Z]', value):
            raise serializers.ValidationError("The phone number must consist of numbers only.")
        
       
        if clean_phone.count('+') > 1 or (clean_phone.count('+') == 1 and not clean_phone.startswith('+')):
            raise serializers.ValidationError("The '+' symbol can only be at the beginning.")
            
       
        digits_only = clean_phone.replace('+', '')
        if len(digits_only) < 9:
            raise serializers.ValidationError("The phone number must be at least 9 digits.")
            
        return clean_phone
    

    def validate_email(self, value):
        value = value.lower()
        if '@' in value:
            index = value.index('@')
            if len(value[:index]) < 6:
                raise serializers.ValidationError("Incorrect format of Email")
     
        return value
    
    def validate_username(self, value):
        if len(value) < 4:
            raise serializers.ValidationError("Логин должен содержать минимум 4 символа.")
        return value
    
    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("Пароль должен содержать минимум 6 символов.")
        return value
    
    def validate(self, data):
        required_fields = ['first_name','last_name','email','phone','address','birth_date','username','password']
        for field in required_fields:
            if not data.get(field):
                raise serializers.ValidationError({field: f"{field} is required field."})
        
        return data
        

    def create(self, validated_data):
        raw_password = validated_data.pop('password', None)
        
        student = Student(**validated_data)
        
        if raw_password:
            student.set_password(raw_password)
            
        student.save()
        return student
    


class StudentPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['address'] 