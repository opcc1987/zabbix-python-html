from . import views
from django.conf.urls import url
#from django.views.decorators.csrf import csrf_exempt
urlpatterns=[
    url(r'^home',views.home,name='home'),
    url(r'^report',views.report,name='report'),
]
