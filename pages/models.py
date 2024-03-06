from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
import ckeditor
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# slug
from django.utils.text import slugify
from random import random
from django.db.models.signals import pre_save
User = get_user_model()

# Create your models here.
#signup for email subscribe


class Contact(models.Model):
    
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.TextField(max_length=100, blank=True)
    msg = models.TextField(max_length=400, blank=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=55)
    overview = models.TextField(max_length=155)  
    slug = models.SlugField(max_length=100,unique=True, null=True, blank=True)
    
    content = RichTextUploadingField()
    timestamp = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d')
    featured = models.BooleanField(default=True)
    is_published = models.BooleanField(default=True)

    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post',kwargs={ 'slug': self.slug})

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug
    
def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
pre_save.connect(pre_save_post_receiver, Post)






    


        