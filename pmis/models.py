# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):

    name = models.CharField("Name", max_length=512)
    project_code = models.CharField("Project Code", unique=True, max_length=32)
    start_date = models.DateTimeField("Start Date")
    end_date = models.DateTimeField("End Date")
    estimated_duration = models.DurationField("Estimated Duration")
    manager = models.ForeignKey(
        User, related_name="manager", on_delete=models.CASCADE)

    class Meta:
        db_table = 'project'


class Phase(models.Model):
    name = models.CharField("Name", max_length=512)
    project_id = models.ForeignKey(
        Project, related_name="phase_project", on_delete=models.CASCADE)
    start_date = models.DateTimeField("Start Date")
    end_date = models.DateTimeField("End Date")
    estimated_duration = models.DurationField("Estimated Duration")

    class Meta:
        db_table = 'project_phase'


class Task(models.Model):
    name = models.CharField("Name", max_length=512)
    project_id = models.ForeignKey(
        Project, related_name="task_project", on_delete=models.CASCADE)
    phase_id = models.ForeignKey(
        Phase, related_name="task_phase", on_delete=models.CASCADE)
    assignee_id = models.ForeignKey(
        User, related_name="assignee", on_delete=models.CASCADE)
    reviewer_id = models.ForeignKey(
        User, related_name="reviewer", on_delete=models.CASCADE)
    start_date = models.DateTimeField("Start Date")
    end_date = models.DateTimeField("End Date")
    estimated_duration = models.DurationField("Estimated Duration")

    class Meta:
        db_table = 'project_task'
