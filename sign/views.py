from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from . import models
from django import forms
from .forms import RegisterForm , UserForm
from captcha.fields import CaptchaField


# Create your views here.
def index(request):
    pass
    return render(request,"index.html")

#登录函数
def login(request):
    if request.session.get('is_login',None):
        return HttpResponseRedirect('/index/')
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            workid = login_form.cleaned_data['work_id']
            password = login_form.cleaned_data['password']

            try:
                user = models.User.objects.get(work_id=workid)
                if user.password==password:
                    request.session['is_login'] = True
                    request.session['user_work_id'] = user.work_id
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return HttpResponseRedirect('/home/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在!"
        return render(request,'login/login.html',locals())
    login_form = UserForm()
    return render(request, 'login/login.html',locals())

#注册函数
def register(request):
    if request.session.get('is_login',None):
        return HttpResponseRedirect('/index/')
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容!"
        if register_form.is_valid():
            work_id = register_form.cleaned_data['work_id']
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2 :
                message = "两次输入的密码不同!"
                return render(request,'login/register.html',locals())
            else:
                same_work_id_user =models.User.objects.filter(work_id=work_id)
                if same_work_id_user:
                    message="该工号已存在，请重新输入工号!"
                    return render(request,'login/register.html',locals())
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:  #用户名唯一
                    message = "用户已经存在，请重新输入用户名!"
                    return render(request,'login/register.html',locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user: #邮箱地址唯一
                    message = "该邮箱地址已被注册，请使用别的邮箱！"
                    return render(request,'login/register.html',locals())


                #创建新用户
                new_user = models.User.objects.create()
                new_user.work_id = work_id
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return HttpResponseRedirect('/login/')
    register_form = RegisterForm()
    return render(request,'login/register.html',locals())

#退出函数  
def logout(request):
    if not request.session.get('is_login',None):
        return HttpResponseRedirect('/index/')
    request.session.flush()
    return HttpResponseRedirect('/login/')

#登录后的首页
def home(request):
    pass
    return render(request,'system/home.html')

#病患信息界面
def patient_info(request):
    pass
    return render(request,'system/patient_info.html')

#医生界面
@login_required
def doc_manage(request):
    patient_list = Patient.objects.all()
    uesrname=request.session.get('user','')
    return render(request,"doc_manage.html",{"user":uesrname,"patients":patient_list})