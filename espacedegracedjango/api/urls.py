from django.urls import path
from . import views
from .views import ListOfSubscribersDetail, ListOfScripturePostDelete

# from .views import

urlpatterns = [
    path("listofsubscribers/", views.ListOfSubscribersCreate.as_view(), name='list-of-subcribers'),
    path('listofsubscribers/<int:pk>/', ListOfSubscribersDetail.as_view(), name='list Of Subscribers Detail'),
    path('listofscripturepost/', views.ListOfScripturePostCreate.as_view(), name='list of scripture post'),
    path('listofscripturepostdelete/<int:pk>', ListOfScripturePostDelete.as_view(), name='Post scripture deletion')
]