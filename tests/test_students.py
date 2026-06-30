import pytest
from django.urls import reverse
from rest_framework import status
from studentapp.models import Student
import json

@pytest.mark.django_db
def test_create_student(client):
    url = reverse('student-create-list') 
    data = {
        "username": "test_user",
        "first_name": "user",
        "last_name": "Ibragimov",
        "email": "test77@example.com",
        "phone": "998901234567",
        "address": "Tashkent",
        "birth_date": "2006-01-01",
        'password':'ddddddddd'
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Student.objects.filter(username="test_user").exists()

@pytest.mark.django_db
def test_patch_student_address(client):
    student = Student.objects.create(
        username="test_patch",
        first_name="test_test",
        last_name="test_name",
        email="test_patch@example.com",
        birth_date="2000-01-01",
        address="Old Tashkent"
    )
    url = reverse('student-patch', kwargs={'pk': student.pk})
    data = {"address": "New Tashkent Address"}
    
    response = client.patch(
        url, 
        data=json.dumps(data), 
        content_type='application/json'
    )
    
    assert response.status_code == status.HTTP_200_OK
    student.refresh_from_db()
    assert student.address == "New Tashkent Address"

@pytest.mark.django_db
def test_delete_student(client):
    student = Student.objects.create(
        username="test_patch",
        first_name="test",
        last_name="test_name",
        email="test_patch@example.com",
        birth_date="2000-01-01",
        address="Old Tashkent"
    )
    url = reverse('student-detail', kwargs={'pk': student.pk})
    
    response = client.delete(url)
    
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Student.objects.count() == 0

@pytest.mark.django_db
def test_validation_missing_email(client):
    url = reverse('student-create-list')
    data = {"username": "", "first_name": "", "last_name": ""}
    response = client.post(url, data, format='json')
    
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'email' in response.data