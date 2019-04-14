from django import forms
from module_app.models import Module


class ModuleForm(forms.ModelForm):

    class Meta:
        model = Module
        fields = ['project', 'name', 'describe']
