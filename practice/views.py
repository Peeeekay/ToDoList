from django.shortcuts import render, get_object_or_404

# Create your views here.
from practice.models import ToDoList, ToDoItem
from django.http import HttpResponse, JsonResponse, Http404, QueryDict

def todolist(request,num_id):
	if request.method =='POST':
		name=request.POST['name']
		List=ToDoList.objects.create(name=name)
	return JsonResponse({"name":name})


def todoitem(request,list_id):
	if request.method =="POST":
		name=request.POST['name']
		List=ToDoList.objects.get(id=list_id)
		Item=ToDoItem.objects.create(name=name, todolist=List)
	return JsonResponse({"name":name})
import yaml

def todoitemnew(request,item_id):
	if request.method =="PUT":
		item_id =int(item_id)
		n=request.body
		newName=yaml.load(n)
		get_item=ToDoItem.objects.get(id=item_id)
		get_item.name=newName['name']
		get_item.save()
	return JsonResponse({"name":newName})

def todoitemComplete(request,item_id):
	if request.method =="PUT":	
		n=request.body
		getItem=ToDoItem.objects.get(id=1)
		getItem.complete=True
		getItem.save()
		return JsonResponse({"name":n})
	
	elif request.method =="GET":	
		complete=request.GET['complete']
		getItem=get_object_or_404(ToDoItem,id=item_id,complete=True)
		return JsonResponse({"complete":complete})