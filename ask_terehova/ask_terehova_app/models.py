from django.db import models
from django.contrib.auth.models import User, UserManager, AbstractBaseUser
from datetime import datetime
# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(User)

	def __str__(self):
		return self.user.username

class Question(models.Model):
	text = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	user = models.ForeignKey(Profile)
	publication_date = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.title + ' by ' + self.user.user.username


class Answer(models.Model):
	question = models.ForeignKey(Question)
	user = models.ForeignKey(Profile, null=True)
	text = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	publication_date = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.title + ' by ' + self.user.user.username

class Tag(models.Model):
	text = models.CharField(max_length = 200)
	question = models.ManyToManyField(Question)
	answer = models.ManyToManyField(Answer)

	def __str__(self):
		return self.text #+ ' by ' + self.user.user.username

class QuestionLike(models.Model):
	question = models.ForeignKey(Question)
	user = models.ForeignKey(Profile, null=True)

	def __str__(self):
		return self.question.title + ' by ' + self.user.user.username

class AnswerLike(models.Model):	
	answer = models.ForeignKey(Answer)
	user = models.ForeignKey(Profile, null=True)

	def __str__(self):
		return self.answer.title + ' by ' + self.user.user.username



