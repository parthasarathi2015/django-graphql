from django.urls import reverse
from pytest_django.asserts import assertContains
import pytest
from .models import Business
from .forms import BusinessForm

@pytest.mark.django_db
def test_business_model():
    business = Business.objects.create(
        name='Demo Test Business',
        description='Demo Test description',
        employee_size=10,
        address='Demo Test address',
        phone_number='555-1234',
        owner_name='Demo Test owner',
        owner_phone_number='555-4321',
        website='https://www.abcd.com/'
    )
    assert str(business) == 'Demo Test Business'
    
@pytest.mark.django_db
def test_business_list_view(client):
    url = reverse('business_list')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_business_detail_view(client):
    business = Business.objects.create(
        name='Demo Test Business',
        description='Demo Test description',
        employee_size=10,
        address='Demo Test address',
        phone_number='555-1234',
        owner_name='Demo Test owner',
        owner_phone_number='555-4321',
        website='https://www.abcd.com/'
    )
    url = reverse('business_detail', args=[business.pk])
    response = client.get(url)
    assert response.status_code == 200
    assertContains(response, 'Demo Test Business')


@pytest.mark.django_db
def test_business_create_view(client):
    url = reverse('business_create')
    data = {
        'name': 'Demo Test Business',
        'description': 'Demo Test description',
        'employee_size': 10,
        'address': 'Demo Test address',
        'phone_number': '555-1234',
        'owner_name': 'Demo Test owner',
        'owner_phone_number': '555-4321',
        'website': 'https://www.abcd.com/'
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Business.objects.count() == 1


@pytest.mark.django_db
def test_business_update_view(client):
    business = Business.objects.create(
        name='Demo Test Business',
        description='Demo Test description',
        employee_size=10,
        address='Demo Test address',
        phone_number='555-1234',
        owner_name='Demo Test owner',
        owner_phone_number='555-4321',
        website='https://www.abcd.com/'
    )
    url = reverse('business_update', args=[business.pk])
    data = {
        'name': 'Updated Test Business',
        'description': 'Updated test description',
        'employee_size': 5,
        'address': 'Updated test address',
        'phone_number': '555-5678',
        'owner_name': 'Updated test owner',
        'owner_phone_number': '555-8765',
        'website': 'https://www.updated-example.com/'
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Business.objects.count() == 1

@pytest.mark.django_db
def test_business_delete_view(client):
    business = Business.objects.create(
        name='Demo Test Business',
        description='Demo Test description',
        employee_size=10,
        address='Demo Test address',
        phone_number='555-1234',
        owner_name='Demo Test owner',
        owner_phone_number='555-4321',
        website='https://www.abcd.com/'
    )
    url = reverse(f'business_delete', args=[business.pk])
   
    response = client.delete(url)
    assert response.status_code == 302
    assert Business.objects.count() == 0
