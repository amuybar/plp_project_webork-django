from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from rest_framework import serializers # type: ignore
from rest_framework.exceptions import ValidationError # type: ignore
from.models import BidService, Blogs, GetStarted, Messages, Newsletter, Services

# Serializer for User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    # Create a new User instance
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

# Serializer for user login
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

# Serializer for password reset
class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    # Validate if the email exists in the User model
    def validate_email(self, value):
        try:
            user = User.objects.get(email=value)
            return value
        except User.DoesNotExist:
            raise ValidationError("No user is associated with this email address.")

    # Generate a password reset token and send an email to the user
    def save(self):
        request = self.context.get('request')
        email = self.validated_data['email']
        user = User.objects.get(email=email)
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        password_reset_url = f"{request.build_absolute_uri('/')[:-1]}/reset/{uid}/{token}/"
        context = {
            'password_reset_url': password_reset_url,
            'user': user,
        }
        subject = 'Password Reset Requested'
        message = render_to_string('api/password_reset_email.txt', context)
        send_mail(subject, message, None, [user.email])

# Serializer for GetStarted model
class GetStartedSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetStarted
        fields = '__all__'

# Serializer for BidService model
class BidServicesSerializer(serializers.ModelSerializer):
  class Meta:
    model = BidService
    fields = '__all__'

# Serializer for Newsletter model
class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ['email']

# Serializer for Messages model
class MessagesSerializer(serializers.ModelSerializer):
   class Meta:
     model = Messages
     fields = ['name', 'email', 'message', 'date_added']

# Serializer for Services model
class ServicesSerializer(serializers.ModelSerializer):
   class Meta:
     model = Services
     fields = ['name', 'description', 'image', 'quotation', 'expected_time', 'colaboration', 'date_added']

# Serializer for Blogs model
class BlogSerializer(serializers.ModelSerializer):
   class Meta:
     model = Blogs
     fields = ['title', 'description', 'image']