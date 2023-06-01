from django.urls import path
from .views import post_detail, post_list #home_page, about_page, contact_us#


app_name = 'blogs'

urlpatterns = [
    #post views
     path('', post_list, name='post_list'),
     path ('<int:id>/', post_detail, name='post_detail',)



    # path('', home_page, name='home'),
    # path('about/', about_page, name='about'),
    # path('contact/', contact_us, name='contact'),
    
]