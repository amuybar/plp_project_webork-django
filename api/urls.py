from django.urls import include, path
from rest_framework import routers # type: ignore
from drf_yasg.views import get_schema_view # type: ignore
from drf_yasg import openapi # type: ignore
from .views import (
    BidServicesListCreate,
    BidServiceRetrieveUpdateDestroyAPIView,
    BlogListCreate,
    BlogRetrieveUpdateDestroyAPIView,
    GetStartedListCreate,
    GetStartedRetrieveUpdateDestroyAPIView,
    MessagesListCreate,
    MessagesRetrieveUpdateDestroyAPIView,
    NewsletterListCreate,
    NewsletterRetrieveUpdateDestroyAPIView,
    RegisterView,
    LoginView,
    PasswordResetView,
    ServicesListCreate,
    ServicesRetrieveUpdateDestroyAPIView,
)
from rest_framework_simplejwt.views import TokenRefreshView # type: ignore

schema_view = get_schema_view(
    openapi.Info(
        title="Webwork Labs API",
        default_version='v1',
        description="Api documentation for webwork website",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="odaribq@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)
urlpatterns = [
    # Authentication URLs
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', include('django.contrib.auth.urls')),
    
    # GetStarted URLs
    path('getstarted/', GetStartedListCreate.as_view(), name='getstarted-list-create'),
    path('getstarted/<int:pk>/', GetStartedRetrieveUpdateDestroyAPIView.as_view(), name='getstarted-retrieve-update-destroy'),

    # BidService URLs
    path('bidservices/', BidServicesListCreate.as_view(), name='bidservices-list-create'),
    path('bidservices/<int:pk>/', BidServiceRetrieveUpdateDestroyAPIView.as_view(), name='bidservices-retrieve-update-destroy'),

    # Newsletter URLs
    path('newsletter/', NewsletterListCreate.as_view(), name='newsletter-list-create'),
    path('newsletter/<int:pk>/', NewsletterRetrieveUpdateDestroyAPIView.as_view(), name='newsletter-retrieve-update-destroy'),

    # Messages URLs
    path('messages/', MessagesListCreate.as_view(), name='messages-list-create'),
    path('messages/<int:pk>/', MessagesRetrieveUpdateDestroyAPIView.as_view(), name='messages-retrieve-update-destroy'),
    
    # Services URLs
    path('services/', ServicesListCreate.as_view(), name='services-list-create'),
    path('services/<int:pk>/', ServicesRetrieveUpdateDestroyAPIView.as_view(), name='services-retrieve-update-destroy'),
    
    # Blog URLs
    path('blog/', BlogListCreate.as_view(), name='blog-list-create'),
    path('blog/<int:pk>/', BlogRetrieveUpdateDestroyAPIView.as_view(), name='blog-retrieve-update-destroy'),
    
    # swagger/openai schema 
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
