from django.db import models

# Create your models here.
#登录用户信息表

class User(models.Model):
    gender = (
        ('male','男'),
        ('female','女'),
    )
    name = models.CharField(max_length=128)
    work_id = models.IntegerField(unique=True,null=True)             #工号
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32,choices=gender,default='男')
    c_time = models.DateTimeField(auto_now_add=True)
  
    def __str__(self):
        return self.name
#医生信息表
class Doctor(models.Model):
    work_id = models.IntegerField()             #工号
    name = models.CharField(max_length=100)     #姓名
    sex = models.CharField(max_length=10)       #性别
    phone = models.CharField(max_length=16)     #手机号
    office = models.CharField(max_length=100)   #科室
    create_time = models.DateTimeField(auto_now=True)  # 创建时间（自动获取当前时间）

    def __str__(self):
        return self.name

#患者信息表
class Patient(models.Model):
    ID = models.ForeignKey(Doctor)              #关联医生的id
    id_card = models.IntegerField()             #身份证号
    name = models.CharField(max_length=100)     #姓名
    sex = models.CharField(max_length=10)       #性别
    create_time = models.DateTimeField(auto_now=True)  # 创建时间（自动获取当前时间）

    def __str__(self):
        return self.name