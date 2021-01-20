from django import forms
from .models import Todos,Project

class ListForm(forms.ModelForm):
    class Meta:
        model = Todos
        fields = ["title","description","actual_time","project_name"]
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["project_name"]

