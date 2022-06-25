from django.urls import path
from .views import *

app_name = "users"
urlpatterns = [
  path('mypage/', mypage, name="mypage"),
  path('mypage/update/', mypage_update_view, name='profile_update'),

]
