from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label=''
        self.fields['username'].widget.attrs['placeholder'] = 'نام کاربری'
        self.fields['email'].label = ''
        self.fields['email'].widget.attrs['placeholder'] = 'ایمیل'
        self.fields['password1'].label = ''
        self.fields['password1'].widget.attrs['placeholder'] = 'رمز عبوز'
        self.fields['password2'].label=''
        self.fields['password2'].widget.attrs['placeholder'] = 'دوباره رمز عبور خود را وارد کنید'
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')