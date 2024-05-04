from django.shortcuts import render
from .forms import documentForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_document import create_documents, get_documents

def document_list(request):
    documents = get_documents()
    context = {
        'document_list': documents
    }
    return render(request, 'documents/documents.html', context)

def documentUpload(request):
    if request.method == 'POST':
        form = documentForm(request.POST)
        if form.is_valid():
            create_documents(form)
            messages.add_message(request, messages.SUCCESS, 'document uploaded successfuly')
            return HttpResponseRedirect(reverse('documentUpload'))
        else:
            print(form.errors)
    else:
        form = documentForm()

    context = {
        'form': form,
    }

    return render(request, 'documents/documentUpload.html', context)