from django.shortcuts import render
from django.http import HttpResponse

from madzones.quizes.forms import QuizForm
from .models import Quiz
from madzones.courses.models import Course
from madzones.pages.models import Page


# Create your views here.
def quiz_view(request, *args, **kwargs): # *args, **kwargs
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
    correct_answers_flag = []
    try:
        quiz_last_id = quiz.id
        correct_answer = quiz.correct_answer

        correct_answer_values = []
        for correct_ans in correct_answer:
            correct_answer_values.append(correct_ans)

        CHOICES = (
            (1, quiz.option1),
            (2, quiz.option2),
            (3, quiz.option3),
            (4, quiz.option4),
        )
        # when user submits the data -- on next click
        if request.POST.get('choices') != None:
            if request.POST.get('submit') != 'Next':
                INITIAL = (request.POST.getlist('choices'))
                is_correct_answer = False

                #check against the right answer value
                for correct_ans_val in correct_answer_values:

                    for user_ans in request.POST.getlist('choices'):
                        if int(correct_ans_val) == int(user_ans):
                            correct_answers_flag.append(True)


                # now check if all answers are right or not
                if len(correct_answers_flag) == len(correct_answer_values):
                    is_correct_answer = True

        #check if answer is multiple choice or single
        count = len(quiz.correct_answer)
        form = QuizForm(CHOICES, INITIAL, False)

        if count > 1:
            form = QuizForm(CHOICES, INITIAL, True)
        else:
            correct_answer_values = correct_answer_values[0]


    except:
        return render(request,"quizes/result.html")
    request.session['quiz_last_id'] = quiz_last_id

    context ={
        'title' : quiz.question,
        'form' : form,
        'request_old' : request.POST,
        'is_correct_answer' : is_correct_answer,
        'correct_answer_values':  correct_answer_values,
        'correct_answer_count':  len(quiz.correct_answer),
        'correct_answer_count_a':  len(correct_answers_flag),
        'explanation': quiz.explanation,
        'quiz_last_id': request.session['quiz_last_id'],
    }

    return render(request,"quizes/index.html", context)



