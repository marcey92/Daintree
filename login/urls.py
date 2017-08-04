from django.conf.urls import url
from .views import login_view
from .views import logout_view
from .views import register_view

app_name = 'login'

urlpatterns = [

url(r'^$', login_view, name= 'login'),
url(r'^logout/', logout_view, name= 'logout'),
url(r'^register/', register_view, name= 'register'),
url(r'^index/', register_view, name= 'index'), #redirect to home page

]