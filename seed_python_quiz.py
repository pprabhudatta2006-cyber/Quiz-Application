import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

from quiz_app.models import Category, Quiz, Question, Choice

def seed_python_quiz():
    # Create or get category
    category, created = Category.objects.get_or_create(
        name="Python Programming",
        defaults={"description": "Quizzes related to Python language and its ecosystem."}
    )

    # Create Quiz
    quiz, created = Quiz.objects.get_or_create(
        title="Python Basics Quiz",
        defaults={
            "description": "Test your fundamental knowledge of the Python programming language.",
            "category": category,
            "quiz_type": "MCQ"
        }
    )

    # Questions and Choices
    quiz_data = [
        {
            "text": "What is the correct file extension for Python files?",
            "choices": [
                { "text": ".python", "is_correct": False },
                { "text": ".pt", "is_correct": False },
                { "text": ".py", "is_correct": True },
                { "text": ".pyt", "is_correct": False },
            ]
        },
        {
            "text": "Which of the following describes Python?",
            "choices": [
                { "text": "Compiled Language", "is_correct": False },
                { "text": "Interpreted Language", "is_correct": True },
                { "text": "Machine Language", "is_correct": False },
                { "text": "Assembly Language", "is_correct": False },
            ]
        },
        {
            "text": "What is used to define a block of code in Python language?",
            "choices": [
                { "text": "Key", "is_correct": False },
                { "text": "Brackets", "is_correct": False },
                { "text": "Indentation", "is_correct": True },
                { "text": "Parentheses", "is_correct": False },
            ]
        },
        {
            "text": "Which keyword is used to define a function in Python?",
            "choices": [
                { "text": "function", "is_correct": False },
                { "text": "def", "is_correct": True },
                { "text": "func", "is_correct": False },
                { "text": "define", "is_correct": False },
            ]
        },
        {
            "text": "What is the output of `print(2 ** 3)`?",
            "choices": [
                { "text": "6", "is_correct": False },
                { "text": "8", "is_correct": True },
                { "text": "9", "is_correct": False },
                { "text": "Error", "is_correct": False },
            ]
        }
    ]

    # Insert into database
    for q_data in quiz_data:
        question, q_created = Question.objects.get_or_create(
            quiz=quiz,
            text=q_data["text"]
        )
        if q_created:
            for c_data in q_data["choices"]:
                Choice.objects.create(
                    question=question,
                    text=c_data["text"],
                    is_correct=c_data["is_correct"]
                )

    print("Python quiz seeded successfully!")

if __name__ == '__main__':
    seed_python_quiz()
