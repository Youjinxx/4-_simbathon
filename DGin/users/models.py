
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .choice import *

class mypage(models.Model):
   user=models.OneToOneField(User,on_delete=models.CASCADE)

class User(AbstractBaseUser, PermissionsMixin):
    
    objects = BaseUserManager()

    user_id = models.CharField(max_length=17, verbose_name="아이디", unique=True)
    password = models.CharField(max_length=256, verbose_name="비밀번호")   
    name = models.CharField(max_length=8, verbose_name="이름", null=True)
    student_id = models.IntegerField(verbose_name="학번", null=True)
    grade = models.CharField(choices=GRADE_CHOICES, max_length=18, verbose_name="학년", null=True)
    department = models.CharField(choices=DEPARTMENT_CHOICES, max_length=24, verbose_name="학과", null=True)
    
    

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['email']
    
    def __str__(self):
        return self.user_id

class UserManager(BaseUserManager):

    def create_user(self, user_id, password, name, student_id, grade, department, auth):
        if not user_id:
            raise ValueError('user_id Required!')

        user = self.model(
            user_id = user_id,
            
            name = name,
            student_id = student_id,
            grade = grade,
            department = department,
            
            
           
        )

        user.set_password(password)
        user.save(using=self._db)
        return user