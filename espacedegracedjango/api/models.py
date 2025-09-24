from django.db import models

class SubscribersList(models.Model):
    firstName = models.CharField(max_length=200, default="")
    lastName = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200)
    subscribType = models.CharField(max_length=200, default="")
    startedDate = models.DateTimeField(auto_now_add=True)

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
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    itemImage = models.ImageField(default='fallback.jpg',blank=True)
    ratings = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name

class ThemeCategory(models.Model):
    theme = models.CharField(max_length=40)
    author = models.CharField(max_length=25)
    timeStamped = models.DateTimeField()

    def __str__(self):
        return self.name

class UpcomingEvents(models.Model):
    dateOfPublication = models.CharField(max_length=12)
    topic = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    image = models.ImageField(default='fallback.jpg', blank=True)

class SlideshowsImage(models.Model):
    sliderImage = models.ImageField(default='fallback.jpg', blank=True)
    topic = models.CharField(max_length=300,default='NA', blank=True)