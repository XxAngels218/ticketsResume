import os
import json

from django.http import JsonResponse
from docxtpl import DocxTemplate
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


from ticketSummary.services.api.api_consumer import get_access_token, get_zoho_departments, get_tickets_by_deparment
from ticketSummary.services.data.data_cleaner import data_cleaner
from ticketSummary.services.data.data_list import make_data_list
from ticketSummary.services.summary import make_summary

# todo make a refactor of this code


def home(request):
    return render(request, 'ticketsummary/home.html')


def show_text(request):
    if request.method == 'POST':
        ticket_id = request.POST.get('ticketId')
        # summary = make_summary(data_cleaner(make_data_list(ticket_id)), prompt)
        summary = make_summary()
        context = {'ticketId': ticket_id, 'summary': summary}
        return render(request, 'ticketsummary/show_text.html', context)
    else:
        return render(request, 'ticketsummary/enter_text.html')


def export_to_word(ticket_id, problem, solution):
    doc = DocxTemplate(
        "ticketSummary/templates/ticketsummary/summaryTmpl.docx")
    context = {
        "ticketId": ticket_id,
        "problem": problem,
        "solution": solution,
    }
    doc.render(context)
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = f'attachment; filename="summary_{ticket_id}.docx"'
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
    data = get_tickets_by_deparment(get_access_token(), department_id)
    return render(request, 'ticketsummary/list_tickets.html', {'data': data['data']})
