from django import forms
from captcha.fields import CaptchaField
 
#登录表单
class UserForm(forms.Form):
    work_id = forms.IntegerField(label="工号",
widget=forms.TextInput(attrs={'class': 'form-control'}))
    
 
    password = forms.CharField(label="密码", max_length=256,
widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    captcha = CaptchaField(label='验证码')





#注册表单
class RegisterForm(forms.Form):
    work_id = forms.IntegerField(label="工号",
widget=forms.TextInput(attrs={'class': 'form-control'}))

    username = forms.CharField(label="用户名", max_length=128,
widget=forms.TextInput(attrs={'class': 'form-control'}))
 
    password1 = forms.CharField(label="密码", max_length=256,
widget=forms.PasswordInput(attrs={'class': 'form-control'}))
 
    password2 = forms.CharField(label="确认密码", max_length=256,
widget=forms.PasswordInput(attrs={'class': 'form-control'}))
 
    email = forms.EmailField(label="邮箱地址",
widget=forms.EmailInput(attrs={'class': 'form-control'}))

    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    sex = forms.ChoiceField(label='性别', choices=gender)
 
    captcha = CaptchaField(label='验证码')