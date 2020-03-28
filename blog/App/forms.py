

from django import forms
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    username = forms.CharField(min_length=2,required=True,error_messages={
        'required':'用户名必须输入',
        'min_length':'用户名至少2个字符',
    })
    password = forms.CharField(min_length=3,required=True,error_messages={
        'required': '密码必须输入',
        'min_length': '密码至少3个字符',
    })
    confirm = forms.CharField(min_length=3,required=True,error_messages={
        'required':'密码必须输入',
        'min_length': '密码至少3个字符',
    })
    phone = forms.CharField(min_length=11,max_length=11,required=False,error_messages={
        'min_length=11':'手机号为11位',
        'max_length=11': '手机号为11位',
    })
    email = forms.CharField(required=False)

    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('confirm'):
            raise ValidationError({'confirm':'两次密码输入不一致'})
        return self.cleaned_data

