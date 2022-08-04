from django import forms
from .models import Task

class AddTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'due_date', 'category', 'status')