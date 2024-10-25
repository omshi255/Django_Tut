from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class chaiVariety(models.Model):
    CHAI_TYPE_CHOICE =[
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('KL','KIWI'),
        ('PL','PLAIN'),

    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='myapp/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')


def __str__(self):
    return self.name
 #one to many
 #--------|
 #--------one to many
 #--------|

class ChaiReview(models.Model):
    chai = models.ForeignKey(chaiVariety,on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

def __str__(self):
    return f'{self.user.username} reviwe for {self.chai.name}'



#Many to Many Relationships

class Store(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=200)
    chai_Varities= models.ManyToManyField(chaiVariety, related_name='stores')

def __str__(self):
    return self.name


#one to one RelationShip

#eg: cirtificate

class Cirtificate(models.Model):
    chai = models.OneToOneField(chaiVariety,on_delete=models.CASCADE,related_name='cirtificate')
    cirtificate_number = models.CharField(max_length=100)
    issued_date= models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()
def __str__(self):
    return f'cirtificate for {self.name.chai}'