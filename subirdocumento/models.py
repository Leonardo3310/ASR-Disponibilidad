from django.db import models
from variables.models import Variable
from espaciodoc.models import document

class Alarm(models.Model):
    document = models.ForeignKey(document, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=255)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{"document": %s,"dateTime": %s}' % (self.document.title, self.dateTime)
    
    def toJson(self):
        alarm = {
            'id': self.id,
            
            'document': self.document.title,
            'title': self.title,
            'dateTime': self.dateTime,
            
        }
        return alarm