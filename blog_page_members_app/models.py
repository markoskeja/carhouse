from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField()
    
class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title    
    
class Signup(models.Model):
    email = models.EmailField(null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    emri = models.TextField(null=True, blank=True)
    yourmessage = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True,  null=True, blank=True)
    comment_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category, null=True, blank=True)
    featured = models.BooleanField( null=True, blank=True)

    def __str__(self):
        return self.title
    
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title   
