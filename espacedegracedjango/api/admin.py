from django.contrib import admin
from .models import SubscribersList
from .models import ScriptureList
from .models import StoreProductItems
from .models import UpcomingEvents
from .models import ThemeCategory
from .models import SlideshowsImage
from .models import StoreProductItems
from .models import LastestEpisodes
from .models import FirstLatestEpisodeId
from .models import Episode, GuestSpeaker

# Register your models here.
admin.site.register(ScriptureList)
admin.site.register(SubscribersList)
admin.site.register(StoreProductItems)
admin.site.register(UpcomingEvents)
admin.site.register(SlideshowsImage)
admin.site.register(LastestEpisodes)
admin.site.register(FirstLatestEpisodeId)
admin.site.register(Episode)
admin.site.register(GuestSpeaker)
# admin.site.register()
