# blog/models.py
from django.db import models
from django.urls import reverse  # Tambahkan impor ini

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='static/img/', null=True, blank=True)
    author = models.CharField(max_length=100)  # Tambahkan atribut author
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])
