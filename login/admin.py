# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Profile, Posts, Like, Follow, Comments

admin.site.register(Profile)
admin.site.register(Posts)
admin.site.register(Like)
admin.site.register(Follow)
admin.site.register(Comments)


