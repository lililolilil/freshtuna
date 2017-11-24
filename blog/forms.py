from django import forms
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget
from django_summernote import fields as summer_fields
from .models import Post,SummerNote

EMPTY_TITLE_ERROR = "제목을 입력하세요"
EMPTY_CONTENT_ERROR = "내용을 입력하세요"
EMPTY_USERNAME_ERROR = "사용자 아이디를 입력하세요"
EMPTY_EMAIL_ERROR = "EMAIL주소를 입력하세요"
EMPTY_PASSWORD_ERROR = "비밀번호를 입력하세요"

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','content',)
		widgets = {
		'title': forms.TextInput({'class':'form-control'}),
		'content': SummernoteWidget({'width': '100%'}),
		}
		error_messages = {
		'title': {'required': EMPTY_TITLE_ERROR},
		'content': {'required': EMPTY_CONTENT_ERROR}
		}

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password']
		error_messages = {
			'username': {'required': EMPTY_USERNAME_ERROR},
			'email': {'required': EMPTY_EMAIL_ERROR},
			'password': {'required': EMPTY_PASSWORD_ERROR}
		}

class LoginForm(forms.ModelForm):
	class Meta: 
		model = User 
		fields = ['username', 'password']
		error_messages = {
			'username': {'required': EMPTY_USERNAME_ERROR},
			'password': {'required': EMPTY_PASSWORD_ERROR}
		}