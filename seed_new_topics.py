import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

from quiz_app.models import Category, Quiz, Question, Choice

def seed_more_quizzes():
    # Helper to add a quiz with its questions
    def add_quiz_with_questions(category_name, quiz_title, quiz_desc, questions_data):
        category, _ = Category.objects.get_or_create(
            name=category_name,
            defaults={"description": f"Quizzes related to {category_name}."}
        )

        quiz, _ = Quiz.objects.get_or_create(
            title=quiz_title,
            defaults={
                "description": quiz_desc,
                "category": category,
                "quiz_type": "MCQ"
            }
        )

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
        print(f"Added {added_count} questions to '{quiz_title}'!")

    # 1. Modelling
    modelling_questions = [
        {
            "text": "Who is known as the first supermodel?",
            "choices": [
                { "text": "Cindy Crawford", "is_correct": False },
                { "text": "Janice Dickinson", "is_correct": True },
                { "text": "Naomi Campbell", "is_correct": False },
                { "text": "Kate Moss", "is_correct": False },
            ]
        },
        {
            "text": "What does 'haute couture' mean in the fashion industry?",
            "choices": [
                { "text": "High fashion / Custom-fitted clothing", "is_correct": True },
                { "text": "Ready-to-wear clothing", "is_correct": False },
                { "text": "Mass-produced fashion", "is_correct": False },
                { "text": "Street style", "is_correct": False },
            ]
        },
        {
            "text": "Which magazine famously features the September Issue?",
            "choices": [
                { "text": "Elle", "is_correct": False },
                { "text": "Cosmopolitan", "is_correct": False },
                { "text": "Vogue", "is_correct": True },
                { "text": "Harper's Bazaar", "is_correct": False },
            ]
        },
        {
            "text": "What is a 'comp card' (zed card) used for by fashion models?",
            "choices": [
                { "text": "A business card with model stats and photos", "is_correct": True },
                { "text": "A credit card for buying clothes", "is_correct": False },
                { "text": "A ticket to enter a runway show", "is_correct": False },
                { "text": "A scoring card by judges", "is_correct": False },
            ]
        },
        {
            "text": "Which modeling agency was founded by Eileen Ford?",
            "choices": [
                { "text": "Elite Model Management", "is_correct": False },
                { "text": "IMG Models", "is_correct": False },
                { "text": "Next Management", "is_correct": False },
                { "text": "Ford Models", "is_correct": True },
            ]
        }
    ]

    # 2. Stranger Things
    stranger_things_questions = [
        {
            "text": "In what fictional town does Stranger Things mostly take place?",
            "choices": [
                { "text": "Riverdale", "is_correct": False },
                { "text": "Hawkins", "is_correct": True },
                { "text": "Derry", "is_correct": False },
                { "text": "Sunnydale", "is_correct": False },
            ]
        },
        {
            "text": "What is Eleven's real name according to the show's lore?",
            "choices": [
                { "text": "Maxine", "is_correct": False },
                { "text": "Jane", "is_correct": True },
                { "text": "Sarah", "is_correct": False },
                { "text": "Nancy", "is_correct": False },
            ]
        },
        {
            "text": "What game are the boys playing in the very first episode?",
            "choices": [
                { "text": "Monopoly", "is_correct": False },
                { "text": "Magic: The Gathering", "is_correct": False },
                { "text": "Dungeons & Dragons", "is_correct": True },
                { "text": "Warhammer", "is_correct": False },
            ]
        },
        {
            "text": "What does Dustin keep as a 'pet' in season 2?",
            "choices": [
                { "text": "A Demogorgon", "is_correct": False },
                { "text": "A Demodog (Dart)", "is_correct": True },
                { "text": "A Mind Flayer spawn", "is_correct": False },
                { "text": "A bat", "is_correct": False },
            ]
        },
        {
            "text": "Who runs the Scoops Ahoy ice cream parlor with Steve Harrington?",
            "choices": [
                { "text": "Nancy Wheeler", "is_correct": False },
                { "text": "Robin Buckley", "is_correct": True },
                { "text": "Chrissy Cunningham", "is_correct": False },
                { "text": "Max Mayfield", "is_correct": False },
            ]
        }
    ]

    # 3. Harry Potter
    harry_potter_questions = [
        {
            "text": "What is the name of Harry Potter's owl?",
            "choices": [
                { "text": "Pigwidgeon", "is_correct": False },
                { "text": "Errol", "is_correct": False },
                { "text": "Hedwig", "is_correct": True },
                { "text": "Crookshanks", "is_correct": False },
            ]
        },
        {
            "text": "Which house does the Sorting Hat originally want to put Harry in?",
            "choices": [
                { "text": "Gryffindor", "is_correct": False },
                { "text": "Slytherin", "is_correct": True },
                { "text": "Ravenclaw", "is_correct": False },
                { "text": "Hufflepuff", "is_correct": False },
            ]
        },
        {
            "text": "What spell is used to disarm an opponent?",
            "choices": [
                { "text": "Expelliarmus", "is_correct": True },
                { "text": "Stupefy", "is_correct": False },
                { "text": "Avada Kedavra", "is_correct": False },
                { "text": "Lumos", "is_correct": False },
            ]
        },
        {
            "text": "Who is the Half-Blood Prince?",
            "choices": [
                { "text": "Tom Riddle", "is_correct": False },
                { "text": "Sirius Black", "is_correct": False },
                { "text": "Harry Potter", "is_correct": False },
                { "text": "Severus Snape", "is_correct": True },
            ]
        },
        {
            "text": "What are the three core components used in wand-making by Ollivander?",
            "choices": [
                { "text": "Dragon heartstring, Phoenix feather, Unicorn hair", "is_correct": True },
                { "text": "Basilisk fang, Dementor cloth, Phoenix feather", "is_correct": False },
                { "text": "Unicorn hair, Thestral tail-hair, Troll whisker", "is_correct": False },
                { "text": "Phoenix feather, Veela hair, Dragon scale", "is_correct": False },
            ]
        }
    ]

    add_quiz_with_questions(
        category_name="Fashion & Modelling",
        quiz_title="Supermodels & High Fashion",
        quiz_desc="Test your fashion industry knowledge, from legendary supermodels to basic terminology.",
        questions_data=modelling_questions
    )

    add_quiz_with_questions(
        category_name="Pop Culture & Movies",
        quiz_title="Stranger Things Trivia",
        quiz_desc="How much do you really know about Hawkins and the Upside Down?",
        questions_data=stranger_things_questions
    )

    add_quiz_with_questions(
        category_name="Fantasy & Books",
        quiz_title="Harry Potter Ultimate Quiz",
        quiz_desc="From the Sorcerer's Stone to the Deathly Hallows. Check your wizarding world trivia!",
        questions_data=harry_potter_questions
    )

if __name__ == '__main__':
    seed_more_quizzes()
