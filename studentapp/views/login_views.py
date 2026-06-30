from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from studentapp.serializers.login_serializers import LoginSerializer

class LoginApiView(APIView):
    permission_classes= [permissions.AllowAny]
    
    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TokenRefreshApiView(APIView):
    def post(self,request):
        refresh_token = request.data.get('refresh')

        if not refresh_token:
            return Response({'error':'Refresh Token is required'},status=status.HTTP_400_BAD_REQUEST)
        
        try:
            token = RefreshToken(refresh_token)
            new_access = str(token.access_token)

            return Response({'access': new_access},status=status.HTTP_200_OK)

        except TokenError:
            return Response({"error": "Invalid or expired token"}, status=status.HTTP_401_UNAUTHORIZED)
        

