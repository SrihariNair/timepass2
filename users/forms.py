import datetime

from bootstrap_datepicker_plus import DatePickerInput
from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm


from .models import CustomUser,userPosts


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        now = datetime.datetime.now()
        fields = ('username', 'email', 'gender', 'security_question', 'answer', 'birth_date', 'image','resume')
        widgets={
            'birth_date' :DatePickerInput(
                options={
                    'maxDate':str(datetime.datetime.now()),
                }
            )
        }

class PostForm(forms.ModelForm):

    class Meta:
        model = userPosts
        fields = ('subject', 'text', 'from_date', 'to_date')
        widgets = {'text': forms.Textarea(attrs={'rows': 5,'cols':100,'style': 'resize:none;'}),
                   'from_date': DatePickerInput(),
                   'to_date': DatePickerInput()

                   }

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

