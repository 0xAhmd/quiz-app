#Quiz App

This is a simple Quiz App written in Python that allows users to select a category, difficulty level, and number of questions. The app features hardcoded quiz data and provides immediate feedback on the answers.

Features

Multiple categories to choose from (e.g., Science, History).

Three difficulty levels: Easy, Medium, Hard.

Flexible number of questions based on user preference.

Immediate feedback on whether the answer is correct or not.

Final score displayed at the end of the quiz.

How It Works

Start the App: Run the Python script.

Select a Category: Choose from the available categories (e.g., Science, History).

Choose Difficulty: Select a difficulty level: Easy, Medium, or Hard.

Specify Number of Questions: Enter the number of questions you'd like to attempt.

Answer Questions: The app will display questions one by one. You select your answer by entering the number corresponding to your choice.

View Results: At the end of the quiz, your score will be displayed.

Requirements

Python 3.x

Running the App
```

Clone or download this repository.
```
Open a terminal or command prompt.

Navigate to the directory containing the script.

Run the script using the following command:

python quiz_app.py

Example Interaction

Starting the App:
```
Welcome to the Quiz App!

Available Categories:
- Science
- History

Enter a category: Science

Select difficulty (easy, medium, hard): easy

Enter the number of questions: 2
```
```
Sample Question:

Question 1: What planet is known as the Red Planet?
1. Earth
2. Mars
3. Jupiter
4. Saturn
Your choice (1-4): 2
Correct!

Question 2: What is H2O commonly known as?
1. Hydrogen
2. Water
3. Oxygen
4. Helium
Your choice (1-4): 2
Correct!

Quiz finished! Your score: 2/2
```
Customizing the App

You can customize the quiz by modifying the get_quiz_data() function:

Add new categories.

Add more questions to existing categories.

Update or change difficulty levels.

Future Enhancements

Dynamic Question Generation: Integrate OpenAI API to generate questions dynamically.

Persistent Storage: Save scores and user progress to a database.

GUI Support: Create a graphical user interface using libraries like Tkinter or PyQt.

