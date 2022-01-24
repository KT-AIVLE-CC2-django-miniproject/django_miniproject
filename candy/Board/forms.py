from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import Board
from django.contrib.auth.hashers import check_password

class BoardForm(forms.ModelForm):
    # title = forms.CharField()
    class Meta:
        model = Board
        fields = ['postNum','title','contetn',
                    'id','pub_date','recuritment',]

# from .models import 