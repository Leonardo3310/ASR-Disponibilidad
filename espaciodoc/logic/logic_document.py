from ..models import document

def get_documents():
    queryset = document.objects.all().order_by('-dateTime')[:10]
    return (queryset)

def create_documents(form):
    document = form.save()
    document.save()
    return ()