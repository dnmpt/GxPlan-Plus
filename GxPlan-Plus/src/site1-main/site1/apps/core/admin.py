from django.contrib import admin
from .models import Category, Project, Task, Note, Authorization, Message, Schedule

# Register your models here.
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Note)
admin.site.register(Authorization)
admin.site.register(Message)
admin.site.register(Schedule)