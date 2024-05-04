from django.http import JsonResponse
from django.shortcuts import render

from variables.logic.variable_logic import get_variable_by_id
from .logic.logic_subirdocumento import get_alarms, get_documents, create_alarm

def alarm_list(request):
    alarms = get_alarms()
    context = list(alarms.values())
    return JsonResponse(context, safe=False)

def generate_alarm(request, variable_id):
    variable = get_variable_by_id(variable_id)
    documents = get_documents()
    createAlarm = False
    upperDocument = None
    for document in documents:
        if document.title == '' or document.title == ' ' or document.title == None or document.title == 'DANGER':
            createAlarm = True
            upperDocument = document
    if createAlarm:
        alarm = create_alarm(variable, upperDocument, 30)
        return JsonResponse(alarm.toJson(), safe=False)
    else:
        return JsonResponse({'message': 'No alarm created'}, status=200)