from rest_framework import serializers
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from studentapp.models import Student



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        try:
            user = Student.objects.get(username=username)
        except Student.DoesNotExist:
            raise serializers.ValidationError("Invalid username or password.")
        
        if not check_password(password, user.password):
            raise serializers.ValidationError("Invalid username or password.")

        if not user.is_active:
            raise serializers.ValidationError('This account is inactive.')
        

        refresh = RefreshToken.for_user(user)


        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'username': user.username
        }