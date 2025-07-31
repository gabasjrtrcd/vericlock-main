from django.http import HttpResponse
from django.template import loader

from .models import Person, TimeInRecord, TimeOutRecord


def index(request):
    person_list = Person.objects.all()
    context = { "person_list": person_list }
    template = loader.get_template('bundy/index.html')
    return HttpResponse(template.render(context, request))


def about(request, person_id):
    return HttpResponse(f"About person {person_id} in Bundy app.")


def persons(request):
    return HttpResponse("List of persons in Bundy app.")