# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class User(models.Model):

    WORKING = 'working'
    ON_VACATION = 'vacation'

    STATUSES = (
        (WORKING, "Working"),
        (ON_VACATION, "On Vacation"),
    )
    list_display = ['get_status_display']

    username = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUSES, default=WORKING)


def get_or_none(model, *args, **kwargs):

    try:
        return model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        return None

