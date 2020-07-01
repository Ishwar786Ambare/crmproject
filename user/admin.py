
from django.contrib import admin
from django.contrib.auth.models import Group

from .forms import UserAdmin
from .models import MyUser


# Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
