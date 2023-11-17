from django.shortcuts import render
from django.shortcuts import HttpResponse
import json
from login.serializer import RegisterSerailizer
from login.models import RegisterationModel
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def Registration(request):
    if request.method=="POST":
        recieved_data=json.loads(request.body)
        print(recieved_data)
        serializer_check=RegisterSerailizer(data=recieved_data)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status":"Registeration adding success"}))
        else:
            return HttpResponse(json.dumps({"status":"Registeration adding Failed"}))
