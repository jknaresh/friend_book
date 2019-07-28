from django.contrib.auth.models import User, Group
from rest_framework import serializers

from user_profile.models import UserFriend


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password']

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserFriendSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserFriend
        fields = ['user_id', 'friend_id']
