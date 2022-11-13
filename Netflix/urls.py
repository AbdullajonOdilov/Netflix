from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from filmapp.views import *


router = DefaultRouter()
router.register("movies",KinoViewSet)
router.register("actors",ActorViewSet)
router.register("commentlar",CommentViewSet)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path("kinolar/",KinolarAPIView.as_view()),
    path("actorlar/",ActorsAPIView.as_view()),
    path("actor/<int:pk>/",AktorAPIView.as_view()),
    path("get_token/",TokenObtainPairView.as_view()),
    path("token_update/", TokenRefreshView.as_view()),
    path("comment/<int:pk>/", CommentAPIView.as_view()),

]
