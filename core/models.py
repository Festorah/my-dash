from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class MyMessage(models.Model):
    message = models.TextField(_("message"), blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("last updated at"))
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.created_at)
