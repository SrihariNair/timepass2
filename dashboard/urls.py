from django.urls import path
from . import views
app_name='dashboard'


urlpatterns = [
    path('birthday_list/',views.birthdaylist,name='birthday_list'),
    path('profileview/', views.profileview, name='profileview'),
    path('home/',views.home,name='home'),
    path('approval/', views.approval, name='approval'),
    path('applyleave/', views.applyleave.as_view(), name='applyleave'),

]