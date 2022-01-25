from django import forms
from .models import User

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['id', 'pw', 'name']
        labels = {
          'user_id': '아이디', 
          'user_pw': '비밀번호', 
          'user_name': '이름'
        }