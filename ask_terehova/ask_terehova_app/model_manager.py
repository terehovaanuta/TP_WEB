from models import Profile, Question, Answer, Tag, QuestionLike, AnswerLike
from django.contrib.auth.models import User, UserManager, AbstractBaseUser
from django.db.models import Count

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

class ModelManager:

	def createProfile(self):
		user = User.objects.create_user(username='test', password='123')
		user.save()
		profile = Profile(user=user)
		profile.save()

	def getAllQuestions(self):
		return Question.question_objects.get_questions()

	def getQuestionById(self, question_id):
		return Question.question_objects.get_question_with_answers(question_id)

	def getLikeQuestion(self):
		return Question.question_objects.get_top_questions()

	def getTagQuestion(self, tag):
		return Question.question_objects.get_tag_questions(tag)


		
