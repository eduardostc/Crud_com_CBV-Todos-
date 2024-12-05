from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Todo(models.Model):
    title = models.CharField(verbose_name="Título", max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(verbose_name="Data de Entrega", null=False, blank=False)
    finishe_at = models.DateField(null=True)

    class Meta:
        ordering = ["deadline"]

    def mark_has_complete(self):
        if not self.finishe_at:
            self.finishe_at = date.today()
            self.save()

class CustomUser(AbstractUser):
    telefone = models.CharField(_("telefone de contato"), max_length=15, blank=True)

    def __str__(self):
        return self.username