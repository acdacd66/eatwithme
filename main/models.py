from django.db import models
from account.models import User
# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=100,null=True)
    pub_date = models.DateTimeField(null=True)
    body = models.TextField(null=True)
    meeting_time = models.DurationField(null=True)
    number = models.IntegerField(null=True)
    location = models.CharField(max_length=30,null=True)
    writer = models.CharField(max_length=500, null=True)
    like=models.ManyToManyField(User, blank=True,related_name="User_apply")
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]
    
    def total_appliers(self):
        return self.like.count()


