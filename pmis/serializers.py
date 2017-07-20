from rest_framework import serializers
from .models import Project, Phase, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','name', 'project_id', 'phase_id',
                  'start_date', 'end_date', 'estimated_duration','assignee_id', 'reviewer_id',]


class PhaseSerializer(serializers.ModelSerializer):
    task_phase = TaskSerializer(many=True,read_only=True)

    class Meta:
        model = Phase
        fields = ['id','name', 'project_id', 'start_date',
                  'end_date', 'estimated_duration', 'task_phase']


class ProjectSerializer(serializers.ModelSerializer):
    # task_project = TaskSerializer(many=True,read_only=True)
    phase_project = PhaseSerializer(many=True,read_only=True)

    class Meta:
        model = Project
        fields = ['id','name', 'project_code', 'start_date', 'end_date',
                  'estimated_duration', 'manager','phase_project']
    
    def create(self, payload):
        return super(ProjectSerializer,self).create(payload)

    def update(self,instance, payload):
        return super(ProjectSerializer,self).update(instance,payload)

    

        
