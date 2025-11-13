from django.urls import path
from . import views
from .views import ScriptureListCreate, SubscribersListDetail, ScripturePostDelete
from .views import StoreItems, AddingScripturePosting, GetUpcomingEvents, EventsDeletion
from .views import ThemeScripture, ThemeList, SlideList, SlideShowPost, slideShowDeletion

# from .views import

urlpatterns = [
    path("subscriberslist/", views.SubscribersListCreate.as_view(), name='list-of-subcribers'),
    path('subscribersdetails/<int:pk>/', SubscribersListDetail.as_view(), name='list Of Subscribers Detail'),

    #
    path('addingscripture/',AddingScripturePosting.as_view(), name='Adding new object using post method'),
    path('scripturepostlist/', ScriptureListCreate.as_view(), name='list of scripture post'),
    path('scripturepostdelete/<int:id>/', ScripturePostDelete.as_view(), name='Post scripture deletion'),

    # STORE API
    path('storeproductslist/', StoreItems.as_view(), name='Store Product List' ),
    # path('storeproductitems/', StoreProductItemsCreateAPIView.as_view(), name='Store-create'),
    # path('itemsprodlist/', ItemsList.as_view(), name='list of the product'),

    #
    path('addingthemecategory/', ThemeScripture.as_view(), name='Adding Theme' ),
    path('themelist/',ThemeList.as_view(), name='List of Theme'),

    # -- Upcoming event urls
    path('getallupcomingevents/', GetUpcomingEvents.as_view(), name='Get all the upcoming events'),
    path('eventdeletion/<int:pk>', EventsDeletion.as_view(), name='Delete upcoming events'),

    # Slideshow event urls
    path('getslideshow/',SlideList.as_view(), name='get all the slideshow'),
    path('postslideshow/', SlideShowPost.as_view(),name='post all the slideshow'),
    path('slideshowdeletion/<int:pk>', slideShowDeletion.as_view(), name='Delete a post the slideshow')
    # path('scripturepost', views.ScripturesListAPIView.as_view(), name='delete one scripture')
]