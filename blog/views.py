from django.shortcuts import render
from django.shortcuts import HttpResponse
import json
from blog.serializer import PostSerailizer
from blog.models import PostModel
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

# Create your views here.
@csrf_exempt
def addPost(request):
    if request.method=="POST":
        recieved_data=json.loads(request.body)
        print(recieved_data)
        serializer_check=PostSerailizer(data=recieved_data)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status":"Post adding success"}))
        else:
            return HttpResponse(json.dumps({"status":"Post adding Failed"}))
        

@csrf_exempt
def viewAll(request):
    if request.method=="POST":
        Postlist=PostModel.objects.all()
        serialize_data=PostSerailizer(Postlist,many=True)
        return HttpResponse(json.dumps(serialize_data.data))
    
@csrf_exempt
def viewMyPost(request):
    if request.method=="POST":
        recieved_data=json.loads(request.body)
        getUserid=recieved_data["userid"]
        data=list(PostModel.objects.filter(Q(userid__icontains=getUserid)).values())
        return HttpResponse(json.dumps(data))
    

