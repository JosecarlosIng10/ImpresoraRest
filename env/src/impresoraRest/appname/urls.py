from django.conf.urls import url
from rest_framework import routers as merouters
from impresoraRest.appname.views import ToolViewSet



merouter = merouters.DefaultRouter()
merouter.register(r'print', ToolViewSet)
 
urlpatterns = []
 
urlpatterns += merouter.urls