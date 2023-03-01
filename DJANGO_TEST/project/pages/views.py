from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Scan, Event
import json

@csrf_exempt
def	home_page(request, *args, **kwargs):
	context = {
		'scans': Scan.objects.all(),
		'current_event': [ev for ev in Event.objects.all() if Event.is_current()]
	}
	print (current_event)
	return render(request, "home.html", context)

@csrf_exempt
def events_page(request, *args, **kwargs):
	if request.method == 'POST':
		res = request.body
		d = json.loads(res)
		participant = Participant(participant = d['id'])
		participant.save()

	context = {
		'scans': Scan.objects.all(),
		'events': Event.objects.all(),
	}
	return render(request, "events.html", context)

def	one_event(request, event_id, *args, **kwargs):
	one_event = Event.objects.get(id=event_id)
	context = {
		'scans': Scan.objects.all(),
		'one_events' : one_event,
	}
	return render(request, "one_event.html", context)

def drinks_page(request, *args, **kwargs):
	context = {
		'scans': Scan.objects.all()
	}
	return render(request, "drinks.html", context)

def add_user_page(request, *args, **kwargs):
	context = {
		'scans': Scan.objects.all()
	}
	return render(request, "add_user.html", context)

@csrf_exempt
def scan_page(request, *args, **kwargs):
	#Scan.objects.all().delete()
	if request.method == 'POST':
		res = request.body
		d = json.loads(res)
		scan = Scan(uid = d['id'])
		scan.save()

	context = {
		'scans': Scan.objects.all()
	}
	return render(request, "scan.html", context)