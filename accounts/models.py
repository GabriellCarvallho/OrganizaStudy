from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="accounts_user_set",
        blank=True,
        help_text="Grupos aos quais o usuário pertence.",
        verbose_name="groups",
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="accounts_user_permissions_set",
        blank=True,
        help_text="Permissões específicas do usuário.",
        verbose_name="user permissions",
    )

    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    meta_de_horas_diarias = models.DecimalField(
        max_digits=4, decimal_places=1, default=2.0
    )

    def __str__(self):
        return self.username