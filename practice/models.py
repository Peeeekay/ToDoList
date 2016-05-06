from django.db import models

# Create your models here.
class ToDoList(models.Model):
	name=models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class ToDoItem(models.Model):
	name=models.CharField(max_length=100)
	todolist=models.ForeignKey(ToDoList)
	complete=models.BooleanField(default=False)
	def __unicode__(self):
		return self.name

	def comp(self):
		return self.complete

