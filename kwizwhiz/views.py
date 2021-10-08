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
        questions = Question.objects.filter(quiz = quiz)
        options = Answer.objects.filter(question = questions)
        # right = Answer.objects.filter(is_right = True)
        for option in options:
            user_answer = Answer.objects.filter(answer_text = request.POST.get('answer-'+{option.id}))   
        # true_answer = request.POST['return']
        # for option in options:
        #     if option == Answer.objects.get(is_right = True):
        #         true_answer = option
        total = 0
        wrong = 0
        correct = 0
        score = 0
        for question in questions:
            total += 1
            print(question.title)
            print()
            print(user_answer)
            if user_answer[0] == True:
                true_answer = request.POST['return']
                print(true_answer)
                correct += 1
            else:
                wrong += 1

            # if request.POST['answer'] == request.POST.get('answer.is_right'):
            #     correct += 1
            # elif request.POST['answer'] == '' or request.POST['answer'] != request.POST.get('answer.is_right'):
            #     wrong += 1
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
