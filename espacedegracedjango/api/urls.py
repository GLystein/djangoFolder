from django.urls import path
from . import views
from .views import ListOfScriptureCreate, ListOfSubscribersDetail, ListOfScripturePostDelete, StoreProductItemsCreateAPIView, StoreProductItemsList, AddingScripturePosting
from .views import ThemeScripture, ThemeList

# from .views import

urlpatterns = [
    path("listofsubscribers/", views.ListOfSubscribersCreate.as_view(), name='list-of-subcribers'),
    path('listofsubscribers/<int:pk>/', ListOfSubscribersDetail.as_view(), name='list Of Subscribers Detail'),
    path('listofscripturepost/', ListOfScriptureCreate.as_view(), name='list of scripture post'),
    path('listofscripturepostdelete/<int:id>/', ListOfScripturePostDelete.as_view(), name='Post scripture deletion'),
    path('addingscripture/',AddingScripturePosting.as_view(), name='Adding new object using post method'),
    path('storeproductitems/', StoreProductItemsCreateAPIView.as_view(), name='Store-create' ),
    path('storeproductitemslist', StoreProductItemsList.as_view(), name='list of the product'),
    path('addingthemecategory/', ThemeScripture.as_view(), name='Adding Theme' ),
    path('themelist/',ThemeList.as_view(), name='List of Theme')
    # path('scripturepost', views.ScripturesListAPIView.as_view(), name='delete one scripture')
]