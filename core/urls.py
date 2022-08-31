from django.contrib import admin
from django.urls import path, include
from app.views import ContactViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/contacts/', ContactViewSet.as_view(), name="contacts"),
]
