from django.conf.urls import url
from rest_framework_mongoengine import routers as merouters
from impresoraRest.appname.views import ToolViewSet



merouter = merouters.DefaultRouter()
merouter.register(r'mongo', ToolViewSet)
 
urlpatterns = []
 
urlpatterns += merouter.urls