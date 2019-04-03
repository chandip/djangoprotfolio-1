from django.shortcuts import render
from django.http import HttpResponse

from quizes.forms import QuizForm
from .models import Quiz
from courses.models import Course
from pages.models import Page


# Create your views here.
def quiz_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    quiz = Quiz.objects.all().first()  # get first quiz


    if request.POST.get('submit') != None:
        if request.POST.get('submit') == 'Next':
            quiz_last_id = request.session['quiz_last_id'] + 1
            try:
                quiz = Quiz.objects.filter(id=quiz_last_id).first()
            except Quiz.DoesNotExist:
                quiz = Quiz.objects.none()

    if request.POST.get('submit') != None:
        if request.POST.get('submit') == 'Check Answer':
            try:
                quiz = Quiz.objects.filter(id = request.session['quiz_last_id']).first()
            except Quiz.DoesNotExist:
                quiz = Quiz.objects.none()

    #allCourses = Course.objects.all()
    INITIAL = ''  # set initial selected choice is none
    is_correct_answer = ''  # no correct answer
    try:
        quiz_last_id = quiz.id
        correct_answer = quiz.correct_answer
        CHOICES = (
            (1, quiz.option1),
            (2, quiz.option2),
            (3, quiz.option3),
            (4, quiz.option4),
        )
        # when user submits the data
        if request.POST.get('choices') != None:
            if request.POST.get('submit') != 'Next':
                INITIAL = request.POST.get('choices')
                is_correct_answer = False
                if correct_answer == int(request.POST.get('choices')):
                    is_correct_answer = True

        form = QuizForm(CHOICES, INITIAL)
    except:
        return render(request,"quizes/result.html")
    request.session['quiz_last_id'] = quiz_last_id



    context ={
        'title' : quiz.question,
        'form' : form,
        'request_old' : request.POST,
        'is_correct_answer' : is_correct_answer,
        'correct_answer': correct_answer,
        'explanation': quiz.explanation,
        'quiz_last_id': request.session['quiz_last_id'],
    }

    return render(request,"quizes/index.html", context)



