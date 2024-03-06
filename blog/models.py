from django.db import models

# Create your models here the line with updated_by (number 8) can make more posts.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'Categories'


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/images')
    content = models.TextField()
    published = models.BooleanField(default=False)
    tags = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
        