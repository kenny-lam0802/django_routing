from django.urls import path
from . import views

urlpatterns = [
    path('first-route/', views.first_view),
    path('second-route/', views.second_view),

    #parameter routes
    path('cars', views.one_method),
    path('cars/<int:my_val>', views.another_method),
    path('cars/<str:name>/speed', views.name_method),
    path('cars/<int:id>/<str:color>', views.id_color),
]
