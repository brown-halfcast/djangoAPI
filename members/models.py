from django.db import models
import uuid

# Create your models here.
class Member(models,Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    joined_date = models.DateField(auto_now_add=True)

    def _str_(self):
        return f"{self.first_name} {self.last_name}"
