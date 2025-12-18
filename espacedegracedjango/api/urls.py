from django.urls import path
from .views import ScriptureListCreate, ScripturePostDelete, LastestEpisodesList
from .views import StoreItems, AddingScripturePosting, GetUpcomingEvents, EventsUpdate
from .views import ThemeScripture, ThemeList, SlideList, SlideShowPost, slideShowDeletion
from .views import ItemsDeletion, SubscribersListDetail, SubscribersListCreate

# from .views import

urlpatterns = [
    path("subscriberslist/", SubscribersListCreate.as_view(), name='list-of-subcribers'),
    path('subscribersdetails/<int:pk>/', SubscribersListDetail.as_view(), name='list Of Subscribers Detail'),

    #
    path('addingscripture/',AddingScripturePosting.as_view(), name='Adding new scripture punlication'),
    path('scripturepostlist/', ScriptureListCreate.as_view(), name='list of scripture published'),
    path('scripturepostdelete/<int:id>/', ScripturePostDelete.as_view(), name='Scripture deletion'),

    # STORE API
    path('storeproductslist/', StoreItems.as_view(), name='Store Product List' ),
    path('itemsdeletion/<int:id>/', ItemsDeletion.as_view(), name='Delete an Item product in the store' ),
    # path('storeproductitems/', StoreProductItemsCreateAPIView.as_view(), name='Store-create'),
    # path('itemsprodlist/', ItemsList.as_view(), name='list of the product'),

    #
    path('addingthemecategory/', ThemeScripture.as_view(), name='Adding Theme' ),
    path('themelist/',ThemeList.as_view(), name='List of Theme'),

    # -- Upcoming event urls
    path('getallupcomingevents/', GetUpcomingEvents.as_view(), name='Get all the upcoming events'),
    path('eventupdate/<int:pk>/', EventsUpdate.as_view(), name='Delete upcoming events'),
    path('eventupdate/',EventsUpdate.as_view(), name='Update existing event'),

    # Slideshow event urls
    path('getslideshow/',SlideList.as_view(), name='get all the slideshow'),
    path('postslideshow/', SlideShowPost.as_view(),name='post all the slideshow'),
    path('slideshowdeletion/<int:pk>', slideShowDeletion.as_view(), name='Delete a post the slideshow'),
    # path('scripturepost', views.ScripturesListAPIView.as_view(), name='delete one scripture')

    # Last Episode
    path('lastepisodegetlist/',LastestEpisodesList.as_view(), name='Get All the Last Episodes List max 5'),
    path('lastepisodechange/<int:pk>', LastestEpisodesList.as_view(), name='Get All the Last Episodes List max 5'),

]