from django.db import models
import uuid
# Create your models here.
class Manga(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField( max_length=100)
    description = models.TextField()
    rating = models.IntegerField()
    photo = models.ImageField(null= True, blank= True, upload_to="mangas")

    def __str__(self): 
        return f'{self.name} {self.description}'

