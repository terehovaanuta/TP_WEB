from django.db import models
from django.contrib.auth.models import User, UserManager, AbstractBaseUser
from datetime import datetime
from django.db.models import Count
# Create your models here.



class Profile(models.Model):
	user = models.OneToOneField(User)

	def __str__(self):
		return self.user.username


class QuestionLikeManager(models.Manager):
	def get_queryset(self):
		return super(QuestionLikeManager, self).get_queryset().annotate(like=Count('questionlike')).order_by('-like')

class QuestionAnswerManager(models.Manager):
	def get_queryset(self):
		return super(QuestionAnswerManager, self).get_queryset().all().answer_set.all()


class QuestionManager(models.Manager):
	def get_queryset(self):
		return super(QuestionManager, self).get_queryset().annotate(like=Count('questionlike')).prefetch_related('tag_set')


	def fill_questions(self, questions):
		for question in questions:
			question.tags = question.tag_set.all()
			question.answer_count = question.answer_set.count()
		return questions

	def get_questions(self):
		questions = self.get_queryset().order_by('-publication_date')
		return self.fill_questions(questions)

	def get_top_questions(self):
		questions = self.get_queryset().order_by('-like').filter(like__gte = 1)
		return self.fill_questions(questions)

	def get_question_with_answers(self, question_id):
		question = self.get_queryset().get(pk=question_id)
		question.tags = question.tag_set.all()
		question.answers = question.answer_set.annotate(like=Count('answerlike')).prefetch_related('tag_set').all()
		for answer in question.answers:
			answer.tags = answer.tag_set.all()
		return question

	def get_tag_questions(self, tag):

		questions = self.get_queryset().filter(tag__text=tag)
		return self.fill_questions(questions)



class Question(models.Model):
	text = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	user = models.ForeignKey(Profile)
	publication_date = models.DateTimeField(default=datetime.now)

	question_objects = QuestionManager()

	objects = models.Manager()

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
		return self.text 

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



