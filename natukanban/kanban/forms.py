from django import forms
from .models import Task

class AddTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'due_date', 'category', 'status')

class EditTaskForm(forms.Form):
    category_options = (
        ('urgente', 'Urgente'),
        ('importante', 'Importante'),
        ('precisa ser feito', 'Precisa ser feito')
    )
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)
    category = forms.ChoiceField(choices=category_options)