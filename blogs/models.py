from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    author = models.ForeignKey(
    "auth.User",
    on_delete = models.CASCADE,
    #Si se elimina el autor, se eliminara todo el contenido de ese autorJ
)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse ("post_detail", args=[str(self.id)])
    #reverse("post_detail", args=[str(self.id)])