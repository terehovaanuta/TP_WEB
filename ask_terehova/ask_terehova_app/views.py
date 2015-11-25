from django.conf.urls import url
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

from model_manager import ModelManager


# Create your views here.

modelManager = ModelManager()


def paginate(list_questions, page_number):
    paginator = Paginator(list_questions, 5)

    try:
        questions = paginator.page(page_number)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.page_number)

    return {"questions": questions, "pages_amount": paginator.num_pages}


def base(request):
    return render(request, "base.html")

def render_question_page(request, page_number, questions, template_page):
    
    if len(questions) is 0:
        return render(request, template_page,{
            "error_message": "NO such tag"
            })

    page_number = request.GET.get('page')
    if page_number is not  None:
        page_number = int(page_number)
    paged_data = paginate(questions, page_number)
    paged_questions = paged_data["questions"]
    pages_amount = paged_data["pages_amount"]

    list_number_pages = [index for index in xrange(1, pages_amount + 1)]

    return render(request, template_page, {
        "questions": paged_questions, 
        "page_number": page_number, 
        "pages_amount": pages_amount,
        "list_number_pages": list_number_pages
    })


def main_page(request):
    questions = modelManager.getAllQuestions()
    return render_question_page(request, 1, questions, 'index.html')

def index(request, page_number):
    return render_question_page(request, page_number)
   
def question(request, question_id):

    try:
        result = modelManager.getQuestionById(question_id)
    except ObjectDoesNotExist:
        return render(request, "question.html", {
                "error_message": 'No such question'
            })

    return render(request, "question.html", {
        "question_id": question_id, 
        "question": result, 
        })

def ask(request):
    return render(request, "ask.html")


def login(request):
    return render(request, "login.html")

def signup(request): 
    return render(request, "signup.html")


def hot(request):
    question_like = modelManager.getLikeQuestion()
    return render_question_page(request, 1, question_like, "hot.html")

def tag(request, tag_text):
    question_tag = modelManager.getTagQuestion(tag_text)   
    return render_question_page(request, 1, question_tag)
    
@csrf_exempt
def get_post_params(request):
    result = ['Hello, Django!<br>']
    result.append('Post test:')
    result.append('<form method="post">')
    result.append('<input type="text" name = "test">')
    result.append('<input type="submit" value="Submit">')
    result.append('</form>')

    if request.method == 'GET':
        if request.GET.urlencode() != '':
            result.append('Get data:')
            #result.append(request.GET.urlencode())
            for key, value in request.GET.items():
                keyvalue=key+" = "+value
                result.append(keyvalue)

    if request.method == 'POST':
        result.append(request.POST.urlencode())
    return HttpResponse('<br>'.join(result))
