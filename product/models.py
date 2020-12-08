from django.db import models
from datetime import datetime
import random
from django_seed import Seed



class Product(models.Model):
    tittle = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    sale = models.IntegerField()
    vendor = models.CharField(max_length=200)
    made_in = models.CharField(max_length=200)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=200)
    category = models.CharField(max_length=200)

    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.tittle

seeder = Seed.seeder(locale='uk_UA')

seeder.add_entity(Product, 10, {
    'tittle': "Cвитшот",
    'price': lambda x: seeder.faker.random.randint(100,10000),
    'sale': lambda x: seeder.faker.random.randint(100,10000),
    'category': "Одяг",
    'description': "Ширина плечей: 50 см. Длина рукава: 66 см. Полуобхват в груди: 65 см.",
    'vendor': lambda x: seeder.faker.country(),
    'made_in': lambda x: seeder.faker.country(),
    'color': lambda x: seeder.faker.color_name(),
    'size': '41-44',
    'photo_main':'/photos/photo1.jpeg',
    'photo_1': lambda x: seeder.faker.file_path(depth=3, category='image'),
})
seeder.execute()