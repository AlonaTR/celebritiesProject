from django.urls import reverse
from django.db import models

# Create your models here.
class Women(models.Model):
    title = models.CharField(max_length=200)
    content= models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={"post_id": self.pk})
    
    class Meta:  # вложенный класс для метаданных модели админки
        verbose_name = 'Famous women'
        verbose_name_plural = 'Famous women'
        ordering = ['-time_create']

    
class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

   