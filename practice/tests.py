from django.test import TestCase
from practice.models import ToDoList,ToDoItem
from django.core.urlresolvers import reverse
#from django.test.utils import setup_test_enviornment
#setup_test_enviornment()
from django.shortcuts import get_object_or_404
from django.test import Client
client=Client()
# Create your tests here
class TodoItemAPITests(TestCase):
    def xtest_if_created_todoitem_successfully(self):
        todolist = ToDoList.objects.create(name='test list')
        client.post(reverse('todoitem', kwargs={'list_id':todolist.id}), {'name':'test item','complete':False})
        todoitems = ToDoItem.objects.all()
        self.assertEqual(todoitems.count(),1)
        self.assertEqual(todoitems[0].name,'test item')
class ToDoTest(TestCase):
	#editname
	def xtest_if_function_work(self):
		todolist=ToDoList.objects.create(name='test_list')
		todoitem=ToDoItem.objects.create(name='test1',todolist=todolist)
		print todolist.id
		print todoitem.todolist
		client.put(reverse('todoitemnew',kwargs={'item_id':todoitem.id}),{'name':'preet'})
		todoitems=ToDoItem.objects.all()
		self.assertEqual(todoitems[0].name,'preet')
	
	#complete
	def xtest_if_function_works(self):
		todolist=ToDoList.objects.create(name='test_list')
		todoitem=ToDoItem.objects.create(name='test1',todolist=todolist)
		print todolist.id
		print todoitem.todolist
		client.put(reverse('todoitemComplete',kwargs={'item_id':todoitem.id}),{'complete':True})
		todoitems=ToDoItem.objects.all()
		self.assertEqual(todoitems[0].complete,True)
	
	#get_complete
	def test_get_full(self):
		todolist=ToDoList.objects.create(name='test_list')
		todoitem=ToDoItem.objects.create(name='test1',todolist=todolist)
		client.get(reverse('todoitemComplete',kwargs={'item_id':todoitem.id}),{'complete':True})
		todoitems=ToDoItem.objects.all()
		self.assertEqual(todoitems[0].name,"test1")
class xToUnitTest(TestCase):
	#editname
	def xtest_if_it_is_working(self):
		todolist=ToDoList.objects.create(name='test_list')
		todoitem=ToDoItem.objects.create(name='test1',todolist=todolist)
		getItem=ToDoItem.objects.get(id=1)
		getItem.name="NEWNAME"
		getItem.save()
		todoitems=ToDoItem.objects.all()
		self.assertEqual(todoitems[0].name,"NEWNAME")
	
	#complete
	def xtest_if_this_unit_working(self):
		todolist=ToDoList.objects.create(name='test_list')
		todoitem=ToDoItem.objects.create(name='test1',todolist=todolist)
		getItem=ToDoItem.objects.get(id=1)
		getItem.complete=True
		getItem.save()
		todoitems=ToDoItem.objects.all()
		self.assertEqual(todoitems[0].complete,True)
	
	#get_complete
	def test_get(self):
		todolist=ToDoList.objects.create(name='test_list')
		todoitem=ToDoItem.objects.create(name='test1',todolist=todolist,complete=True)
		
		getItem=get_object_or_404(ToDoItem,id=1,complete=True)
