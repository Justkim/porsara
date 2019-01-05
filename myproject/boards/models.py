from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Question(models.Model):
	title = models.CharField(max_length=400)
	content = models.TextField(max_length=4000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(null=True)
	created_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='questions_created')
	updated_by = models.ForeignKey(User, null=True,on_delete=models.PROTECT,related_name='questions_updated')


class Answer(models.Model):
	content = models.TextField(max_length=400)
	created_at = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(User,on_delete=models.PROTECT)
	parent_question= models.ForeignKey(Question,null=True,on_delete=models.PROTECT)







