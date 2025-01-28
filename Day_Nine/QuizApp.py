import random
import json

# Global variables
score = 0
questions = []

# Pre-written questions
default_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which programming language is known as the 'language of the web'?",
        "options": ["Python", "JavaScript", "C++", "Java"],
        "answer": "JavaScript"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["0", "1", "2", "3"],
        "answer": "2"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["Harper Lee", "Mark Twain", "J.K. Rowling", "Ernest Hemingway"],
        "answer": "Harper Lee"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["H2O", "O2", "CO2", "NaCl"],
        "answer": "H2O"
    }
]

# Menu Function
def display_menu():
    print("\nWelcome to the Quiz Game!")
    print("1. Play Quiz")
    print("2. Add Questions")
    print("3. View Scoreboard")
    print("4. Save and Exit")

# Load Questions
def load_questions(filename="questions.json"):
    global questions
    try:
        with open(filename, "r") as file:
            questions.extend(json.load(file))
        print("\nQuestions loaded successfully!")
    except FileNotFoundError:
        print("\nNo saved questions found. Using default questions.")
        questions.extend(default_questions)

# Save Questions
def save_questions(filename="questions.json"):
    with open(filename, "w") as file:
        json.dump(questions, file)
    print("\nQuestions saved successfully!")

# Play Quiz
def play_quiz():
    global score
    if not questions:
        print("\nNo questions available. Add questions first!")
        return
    
    print("\nStarting the quiz...")
    random.shuffle(questions)
    for question in questions:
        print(f"\nQuestion: {question['question']}")
        for i, option in enumerate(question['options'], start=1):
            print(f"{i}. {option}")
        try:
            user_answer = int(input("Your answer (1/2/3/4): "))
            if question['options'][user_answer - 1] == question['answer']:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {question['answer']}")
        except (IndexError, ValueError):
            print("Invalid input! Skipping question.")
    print(f"\nQuiz finished! Your score: {score}/{len(questions)}")

# Add Questions
def add_question():
    question_text = input("\nEnter the question: ")
    options = []
    for i in range(4):
        options.append(input(f"Enter option {i+1}: "))
    correct_answer = input("Enter the correct answer: ")
    questions.append({
        "question": question_text,
        "options": options,
        "answer": correct_answer
    })
    print("Question added successfully!")

# View Scoreboard
def view_scoreboard():
    print(f"\nYour current score: {score}")

# Main Program
if __name__ == "__main__":
    load_questions()

    while True:
        display_menu()
        menu_choice = input("\nSelect an option (1/2/3/4): ")

        if menu_choice == "1":
            play_quiz()
        elif menu_choice == "2":
            add_question()
        elif menu_choice == "3":
            view_scoreboard()
        elif menu_choice == "4":
            save_questions()
            print("\nGoodbye! Thanks for playing.")
            break
        else:
            print("\nInvalid choice! Please try again.")
