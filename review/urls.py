from django.urls import path
from. import views
app_name='review'
urlpatterns=[
    path('',views.index,name='index'),
    path('after_test/',views.after_test,name='after_test'),

]
