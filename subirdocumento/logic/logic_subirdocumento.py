from espaciodoc.models import document
from ..models import Alarm

def get_alarms():
    queryset = Alarm.objects.all()
    return (queryset)

def get_documents():
    queryset = document.objects
    return (queryset)

def create_alarm(document):
    alarm = Alarm()
    alarm.document = document
    alarm.title = document.title
    alarm.save()
    return alarm