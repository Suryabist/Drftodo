from rest_framework import routers
from .views import todoview
from django.urls import path, include




router = routers.DefaultRouter()
router.register( 'todo', todoview)


urlpatterns = [
    path('', include(router.urls))


]
