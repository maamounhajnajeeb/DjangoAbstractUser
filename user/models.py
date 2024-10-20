from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserModel(AbstractUser):

    class UserTypes(models.TextChoices):
        ADMIN = "ADMIN", _("Admin")
        CLIENT = "CLIENT", _("CLIENT")

    base_type = UserTypes.CLIENT
    user_type = models.CharField(choices=UserTypes.choices, max_length=8, default=base_type)
    email = models.EmailField(
        unique=True, default="maamoun.haj.najeeb@gmail.com", max_length=36, db_index=True
        )
    username = None

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"

    def __str__(self) -> str:
        return f"<username: {self.username}>, <id: {self.pk}>"


# added things
class AdminManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type=UserModel.UserTypes.ADMIN)


class Admin(UserModel):

    base_type = UserModel.UserTypes.ADMIN
    objects = AdminManager()

    class Meta:
        proxy = True

    def __str__(self) -> str:
        return super().__str__()

    def save(self, *args, **kwargs) -> None:
        self.user_type = self.UserTypes.ADMIN
        self.is_staff, self.is_superuser = True, True
        return super().save(*args, **kwargs)


class AdminProfile(Admin):
    rank = models.CharField(max_length=1, default="A")
