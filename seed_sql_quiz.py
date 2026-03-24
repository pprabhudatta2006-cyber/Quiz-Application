import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

from quiz_app.models import Category, Quiz, Question, Choice

def seed_sql_quiz():
    # Create or get category
    category, created = Category.objects.get_or_create(
        name="Database & SQL",
        defaults={"description": "Quizzes related to relational databases and SQL queries."}
    )

    # Create Quiz
    quiz, created = Quiz.objects.get_or_create(
        title="SQL Fundamentals",
        defaults={
            "description": "Test your knowledge of basic SQL syntax, queries, and database concepts.",
            "category": category,
            "quiz_type": "MCQ"
        }
    )

    # Questions and Choices
    quiz_data = [
        {
            "text": "Which SQL statement is used to extract data from a database?",
            "choices": [
                { "text": "EXTRACT", "is_correct": False },
                { "text": "SELECT", "is_correct": True },
                { "text": "OPEN", "is_correct": False },
                { "text": "GET", "is_correct": False },
            ]
        },
        {
            "text": "Which SQL keyword is used to sort the result-set?",
            "choices": [
                { "text": "SORT BY", "is_correct": False },
                { "text": "ORDER BY", "is_correct": True },
                { "text": "ALIGN BY", "is_correct": False },
                { "text": "GROUP BY", "is_correct": False },
            ]
        },
        {
            "text": "What does SQL stand for?",
            "choices": [
                { "text": "Strong Question Language", "is_correct": False },
                { "text": "Structured Query Language", "is_correct": True },
                { "text": "Structured Question Language", "is_correct": False },
                { "text": "Simple Query Language", "is_correct": False },
            ]
        },
        {
            "text": "Which SQL statement is used to update data in a database?",
            "choices": [
                { "text": "UPDATE", "is_correct": True },
                { "text": "MODIFY", "is_correct": False },
                { "text": "ALTER", "is_correct": False },
                { "text": "CHANGE", "is_correct": False },
            ]
        },
        {
            "text": "How do you select all columns from a table named 'Persons'?",
            "choices": [
                { "text": "SELECT [all] FROM Persons", "is_correct": False },
                { "text": "SELECT * FROM Persons", "is_correct": True },
                { "text": "SELECT Persons", "is_correct": False },
                { "text": "SELECT column FROM Persons", "is_correct": False },
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

    print("SQL quiz seeded successfully!")

if __name__ == '__main__':
    seed_sql_quiz()
