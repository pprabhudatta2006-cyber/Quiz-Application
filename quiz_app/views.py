from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Category, Quiz, Question, Choice, Result
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'quiz_app/register.html', {'form': form})

@login_required
def home(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    
    if category_id:
        quizzes = Quiz.objects.filter(category_id=category_id).order_by('-created_at')
    else:
        quizzes = Quiz.objects.all().order_by('-created_at')
        
    return render(request, 'quiz_app/home.html', {
        'quizzes': quizzes,
        'categories': categories,
        'selected_category': int(category_id) if category_id else None
    })

@login_required
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    return render(request, 'quiz_app/quiz_detail.html', {'quiz': quiz})

@login_required
def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = quiz.questions.all()
    
    if request.method == 'POST':
        score = 0
        total_questions = questions.count()
        
        for q in questions:
            selected_choice_id = request.POST.get(f'question_{q.id}')
            if selected_choice_id:
                try:
                    choice = Choice.objects.get(pk=selected_choice_id)
                    if choice.is_correct:
                        score += 1
                except Choice.DoesNotExist:
                    pass
        
        result = Result.objects.create(
            user=request.user,
            quiz=quiz,
            score=score,
            total_questions=total_questions
        )
        return redirect('quiz_result', result_id=result.id)
        
    return render(request, 'quiz_app/take_quiz.html', {'quiz': quiz, 'questions': questions})

@login_required
def quiz_result(request, result_id):
    result = get_object_or_404(Result, pk=result_id, user=request.user)
    quiz = result.quiz
    questions = quiz.questions.all()
    return render(request, 'quiz_app/quiz_result.html', {'result': result, 'quiz': quiz, 'questions': questions})
