from django.urls import path, include
from profile_api import views

from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('hello-viewset',views.HelloViewSet , base_name='hello-viewset')
router.register('profiles',views.UserProfileViewSet, base_name='profiles')
router.register('feed',views.UserProfileFeedViewSet,base_name='feed')


urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
    path('login/',views.UserLoginApiView.as_view()),
    path('',include(router.urls))   
]
