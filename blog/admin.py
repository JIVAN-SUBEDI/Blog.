from django.contrib import admin
from .models import Category,Post,Recommended_Posts,About

# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Recommended_Posts)
admin.site.register(About)