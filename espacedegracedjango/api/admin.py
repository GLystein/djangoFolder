from django.contrib import admin
from .models import ListOfSubscribers
from .models import ListOfScripture
from .models import StoreProductItems
from .models import UpcomingEvents
from .models import ThemeCategory

# Register your models here.
admin.site.register(ListOfScripture)
admin.site.register(ListOfSubscribers)
admin.site.register(StoreProductItems)
admin.site.register(UpcomingEvents)
