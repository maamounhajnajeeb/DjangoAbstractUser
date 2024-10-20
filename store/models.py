from django.db import models


class Bolg(models.Model):
    title = models.CharField(max_length=200, null=False)
    content = models.TextField(null=False)

    def __str__(self) -> str:
        return f"blog id: {self.id}, blog title: {self.title}"
