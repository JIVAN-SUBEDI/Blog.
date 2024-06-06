from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.utils.crypto import get_random_string

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = original_slug = slugify(self.name)
            while Category.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{get_random_string(4)}"
        super(Category, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.slug

class Post(models.Model):
    title = models.CharField(max_length=1000)
    categories = models.ManyToManyField(Category, related_name='posts')
    image = models.ImageField(upload_to="static/posts/")
    slug = models.SlugField(unique=True, blank=True,max_length=1000)
    desc = RichTextField()
    short_desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = original_slug = slugify(self.title)
            while Post.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{get_random_string(4)}"
        super(Post, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.slug

class Recommended_Posts(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.post.slug
class About(models.Model):
    name= models.CharField(max_length=255)
    image = models.ImageField(upload_to="static/about")
    short_desc = models.TextField()
    desc = RichTextField()


