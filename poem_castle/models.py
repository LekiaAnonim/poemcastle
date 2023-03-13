from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.urls import reverse
from cloudinary.models import CloudinaryField

# Create your models here.
class Collection(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    slug = models.SlugField(null=True,  max_length=500)
    # image = CloudinaryField('image', null=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Collection, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('poem_castle:collection_detail',
                       kwargs={'slug': self.slug})
    
class Author(models.Model):
    full_name = models.CharField(null=True, blank=True, max_length=500)

    class Meta:
        ordering = ['full_name']

    def __str__(self):
        return f"{self.full_name}"

class Poem(models.Model):
    collection = models.ForeignKey(Collection, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=500, null=True, blank=True,)
    slug = models.SlugField(null=True,  max_length=500)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    body = RichTextField()
    date_created = models.DateField(auto_now=True)
    featured_image = CloudinaryField('image', null=True)
    add_to_featured_poems = models.BooleanField(default=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Poem, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('poem_castle:poem_detail', kwargs={'slug': self.slug, 'id': self.id})