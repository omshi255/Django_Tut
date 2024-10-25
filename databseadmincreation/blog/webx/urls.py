from django.urls import path 
from . import views
urlpatterns =[
  path('',views.index,name='index'),
  path('<int:chai_id>/',views.data_val,name='details'),
]