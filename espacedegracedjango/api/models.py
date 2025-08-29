from django.db import models

class ListOfSubscribers(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subscribType = models.CharField(max_length=200)
    startedDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstName

class ListOfScripture(models.Model):
    author = models.CharField(max_length=100)
    topic = models.CharField(max_length=250)
    category = models.CharField(max_length=100)
    date = models.DateTimeField()
    # public = models.
    message = models.TextField()

    def __str__(self):
        return self.author

class StoreProductItems(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    itemImage = models.ImageField(default='fallback.jpg',blank=True)

    def __str__(self):
        return self.name

class ThemeCategory(models.Model):
    theme = models.CharField(max_length=40)
    author = models.CharField(max_length=25)
    timeStamped = models.DateTimeField()

    def __str__(self):
        return self.name

class UpcomingEvents(models.Model):
    dateOfPublication = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    image = models.ImageField(default='fallback.jpg', blank=True)
