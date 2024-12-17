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