from django.db import models



class todo(models.Model):
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)





    








