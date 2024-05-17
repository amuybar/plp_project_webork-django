from django.contrib.auth import authenticate

from api.models import BidService, Blogs, GetStarted, Messages, Newsletter, Services
from .serializers import BidServicesSerializer, BlogSerializer, GetStartedSerializer, MessagesSerializer, NewsletterSerializer, PasswordResetSerializer, ServicesSerializer
from rest_framework import generics, status# type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework_simplejwt.tokens import RefreshToken # type: ignore
from rest_framework.permissions import IsAuthenticated, AllowAny # type: ignore


from .serializers import UserSerializer, LoginSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class PasswordResetView(generics.GenericAPIView):
  
    serializer_class = PasswordResetSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "Password reset e-mail has been sent."})
      

# GetStarted API Views
class GetStartedListCreate(generics.ListCreateAPIView):
    queryset = GetStarted.objects.all()
    serializer_class = GetStartedSerializer
    permission_classes = [IsAuthenticated]

class GetStartedRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GetStarted.objects.all()
    serializer_class = GetStartedSerializer
    permission_classes = [IsAuthenticated]

# BidService API Views
class BidServicesListCreate(generics.ListCreateAPIView):
    queryset = BidService.objects.all()
    serializer_class = BidServicesSerializer
    permission_classes = [IsAuthenticated]

class BidServiceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BidService.objects.all()
    serializer_class = BidServicesSerializer
    permission_classes = [IsAuthenticated]

# Newsletter API Views
class NewsletterListCreate(generics.ListCreateAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    permission_classes = [IsAuthenticated]

class NewsletterRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    permission_classes = [IsAuthenticated]

# Messages API Views
class MessagesListCreate(generics.ListCreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer 
    permission_classes = [IsAuthenticated]

class MessagesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer 
    permission_classes = [IsAuthenticated]
    
# Services API Views
class ServicesListCreate(generics.ListCreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [IsAuthenticated]

class ServicesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [IsAuthenticated]

# Blog API Views
class BlogListCreate(generics.ListCreateAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]

class BlogRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]