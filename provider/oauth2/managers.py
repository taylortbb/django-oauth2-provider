from django.utils import timezone
from django.db import models


class AccessTokenManager(models.Manager):
    def get_token(self, token):
        return self.get(token=token, expires__gt=timezone.now())
