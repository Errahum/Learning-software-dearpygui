# Learning Application Documentation

## Overview
This project is a learning application developed using DearPyGui, a simple GUI framework for Python. The application presents questions to users and evaluates their answers, providing feedback and keeping score.

![learning_application]([https://github.com/Sahurows/Learning-Software/demo.gif](https://github.com/Sahurows/Learning-software/blob/main/demo.gif))

### questions.json
A JSON file containing a list of questions and their correct answers.

Example:
```json
[
    {
        "question": "What is a Python interpreter?",
        "correct_answer": "The program that executes Python code line by line."
    },
    {
        "question": "What does indentation determine in Python?",
        "correct_answer": "How Python determines the structure of its code, using spaces or tabs to delineate code blocks."
    }
]

```

### How to Run
Ensure you have the required dependencies:
pip install dearpygui

Place the questions.json file in the same directory as learning_app.py.
Run the application:
python learning_app.py

The application window will display questions, and users can select answers. The score is updated based on correct or incorrect responses.
