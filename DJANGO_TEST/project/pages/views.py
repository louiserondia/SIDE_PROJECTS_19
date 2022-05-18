from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Scan
import json

@csrf_exempt
def	home_page(request, *args, **kwargs):
	return render(request, "home.html", {})

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
	return render(request, "home.html", context)