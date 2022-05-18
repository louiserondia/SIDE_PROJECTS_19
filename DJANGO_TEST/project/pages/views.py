from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def	home_page(request, *args, **kwargs):
	return render(request, "home.html", {})

@csrf_exempt
def scan_page(request, *args, **kwargs):
	if request.method == 'POST':
		res = request.body
		d = json.loads(res)
		print(d)
		return render(request, "home.html", {})
	else:
		return render(request, "home.html", {})