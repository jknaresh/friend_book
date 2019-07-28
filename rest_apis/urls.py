from django.urls import include, path
from rest_framework import routers
from rest_apis import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'user-friend', views.UserFriendViewSet)
# router.register(r'user-search', views.UserListView)


urlpatterns = [
    path('', include(router.urls)),
    path('user-search/', views.UserListView.as_view()),
    # url for friends list
    # path('user-friend/', views.UserFriendViewSet.as_view()),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
