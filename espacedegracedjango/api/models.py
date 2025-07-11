from django.db import models

class ListOfSubscribers(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subscribType = models.CharField(max_length=200)
    startedDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstName

class ListOfScripturePost(models.Model):
    author = models.CharField(max_length=100)
    topic = models.CharField(max_length=250)
    category = models.CharField(max_length=100)
    date = models.DateTimeField()
    # public = models.
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.author