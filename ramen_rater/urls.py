from django.urls import path
from .views import (IndexView, HomePageView, RamenDetails,
                    AddRamen, EditRamen, DeleteRamen, SearchRamen)


urlpatterns = [
               path('', HomePageView.as_view(), name='home'),
               path('ramen_rater/', IndexView.as_view(), name='index'),
               path('ramen_rater/detail/<int:pk>', RamenDetails.as_view(), 
                    name="detail"),
               path('ramen_rater/add', AddRamen.as_view(), name='add'),
               path('ramen_rater/edit/<int:pk>', EditRamen.as_view(),
                    name='edit'),
               path('ramen_rater/delete/<int:pk>', DeleteRamen.as_view(),
                    name='delete'), 
               path('ramen_rater/search', SearchRamen.as_view(), name='search'),
               
          
               ]



