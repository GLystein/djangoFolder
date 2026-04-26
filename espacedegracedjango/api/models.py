from django.contrib.postgres.fields import ArrayField
from django.db import models
from datetime import datetime, timedelta, date
from django.db.models.signals import post_save
from django.dispatch import receiver
# from imageio.config.plugins import summary


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
    location = models.CharField(max_length=100, blank=True, default="")

class SlideshowsImage(models.Model):
    sliderImage = models.ImageField(default='fallback.jpg', blank=True)
    topic = models.CharField(max_length=300,default='NA', blank=True)

class LastestEpisodes(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    guestSpeaker = models.CharField(max_length=40)
    publicationDate = models.DateTimeField(blank=True,null=True)
    thumbnail = models.ImageField(default='fallback.jpg', blank=True)
    synced_at = models.DateTimeField(auto_now_add=True)
    episode_num = models.IntegerField()

    class Meta:
        ordering = ['-synced_at']

class FirstLatestEpisodeId(models.Model):
    episodeId = models.CharField(blank=True)

def get_next_episode_id():
    last_episode = Episode.objects.all().order_by('episodeId').last()
    if not last_episode:
        return 20250001
    return last_episode.episodeId+1


class GuestSpeaker(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)
    Minister_title = models.CharField(max_length=200)
    company_church = models.CharField(max_length=200,blank=True)
    bio = models.TextField(help_text="Full professional biography")
    headshot = models.ImageField(upload_to='speakers/', blank=True, null=True)
    linkedin_url = models.URLField(blank=True)
    expertise = models.JSONField(default=list)  # List of tags or topics
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Episode(models.Model):
    episodeId = models.IntegerField(default=get_next_episode_id,unique = True, editable=False)
    # unique = True
    title = models.CharField(max_length=150)
    description = models.TextField()
    air_Date = models.DateTimeField()
    duration = models.IntegerField()
    media_url = models.URLField(blank=True)
    # guests_array = models.ManyToManyField('GuestSpeaker', through='EpisodeGuestAssignment')
    guests_array = models.ManyToManyField('GuestSpeaker', blank=True)
    # guest = ArrayField(models.CharField(max_length=100), blank=True, size= 8)
    status = models.BooleanField(default=False)
    images = models.ImageField(default='fallback.jpg', blank=True)
    slideImage = models.ImageField(default='fallback.jpg', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Determine if this is a new object creation
        is_new = self.pk is None
        super().save(*args, **kwargs)  # Save the Product first

        if is_new:
            slideshowAdding = SlideshowsImage.objects.create(
                sliderImage = self.slideImage,
                topic = self.title
            )
# class EpisodeGuestAssignment(models.Model):
#     episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
#     speaker = models.ForeignKey(GuestSpeaker, on_delete=models.CASCADE)
#     role = models.CharField(max_length=100) # Example of an extra field

@receiver(post_save, sender=Episode)
def sync_latest_episodes(sender, instance, created, **kwargs):
    if created:
        # 1. Manually map fields from Episode to LastestEpisodes
        LastestEpisodes.objects.create(
            episode_num=instance.episodeId,
            title=instance.title
        )

        # 2. Keep only the 5 most recent records
        # all_entries = LastestEpisodes.objects.all().order_by('-synced_at')
        all_entries = LastestEpisodes.objects.all().order_by('-id')
        if all_entries.count() > 5:
            # Get the IDs of the 5 newest
            ids_to_keep = all_entries.values_list('id', flat=True)[:5]
            # Delete anything not in that list
            LastestEpisodes.objects.exclude(id__in=ids_to_keep).delete()