
import pytest
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.test import APIRequestFactory
from api.models import BidService, Blogs, GetStarted, Messages, Newsletter, Services
from api.serializers import (
    UserSerializer, LoginSerializer, PasswordResetSerializer, GetStartedSerializer,
    BidServicesSerializer, NewsletterSerializer, MessagesSerializer, ServicesSerializer, BlogSerializer
)

@pytest.mark.django_db
def test_user_serializer_create():
    data = {
        'username': 'testuser',
        'password': 'testpassword',
        'email': 'testuser@example.com'
    }
    serializer = UserSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    user = serializer.save()
    assert User.objects.filter(username='testuser').exists()
    assert user.check_password('testpassword')

@pytest.mark.django_db
def test_login_serializer():
    user = User.objects.create_user(username='testuser', password='testpassword')
    data = {
        'username': 'testuser',
        'password': 'testpassword'
    }
    serializer = LoginSerializer(data=data)
    assert serializer.is_valid(), serializer.errors

@pytest.mark.django_db
def test_password_reset_serializer_valid_email():
    user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')
    data = {'email': 'testuser@example.com'}
    serializer = PasswordResetSerializer(data=data)
    assert serializer.is_valid(), serializer.errors

@pytest.mark.django_db
def test_password_reset_serializer_invalid_email():
    data = {'email': 'invalid@example.com'}
    serializer = PasswordResetSerializer(data=data)
    assert not serializer.is_valid()
    with pytest.raises(ValidationError):
        serializer.validate_email('invalid@example.com')
        
        
@pytest.mark.django_db
def test_password_reset_serializer_save(mocker):
    user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')
    data = {'email': 'testuser@example.com'}
    factory = APIRequestFactory()
    request = factory.post('/api/password_reset/', data, format='json')
    context = {'request': request}
    serializer = PasswordResetSerializer(data=data, context=context)
    assert serializer.is_valid(), serializer.errors
    
    # Mock the send_mail function
    mocker.patch('django.core.mail.send_mail', return_value=1)
    
    # Mock the render_to_string function to return a sample email body
    mocker.patch('django.template.loader.render_to_string', return_value='Sample email body')
    
    serializer.save()

@pytest.mark.django_db
def test_get_started_serializer():
    instance = GetStarted.objects.create(
        first_name='John',
        last_name='Doe',
        email='john.doe@example.com',
        phone='1234567890',
        country='Country',
        message='This is a test message',
        date_added=timezone.now()  # Use timezone.now() to avoid warnings
    )
    assert instance.first_name == 'John'
    assert instance.last_name == 'Doe'
    assert instance.email == 'john.doe@example.com'
    assert instance.phone == '1234567890'
    assert instance.country == 'Country'
    assert instance.message == 'This is a test message'

@pytest.mark.django_db
def test_bid_services_serializer():
    instance = BidService.objects.create(
        name='John Doe',
        email='john.doe@example.com',
        phone='1234567890',
        message='This is a bid service message',
        date_added=timezone.now()  # Use timezone.now() to avoid warnings
    )
    assert instance.name == 'John Doe'
    assert instance.email == 'john.doe@example.com'
    assert instance.phone == '1234567890'
    assert instance.message == 'This is a bid service message'

@pytest.mark.django_db
def test_newsletter_serializer():
    instance = Newsletter.objects.create(email='testuser@example.com')
    serializer = NewsletterSerializer(instance)
    data = serializer.data
    assert data['email'] == 'testuser@example.com'

@pytest.mark.django_db
def test_messages_serializer():
    instance = Messages.objects.create(name='test', email='test@example.com', message='Hello', date_added='2024-01-01')  # adjust date as needed
    serializer = MessagesSerializer(instance)
    data = serializer.data
    assert data['name'] == 'test'
    assert data['email'] == 'test@example.com'
    assert data['message'] == 'Hello'

@pytest.mark.django_db
def test_services_serializer():
    instance = Services.objects.create(
        name='Test Service', description='Description', image='image.jpg',
        quotation=100, expected_time='2 weeks', colaboration='Yes', date_added='2024-01-01'  # adjust date as needed
    )
    serializer = ServicesSerializer(instance)
    data = serializer.data
    assert data['name'] == 'Test Service'
    assert data['description'] == 'Description'

@pytest.mark.django_db
def test_blog_serializer():
    instance = Blogs.objects.create(title='Test Blog', description='Description', image='image.jpg', date_added='2024-01-01')
    serializer = BlogSerializer(instance)
    data = serializer.data
    assert data['title'] == 'Test Blog'
    assert data['description'] == 'Description'
