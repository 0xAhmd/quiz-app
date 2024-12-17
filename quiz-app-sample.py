
def get_quiz_data():
    """
    Hardcoded quiz data with categories, difficulties, and questions.
    """
    return {
        "Science": {
            "easy": [
                {
                    "question": "What planet is known as the Red Planet?",
                    "choices": ["Earth", "Mars", "Jupiter", "Saturn"],
                    "answer": "Mars",
                },
                {
                    "question": "What is H2O commonly known as?",
                    "choices": ["Hydrogen", "Water", "Oxygen", "Helium"],
                    "answer": "Water",
                },
            ],
            "medium": [
                {
                    "question": "What gas do plants absorb from the atmosphere?",
                    "choices": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
                    "answer": "Carbon Dioxide",
                },
                {
                    "question": "What is the chemical symbol for gold?",
                    "choices": ["Au", "Ag", "Gd", "Go"],
                    "answer": "Au",
                },
            ],
            "hard": [
                {
                    "question": "What is the powerhouse of the cell?",
                    "choices": ["Nucleus", "Ribosome", "Mitochondria", "Golgi Apparatus"],
                    "answer": "Mitochondria",
                },
                {
                    "question": "What is the speed of light in a vacuum (in m/s)?",
                    "choices": ["3 x 10^8", "5 x 10^6", "3 x 10^5", "1 x 10^7"],
                    "answer": "3 x 10^8",
                },
            ],
        },
        "History": {
            "easy": [
                {
                    "question": "Who was the first President of the United States?",
                    "choices": ["George Washington", "Abraham Lincoln", "John Adams", "Thomas Jefferson"],
                    "answer": "George Washington",
                },
                {
                    "question": "In what year did World War II end?",
                    "choices": ["1940", "1945", "1950", "1939"],
                    "answer": "1945",
                },
            ],
            "medium": [
                {
                    "question": "Who discovered America?",
                    "choices": ["Christopher Columbus", "Marco Polo", "Ferdinand Magellan", "Vasco da Gama"],
                    "answer": "Christopher Columbus",
                },
                {
                    "question": "What was the name of the ship on which the Pilgrims traveled to America in 1620?",
                    "choices": ["Mayflower", "Santa Maria", "Endeavour", "Beagle"],
                    "answer": "Mayflower",
                },
            ],
            "hard": [
                {
                    "question": "Which treaty ended World War I?",
                    "choices": ["Treaty of Paris", "Treaty of Versailles", "Treaty of Ghent", "Treaty of Tordesillas"],
                    "answer": "Treaty of Versailles",
                },
                {
                    "question": "Who was the British Prime Minister during World War II?",
                    "choices": ["Winston Churchill", "Neville Chamberlain", "Clement Attlee", "Harold Macmillan"],
                    "answer": "Winston Churchill",
                },
            ],
        },
    }
def start_quiz(questions):
    """
    Starts the quiz and keeps track of the score.
    """
    score = 0
    for idx, q in enumerate(questions):
        print(f"\nQuestion {idx + 1}: {q['question']}")
        for i, choice in enumerate(q["choices"]):
            print(f"{i + 1}. {choice}")
        
        try:
            user_answer = int(input("Your choice (1-4): "))
            if q["choices"][user_answer - 1] == q["answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {q['answer']}")
        except (ValueError, IndexError):
            print("Invalid input! Moving to the next question.")
    
    print(f"\nQuiz finished! Your score: {score}/{len(questions)}")

def main():
    print("Welcome to the Quiz App!")
    quiz_data = get_quiz_data()

    # Category selection
    print("\nAvailable Categories:")
    for category in quiz_data.keys():
        print(f"- {category}")
    category = input("\nEnter a category: ").strip()
    while category not in quiz_data:
        category = input("Invalid category. Enter a valid category: ").strip()

    # Difficulty selection
    difficulty = input("\nSelect difficulty (easy, medium, hard): ").lower()
    while difficulty not in ["easy", "medium", "hard"]:
        difficulty = input("Invalid choice. Select difficulty (easy, medium, hard): ").lower()

    # Number of questions
    try:
        num_questions = int(input("\nEnter the number of questions: "))
    except ValueError:
        print("Invalid input! Defaulting to 5 questions.")
        num_questions = 5

    # Get the selected questions
    all_questions = quiz_data[category][difficulty]
    selected_questions = all_questions[:num_questions]

    # Start the quiz
    start_quiz(selected_questions)

if __name__ == "__main__":
    main()
