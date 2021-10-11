from django.shortcuts import redirect, render

from kwizwhiz.models import Answer, Category, Question, Quiz

def homepage(request):
    return render(request, "homepage.html")

def register(request):
    pass

def login(request):
    pass

def selectcategory(request):
    context = {
        "categories": Category.objects.all()
    }
    return render(request, "selectcategory.html", context)

def selectquiz(request, category_id):
    category = Category.objects.get(id = category_id)
    quizzes = Quiz.objects.all()
    context = {
        "quizzes": quizzes,
        "category": category
    }
    return render(request, "selectquiz.html", context)

def takequiz(request, quiz_id):
    count = 1
    quiz = Quiz.objects.get(id = quiz_id)
    questions = Question.objects.all()
    answers = Answer.objects.all()
    context = {
        "count": count,
        "answers": answers,
        "questions": questions,
        "quiz": quiz
    }
    return render(request, "takequiz.html", context)

def processquiz(request, quiz_id):
    if request.method == 'POST':
        quiz = Quiz.objects.get(id = quiz_id)
        total = 0
        wrong = 0
        correct = 0
        score = 0
        for question in quiz.questions.all():
            total += 1
            for answer in question.answers.all():
                if answer.is_right and answer.answer_text == request.POST['answer-'+str(question.id)]:              
                    correct += 1
                elif request.POST['answer-'+str(question.id)] == '':
                    return redirect('takequiz')
                elif not answer.is_right and answer.answer_text == request.POST['answer-'+str(question.id)]:
                    wrong += 1
        score = correct * 20
        request.session['score'] = score
        request.session['correct'] = correct
        request.session['wrong'] = wrong
        request.session['total'] = total
        return redirect('/results')
    else:
        return redirect('/')

def results(request):
    return render(request, "results.html")

def logout(request):
    request.session.flush()
    return redirect('/')

# Create your views here.
