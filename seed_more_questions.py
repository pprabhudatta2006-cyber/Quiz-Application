import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

from quiz_app.models import Quiz, Question, Choice

def seed_more_questions():
    # Helper function to add questions
    def add_questions_to_quiz(quiz_title, questions_data):
        try:
            quiz = Quiz.objects.get(title=quiz_title)
            added_count = 0
            for q_data in questions_data:
                question, q_created = Question.objects.get_or_create(
                    quiz=quiz,
                    text=q_data["text"]
                )
                if q_created:
                    added_count += 1
                    for c_data in q_data["choices"]:
                        Choice.objects.create(
                            question=question,
                            text=c_data["text"],
                            is_correct=c_data["is_correct"]
                        )
            print(f"Added {added_count} new questions to '{quiz_title}'.")
        except Quiz.DoesNotExist:
            print(f"Quiz '{quiz_title}' not found.")

    python_questions = [
        {
            "text": "What is the correct way to create a list in Python?",
            "choices": [
                { "text": "list = {}", "is_correct": False },
                { "text": "list = ()", "is_correct": False },
                { "text": "list = []", "is_correct": True },
                { "text": "list = //", "is_correct": False },
            ]
        },
        {
            "text": "Which method can be used to return a string in upper case letters?",
            "choices": [
                { "text": "upper()", "is_correct": True },
                { "text": "uppercase()", "is_correct": False },
                { "text": "upperCase()", "is_correct": False },
                { "text": "toUpperCase()", "is_correct": False },
            ]
        },
        {
            "text": "Which collection is ordered, changeable, and allows duplicate members?",
            "choices": [
                { "text": "Set", "is_correct": False },
                { "text": "Dictionary", "is_correct": False },
                { "text": "Tuple", "is_correct": False },
                { "text": "List", "is_correct": True },
            ]
        },
        {
            "text": "How do you start writing a while loop in Python?",
            "choices": [
                { "text": "while x > y {", "is_correct": False },
                { "text": "while x > y:", "is_correct": True },
                { "text": "while (x > y)", "is_correct": False },
                { "text": "x > y while {", "is_correct": False },
            ]
        },
        {
            "text": "What is the correct syntax to output the type of a variable or object in Python?",
            "choices": [
                { "text": "print(typeof(x))", "is_correct": False },
                { "text": "print(typeOf(x))", "is_correct": False },
                { "text": "print(type(x))", "is_correct": True },
                { "text": "print(typeof x)", "is_correct": False },
            ]
        }
    ]

    sql_questions = [
        {
            "text": "Which operator is used to search for a specified pattern in a column?",
            "choices": [
                { "text": "GET", "is_correct": False },
                { "text": "LIKE", "is_correct": True },
                { "text": "FROM", "is_correct": False },
                { "text": "EXTRACT", "is_correct": False },
            ]
        },
        {
            "text": "Which SQL statement is used to insert new data in a database?",
            "choices": [
                { "text": "INSERT NEW", "is_correct": False },
                { "text": "ADD RECORD", "is_correct": False },
                { "text": "ADD NEW", "is_correct": False },
                { "text": "INSERT INTO", "is_correct": True },
            ]
        },
        {
            "text": "How can you select all the records from a table named 'Persons' where the value of the column 'FirstName' starts with an 'a'?",
            "choices": [
                { "text": "SELECT * FROM Persons WHERE FirstName='%a%'", "is_correct": False },
                { "text": "SELECT * FROM Persons WHERE FirstName LIKE '%a'", "is_correct": False },
                { "text": "SELECT * FROM Persons WHERE FirstName='a'", "is_correct": False },
                { "text": "SELECT * FROM Persons WHERE FirstName LIKE 'a%'", "is_correct": True },
            ]
        },
        {
            "text": "The OR operator displays a record if ANY conditions listed are true. The AND operator displays a record if ALL of the conditions listed are true",
            "choices": [
                { "text": "True", "is_correct": True },
                { "text": "False", "is_correct": False },
                { "text": "None", "is_correct": False },
                { "text": "Depends on the Database", "is_correct": False },
            ]
        },
        {
            "text": "Which SQL statement is used to delete data from a database?",
            "choices": [
                { "text": "COLLAPSE", "is_correct": False },
                { "text": "REMOVE", "is_correct": False },
                { "text": "DELETE", "is_correct": True },
                { "text": "DROP", "is_correct": False },
            ]
        }
    ]

    add_questions_to_quiz("Python Basics Quiz", python_questions)
    add_questions_to_quiz("SQL Fundamentals", sql_questions)

if __name__ == '__main__':
    seed_more_questions()
