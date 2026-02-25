from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
