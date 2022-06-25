from pyexpat.errors import messages
from django.shortcuts import render
from qna.models import Question
from django.contrib.auth.models import User
from .forms import CustomUserChangeForm

def mypage(request):
     user=request.user
     #로그인한 유저이름과 글 작성자 이름이 동일한 글 필터링

     posts=Question.objects.filter(writer=user)
     return render(request,'users/mypage.html',{'posts':posts})

def mypage_view(request):
     if request.method == 'GET':
          return render(request, 'users/mapage.html') 
     

def mypage_update_view(request):
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance = request.user)

        if user_change_form.is_valid():
            user_change_form.save()
            messages.success(request, '회원정보가 수정되었습니다.')
            return render(request, 'users/mypage.html')
    else:
        user_change_form = CustomUserChangeForm(instance = request.user)

        return render(request, 'users/mypage.html', {'user_change_form':user_change_form})
