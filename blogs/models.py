from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    author = models.ForeignKey(
    "auth.User",
    on_delete = models.CASCADE,
    #Si se elimina el autor, se eliminara todo el contenido de ese autorJ
)
    def __str__(self) -> str:
        return self.title