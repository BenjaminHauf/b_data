from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from accounts.models import Account

class Communication(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={
        'model__in': ('family', 'bank', 'insurance', 'administration', 'accommodation')
    })
    object_id = models.PositiveIntegerField()
    related_object = GenericForeignKey('content_type', 'object_id')

    subject = models.CharField(max_length=100)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    files = models.CharField(null=True,blank=True)

    def __str__(self):
        return f"{self.subject} ({self.content_type} ID: {self.object_id})"