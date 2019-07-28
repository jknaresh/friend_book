import django_filters
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics, filters
from rest_framework.permissions import AllowAny

from rest_apis.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    search_fields = ['username', 'email']
    filter_backends = [filters.SearchFilter]
