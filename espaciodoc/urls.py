from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('documents/', views.document_list),
    path('documentupload/', csrf_exempt(views.documentUpload), name='documentUpload'),
]