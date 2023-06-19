from django.http import JsonResponse
from docxtpl import DocxTemplate
from django.shortcuts import render
import os
from django.http import HttpResponse
from ticketSummary.utils.api_consumer import *
from ticketSummary.utils.data_cleaner import data_cleaner
from ticketSummary.utils.summary import *
from django.shortcuts import render
import json


prompt = " The text above is a python string which contains the records of a conversation to solve a technical support problem, make a summary of the above and separate it into problem and solution naming each one as Problem: and the other as Solution:, they are not ordered in sequence of what happened, max tokens 3000."


def home(request):
    return render(request, 'ticketsummary/home.html')


def show_text(request):
    if request.method == 'POST':
        ticketId = request.POST.get('ticketId')
        summary = make_summary(data_cleaner(make_data_list(ticketId)), prompt)
        context = {'ticketId': ticketId, 'summary': summary}
        return render(request, 'ticketsummary/show_text.html', context)
    else:
        return render(request, 'ticketsummary/enter_text.html')


def export_to_word(request, ticketId, problem, solution):
    doc = DocxTemplate(
        "ticketSummary/templates/ticketsummary/summaryTmpl.docx")
    context = {
        "ticketId": ticketId,
        "problem": problem,
        "solution": solution,
    }
    doc.render(context)
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = f'attachment; filename="summary_{ticketId}.docx"'
    doc.save(response)
    return response


def dropdown_view(request):
    data = get_zoho_departments(get_access_token())
    options = [(d['id'], d['name']) for d in data['data']]
    context = {
        'options': options
    }

    return render(request, 'ticketsummary/dropdown.html', context)


def tickets_view(request):
    department_id = request.GET.get('id')
    data = get_tickets_byDeparment(get_access_token(), department_id)
    return render(request, 'ticketsummary/list_tickets.html', {'data': data['data']})
