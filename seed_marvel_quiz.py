import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

from quiz_app.models import Category, Quiz, Question, Choice

def seed_marvel_quiz():
    category, created = Category.objects.get_or_create(
        name="Pop Culture & Movies",
        defaults={"description": "Test your knowledge on movies, comics, and pop culture."}
    )

    quiz, created = Quiz.objects.get_or_create(
        title="Marvel Cinematic Universe Quiz",
        defaults={
            "description": "How well do you know the MCU? Take this ultimate Marvel trivia quiz!",
            "category": category,
            "quiz_type": "MCQ"
        }
    )

    marvel_questions = [
        {
            "text": "What is Captain America's shield made of?",
            "choices": [
                { "text": "Adamantium", "is_correct": False },
                { "text": "Vibranium", "is_correct": True },
                { "text": "Promethium", "is_correct": False },
                { "text": "Carbonadium", "is_correct": False },
            ]
        },
        {
            "text": "Who is the Winter Soldier?",
            "choices": [
                { "text": "Steve Rogers", "is_correct": False },
                { "text": "Sam Wilson", "is_correct": False },
                { "text": "Bucky Barnes", "is_correct": True },
                { "text": "Baron Zemo", "is_correct": False },
            ]
        },
        {
            "text": "What is the name of Thor's hammer?",
            "choices": [
                { "text": "Stormbreaker", "is_correct": False },
                { "text": "Mjolnir", "is_correct": True },
                { "text": "Gungnir", "is_correct": False },
                { "text": "Jarnbjorn", "is_correct": False },
            ]
        },
        {
            "text": "Which Infinity Stone is hidden on Vormir?",
            "choices": [
                { "text": "Time Stone", "is_correct": False },
                { "text": "Reality Stone", "is_correct": False },
                { "text": "Mind Stone", "is_correct": False },
                { "text": "Soul Stone", "is_correct": True },
            ]
        },
        {
            "text": "Who said the famous line, 'I am Iron Man'?",
            "choices": [
                { "text": "Tony Stark", "is_correct": True },
                { "text": "Thanos", "is_correct": False },
                { "text": "Nick Fury", "is_correct": False },
                { "text": "Obadiah Stane", "is_correct": False },
            ]
        },
        {
            "text": "What species is Groot?",
            "choices": [
                { "text": "Kree", "is_correct": False },
                { "text": "Skrull", "is_correct": False },
                { "text": "Flora colossus", "is_correct": True },
                { "text": "Sovereign", "is_correct": False },
            ]
        },
        {
            "text": "What is the name of the AI that Tony Stark created to replace J.A.R.V.I.S.?",
            "choices": [
                { "text": "E.D.I.T.H.", "is_correct": False },
                { "text": "F.R.I.D.A.Y.", "is_correct": True },
                { "text": "H.O.M.E.R.", "is_correct": False },
                { "text": "U.L.T.R.O.N.", "is_correct": False },
            ]
        },
        {
            "text": "Who is T'Challa's sister?",
            "choices": [
                { "text": "Okoye", "is_correct": False },
                { "text": "Nakia", "is_correct": False },
                { "text": "Shuri", "is_correct": True },
                { "text": "Ramonda", "is_correct": False },
            ]
        },
        {
            "text": "In which movie did Spider-Man make his first appearance in the MCU?",
            "choices": [
                { "text": "Spider-Man: Homecoming", "is_correct": False },
                { "text": "Avengers: Age of Ultron", "is_correct": False },
                { "text": "Avengers: Infinity War", "is_correct": False },
                { "text": "Captain America: Civil War", "is_correct": True },
            ]
        },
        {
            "text": "What is the name of Peter Quill's ship in the first Guardians of the Galaxy movie?",
            "choices": [
                { "text": "The Benatar", "is_correct": False },
                { "text": "The Milano", "is_correct": True },
                { "text": "The Bowie", "is_correct": False },
                { "text": "The Eclector", "is_correct": False },
            ]
        }
    ]

    added_count = 0
    for q_data in marvel_questions:
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

    print(f"Added {added_count} Marvel questions successfully!")

if __name__ == '__main__':
    seed_marvel_quiz()
