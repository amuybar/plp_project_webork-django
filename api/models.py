from django.utils import timezone
from django.db import models


# GET STARTED INFORMATION MODEL
class GetStarted(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    country = models.CharField(max_length=50)
    message = models.TextField()
    date_added = models.DateTimeField( default=timezone.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

# BIDDING MODELS
class BidService(models.Model):
    name = models.CharField(max_length=30)
    email=models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    date_added = models.DateTimeField( default=timezone.now)
    
    def __str__(self):
        return f"{self.name} - {self.email}"

# nEWS LETTER MODELS
class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    date_added = models.DateTimeField( default=timezone.now)
    def __str__(self):
        return self.email
   
#MODELS FOR MESSAGES SEND FROM OUR SITE 
class Messages(models.Model):
    name = models.CharField(max_length=30)
    email=models.EmailField()
    message=models.CharField(max_length=250)
    date_added = models.DateTimeField( default=timezone.now)
    
    def __str__(self):
        return f"{self.name} - {self.email}"

# MODEL FOR OUR SERVICES OFFERD   
class Services(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    image = models.ImageField()
    quotation = models.CharField(max_length=250)
    expected_time = models.CharField(max_length=250)
    colaboration = models.CharField(max_length=250)
    date_added = models.DateTimeField( default=timezone.now)
    
    def __str__(self):
        return f"{self.name} - {self.description}"

# BLOG MODEL FOE OUR BLOG PODT  
class Blogs(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    image = models.ImageField()
    date_added = models.DateTimeField( default=timezone.now)
    
    def __str__(self):
        return f"{self.title} - {self.description}"
    
#   COMMENTS MODEL <EACH RELATES TO A BLOG>
class Comments(models.Model):
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    comment = models.CharField(max_length=250)
    date_added = models.DateTimeField( default=timezone.now)
    
    def __str__(self):
        return f"{self.name} - {self.email}"