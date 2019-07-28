from django.contrib import admin

from user_profile.models import UserFriend


class UserFriendAdmin(admin.ModelAdmin):
    list_display = ("user_id", "friend_id", "c_on")


admin.site.register(UserFriend, UserFriendAdmin)
