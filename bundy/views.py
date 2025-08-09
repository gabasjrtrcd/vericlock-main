from django.http import HttpResponse
from django.template import loader

from datetime import datetime
from .models import Person, TimeRecord

from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.conf import settings
import os

def index(request):
    person_list = Person.objects.all()
    context = { "person_list": person_list }
    return render(request, 'bundy/index.html', context)

def clock(request):
    context = {}
    if request.method == "POST":
        person_id = request.POST.get("person_id")
        now = datetime.now()
        action = request.POST.get("action")
        image_file = request.FILES.get("image")

        if person_id and image_file:
            # Save the uploaded image to MEDIA_ROOT/uploads/
            upload_path = os.path.join("uploads", image_file.name)
            file_path = default_storage.save(upload_path, image_file)
            # Optionally, save a record to the database here
            person = Person.objects.get(id=person_id)
            timeRecord = TimeRecord(
                person=person, 
                time=now, 
                action=action,
                image=image_file)
            timeRecord.save()
            # Prepare context for rendering
            context["success"] = "Image uploaded successfully!"
            context["image_url"] = default_storage.url(file_path)
        else:
            context["error"] = "Please select a person and an image."
    return render(request, 'bundy/clock.html', context)


def about(request, person_id):
    return HttpResponse(f"About person {person_id} in Bundy app.")


def persons(request):
    return HttpResponse("List of persons in Bundy app.")


def sheet(request, year, month, day):
    context = {}
    persons = Person.objects.all()
    persons_list = []

    for person in persons:
        time_in_records_all = TimeRecord.objects.all().filter(
            person=person,
            action='IN',
            time__year=year,
            time__month=month,
            time__day=day).order_by('time')
        time_in_record = time_in_records_all.first() if time_in_records_all else None

        time_out_records_all = TimeRecord.objects.filter(
            person=person,
            action='OUT',
            time__year=year,
            time__month=month,
            time__day=day).order_by('time')
        time_out_record = time_out_records_all.last() if time_out_records_all else None

        persons_list.append({
            # 'date': f"{year}-{month:02d}-{day:02d}",
            'name': person.name,
            'image': person.image_tag(),
            'time_in': time_in_record.time_tag() if time_in_record else None,
            'image_in': time_in_record.image_tag() if time_in_record else "No Image",
            'time_out': time_out_record.time_tag() if time_out_record else None,
            'image_out': time_out_record.image_tag() if time_out_record else "No Image",
        })

    # context['persons_list'] = persons_list
    context = {'persons_list': persons_list}

    return render(request, "bundy/sheet.html", context)
    # return HttpResponse(template.render(context, request))
