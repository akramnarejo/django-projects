from django import forms
from .models import Task
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        
        widgets = {
            'task':forms.TextInput(attrs={
                'id':'task-text',
                'required':True,
                'placeholder':'Add Task'
            }),
        }
