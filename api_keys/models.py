__author__ = 'Taylor'

import hashlib
import random

from django.db import models


def generate_key():
    key = hashlib.sha224(str(random.getrandbits(256))).hexdigest()
    return key


class Client(models.Model):
    name = models.CharField(max_length=20)
    key = models.CharField(max_length=56, default=generate_key, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.key