from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class TODO(models.Model):
    srno = models.AutoField(primary_key=True,auto_created=True)
    title = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    