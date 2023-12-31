from django.db import models

class Task(models.Model):
  title = models.CharField(max_length = 100)
  due_date = models.DateTimeField()
  overdue = models.BooleanField(default=False)
  task_owners = models.JSONField(default=list, blank=True)
  priority = models.PositiveIntegerField(default=1)
  state = models.CharField(max_length = 15)
  
