from django.contrib import admin
from django.urls import path, include
from app.views import ContactViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('contacts', ContactViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)),
]
