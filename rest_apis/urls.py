from django.urls import include, path
from rest_framework import routers
from rest_apis import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'user-friend', views.UserFriendViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user-search/', views.UserListView.as_view()),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
