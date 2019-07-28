from django.contrib.auth.models import User, Group
from django.db.models import Q
from django.http import Http404
from rest_framework import viewsets, generics, filters, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from rest_apis.serializers import UserSerializer, UserFriendSerializer
from user_profile.models import UserFriend


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    search_fields = ['username', 'email']
    filter_backends = [filters.SearchFilter]


class UserFriendViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    serializer_class = UserFriendSerializer
    queryset = UserFriend.objects.all()

    def get_queryset(self):
        return UserFriend.objects.filter(Q(user_id=self.request.user) | Q(friend_id=self.request.user))

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            print(instance)
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)
