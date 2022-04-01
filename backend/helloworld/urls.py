from django.urls import path
from rest_framework import routers
from . import views

my_router = routers.DefaultRouter()
my_router.register(r"users", views.UserViewSet)
my_router.register(r"groups", views.GroupViewSet)

urlpatterns = [
    path("near/", views.nearApi),
    path("hello-world/", views.helloWorldView),
    path("user-model/<int:userId>/", views.userView),
]

urlpatterns += my_router.urls
