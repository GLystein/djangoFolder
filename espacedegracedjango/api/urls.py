from django.urls import path
from . import views
from .views import ListOfSubscribersDetail
# from .views import

urlpatterns = [
    path("listofsubscribers/", views.ListOfSubscribersCreate.as_view(), name='list-of-subcribers'),
    path('listofsubscribers/<int:pk>/', ListOfSubscribersDetail.as_view(), name='list Of Subscribers Detail'),
    path('listofcripturepost/', views.ListOfScripturePostCreate.as_view(), name='list of scripture post'),
]