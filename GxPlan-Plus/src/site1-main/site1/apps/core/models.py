from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

# Create your models here.

STATUS_CANCELLED = 0
STATUS_SCHEDULED = 1
STATUS_IN_PROGRESS = 2
STATUS_DONE = 3

STATUS = ((STATUS_CANCELLED,'Canceled'),(STATUS_SCHEDULED,'Scheduled'),(STATUS_IN_PROGRESS,'In Progress'),(STATUS_DONE,'Done')) # Tuple for status of project ...

class Category(models.Model):
    'Model for the category (i.e. type) of projects'
    name = models.CharField(max_length=20)
    author = models.ForeignKey(to=User, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Project(models.Model):
    'Model for Projects'
    categ = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    notes = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    image = models.ImageField(upload_to="media", null=True,blank=True)
    status = models.IntegerField(choices=STATUS, default = STATUS_SCHEDULED)

    def __str__(self):
        return self.categ.name + " | " + self.name

class Task(models.Model):
    'Model for Tasks'
    #TaskID INTEGER PRIMARY KEY AUTOINCREMENT ,ProjIDD INT, TaskNome CHAR, TaskValor INT, TaskCompliance INT, TaskUrgencia INT, TaskEsforco INT, TaskPrioridade REAL, TaskCusto INT, TaskFeito BIT, TaskStart INT, TaskEnd INT
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    value = models.PositiveSmallIntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    compliance = models.PositiveSmallIntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    urgency = models.PositiveSmallIntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    effort = models.PositiveSmallIntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    priority = models.FloatField(default=10)
    cost = models.IntegerField(default = 0, validators=[MinValueValidator(0), MaxValueValidator(1000000000)])
    progress = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    status = models.IntegerField(choices=STATUS, default = STATUS_SCHEDULED)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
     
    def __str__(self):
        return self.project.name + " # " + self.name

class Note(models.Model):
    'Model for task notes'
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    note_text = models.TextField()
    original_date = models.DateTimeField(auto_now_add=True)
    revision_date = models.DateTimeField(null=True)
    author = models.ForeignKey(to=User,blank=True, null=True, on_delete=models.SET_NULL) 

    def __str__(self):
        return self.task.name + " ! " + self.title


class Authorization(models.Model):
    'Model for user authorization in Tasks'
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user_authorized = models.CharField(max_length=200)

    def __str__(self):
        return self.task.name + " @ " + self.user_authorized


class Message(models.Model):
    'Model for messages in Tasks'
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    author = models.ForeignKey(to=User,blank=True, null=True,on_delete=models.SET_NULL)
    pub_date = models.DateTimeField(auto_now_add=True)
    msgText = models.TextField()

    def __str__(self):
        return self.task.name + " - " + self.msgText


class Schedule(models.Model):
    _date = models.DateTimeField()
    _hour = models.PositiveSmallIntegerField(default=9, validators=[MinValueValidator(0), MaxValueValidator(24)])
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.date.strftime("%d/%m/%Y ") + str(self._hour)
