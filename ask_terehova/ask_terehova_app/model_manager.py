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
		# questions = Question.objects.all()
		questions = Question.objects.order_by('-publication_date')
		return questions

	def getAnswersQuestion(self, question_id):
		#try:
		question = Question.objects.get(pk=question_id)
		answer_count = Answer.objects.filter(question__pk=question_id)
		answers = answer_count.order_by('publication_date')
		return {'question': question, 'answers': answers}
		#except ObjectDoesNotExist:
		#	raise Http404


	def getQuestionTags(self, question_id):
		tags = Tag.objects.filter(question__pk=question_id)
		print tags
		return tags
	
	def getAnswerTags(self, answer_id):
		tags = Tag.objects.filter(answer__pk=answer_id)
		print tags
		return tags

	def getQuestionLike(self, question_id):
		question_like = QuestionLike.objects.filter(question__pk=question_id).count()
		print question_like
		return question_like

	def getAnswerLike (self, answer_id):
		answer_like = AnswerLike.objects.filter(answer__pk=answer_id).count()
		print answer_like
		return answer_like		
		
	def getTagQuestion(self, tag_text):
		try:
			question_tag = Tag.objects.get(text=tag_text)
			print question_tag
			return question_tag.question.all()
		except ObjectDoesNotExist:
			return []


	def questionInfo(self, question):
		question.tags = self.getQuestionTags(question.id)
		question.like = self.getQuestionLike(question.id)
		question.answer = len(self.getAnswersQuestion(question.id).get('answers'))
		return question

	def getLikeQuestion(self):
		sorted_questions = Question.objects.annotate(likes_count=Count('questionlike')).order_by('-likes_count')
		return sorted_questions
		
