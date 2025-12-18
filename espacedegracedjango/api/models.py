from django.db import models
from datetime import datetime, timedelta, date

class SubscribersList(models.Model):
    firstName = models.CharField(max_length=200, default="")
    lastName = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200)
    subscribType = models.CharField(max_length=200, default="")
    startedDate = models.DateTimeField(auto_now_add=True)
    endDate = models.DateTimeField(null=True, blank=True) #auto_now_add=True,
    # endDate = models.DateTimeField(default= "2023-10-27 10:30:00Z",blank=True)
    # endDate = models.DateField(default=date.today() + timedelta(days=14))

    def __str__(self):
        return self.firstName

class ScriptureList(models.Model):
    author = models.CharField(max_length=100)
    # topic = models.CharField(max_length=250)
    category = models.CharField(max_length=100)
    date = models.DateTimeField()
    # public = models.
    message = models.TextField()
    authorAvatar = models.ImageField(default='fallback.jpg',blank=True)

    def __str__(self):
        return self.name

class StoreProductItems(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    itemImage = models.ImageField(default='fallback.jpg',blank=True)
    ratings = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    brand = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    countInStock = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    numReviews = models.DecimalField(max_digits=10, decimal_places=0, default=0)

    def __str__(self):
        return self.name

class ThemeCategory(models.Model):
    theme = models.CharField(max_length=40)
    author = models.CharField(max_length=25)
    timeStamped = models.DateTimeField()

    def __str__(self):
        return self.name

class UpcomingEvents(models.Model):
    dateOfPublication = models.CharField(max_length=12,blank=True)
    topic = models.CharField(max_length=50,blank=True)
    description = models.CharField(max_length=300, blank=True)
    image = models.ImageField(default='fallback.jpg', blank=True)

class SlideshowsImage(models.Model):
    sliderImage = models.ImageField(default='fallback.jpg', blank=True)
    topic = models.CharField(max_length=300,default='NA', blank=True)

class LastestEpisodes(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    guestSpeaker = models.CharField(max_length=40)
    publicationDate = models.DateTimeField(blank=True)
    thumbnail = models.ImageField(default='fallback.jpg', blank=True)

# class