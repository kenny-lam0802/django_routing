from django.urls import path
from . import views

urlpatterns = [
    path('first-view', views.first_view),
    path('second-view', views.second_view),

    #redirecting
    path('', views.root_method),
    path('another_route', views.another_method),
    path('redirected_route', views.redirected_method),
]