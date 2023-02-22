from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'image']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
           field.widget.attrs.update({'class':'form-control'})        
           field.help_text = ''

class HesapForm(ModelForm):
    class Meta:
        model=Hesap
        fields=['image', 'telefon']

    def __init__(self, *args, **kwargs):
        super(HesapForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})    
            field.help_text = ''