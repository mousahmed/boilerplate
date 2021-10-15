from django.db import models
from django.utils import timezone
from django.conf import settings


class CommonInfo(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT)

    class Meta:
        abstract = True
