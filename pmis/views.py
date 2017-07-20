# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Project, Phase, Task
from .serializers import ProjectSerializer, PhaseSerializer, TaskSerializer
from rest_framework.response import Response
from rest_framework.decorators import detail_route
# Create your views here.


class ProjectView(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    # @detail_route(methods=['get'], url_name='say')
    # def say_hi(self, request, pk=None):
    #     proj = self.get_object()
    #     ser = ProjectSerializer()
    #     ser.update(proj, {'name': "New Name"})
    #     return Response("Hello")

    @detail_route(methods=['put'])
    def say(self, request, pk=None):
        proj = self.get_object()
        ser = ProjectSerializer()
        res = ser.update(proj, {'name': request.data.get('new_name')})
        return Response("Success")


class PhaseView(ModelViewSet):
    queryset = Phase.objects.all()
    serializer_class = PhaseSerializer


class TaskView(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
