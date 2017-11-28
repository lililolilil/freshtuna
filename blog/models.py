from django.db import models
#다른 파일에 있는걸 추가하라는 뜻. django.utils 에 있는 timezone을 추가함. 
from django.utils import timezone 
from django_summernote import models as summer_model
from django_summernote import fields as summer_fields

# model(:객체)을 정의하는 코드 
#클래스의 이름의 첫글자는 대문자로 써야 함. models는 Post가 장고 모델임을 읫미함. 
#장고는 Post를 데이터베이스에 저장함. 
class Board(models.Model):
	title = models.CharField(max_length=40, null=False)
	title_ko = models.CharField(max_length=40, null=False)

	def __str__(self): 
		return self.title; 

class TagModel(models.Model):
	title = models.CharField(max_length=20, null=False)



class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200) #글자수가 제한된 텍스트 정의 
	content = models.TextField(default='')
	boardCd = models.ForeignKey(Board, default=1)
	hit = models.IntegerField(null=True, blank=True)
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	Tags = models.ManyToManyField(TagModel)
	comments = models.PositiveSmallIntegerField(default=0, null=True)

	def publish(self): 
		self.published_date = timezone.now()
		self.save()

	def __str__(self): #__ = (dunder : double under score) _ _  
		return self.title 

class Comment(models.Model):
	post = models.ForeignKey(Post)
	author = models.CharField(max_length=10)
	message = models.TextField(default='')
	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.updated_at = timezone.now()
		self.save()

class SummerNote(summer_model.Attachment):
	summer_field = summer_fields.SummernoteTextField(default='')

# class Post_logger(models.Model):
# 	entry = models.ForeignKey(Post, related_name='post_views')
# 	ip = models.CharField(max_length=40)
# 	session = models.CharField(max_length=40, null=True)
# 	created = models.DateTimeField(default=timezone.now)

# 	def __unicode__(self):
# 		return self.entry.title

# 	class Meta:
# 		verbose_name_plural = "Post Views"