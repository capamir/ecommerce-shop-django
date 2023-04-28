from django.db import models
import uuid

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250, db_index=True)
    brand = models.CharField(max_length=250, default='un-branded')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    slug = models.SlugField(max_length=250)
    image = models.ImageField(upload_to='images/', default='default.jpg', blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    