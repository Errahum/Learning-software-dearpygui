import json
import random
import textwrap

import dearpygui.dearpygui as dpg


class LearningApp:
    def __init__(self):
        self.score = 0
        self.total_questions = 0
        self.questions = self.load_data()
        self.current_question = None
        random.shuffle(self.questions)  # Randomize questions
        self.total_questions = len(self.questions)
        self.create_interface()
        self.show_question()

    def load_data(self):
        with open('questions_en.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    def create_interface(self):
        with dpg.window(label="Application d'Apprentissage", width=800, height=400):
            self.question_text = dpg.add_text(wrap=400)
            self.answer_buttons = [dpg.add_button(label="", callback=self.check_answer) for _ in range(6)]
            self.correct_button = dpg.add_button(label="Show Correct Answer", callback=self.show_correct_answer)
            self.score_label = dpg.add_text(default_value="Score: 0")
            self.result_text = dpg.add_text(color=[255, 0, 0])

    def get_random_incorrect_answers(self, correct_answer, all_answers, num=5):
        incorrect_answers = [ans for ans in all_answers if ans != correct_answer]
        random.shuffle(incorrect_answers)
        return incorrect_answers[:num]

    def shuffle_answers(self, correct_answer, all_answers):
        incorrect_answers = self.get_random_incorrect_answers(correct_answer, all_answers)
        answers = [correct_answer] + incorrect_answers
        random.shuffle(answers)
        return answers

    def show_question(self):
        if self.questions:
            self.current_question = self.questions.pop(0)
            wrapped_question = textwrap.fill(self.current_question['question'], width=90)
            dpg.set_value(self.question_text, wrapped_question)
            answers = self.shuffle_answers(self.current_question['correct_answer'],
                                           [q['correct_answer'] for q in self.questions])
            for i, button in enumerate(self.answer_buttons):
                wrapped_answer = textwrap.fill(f"{chr(65 + i)}: {answers[i]}", width=90)
                dpg.configure_item(button, label=wrapped_answer, user_data=answers[i])

    def check_answer(self, sender, app_data, user_data):
        user_answer = user_data
        correct_answer = self.current_question['correct_answer']
        if user_answer == correct_answer:
            dpg.set_value(self.result_text, "Correct!")
            self.score += 1
        else:
            dpg.set_value(self.result_text, "Incorrect!")
        dpg.set_value(self.score_label, f"Score: {self.score}/{self.total_questions}")
        dpg.configure_item(self.correct_button, callback=self.show_correct_answer)

        # Utiliser un thread pour attendre avant de montrer la prochaine question
        dpg.add_text("Please wait for the next question...", parent=dpg.last_item())
        dpg.split_frame()  # Attendre environ 1 seconde

        self.show_question()

    def show_correct_answer(self):
        dpg.set_value(self.result_text, f"The correct answer is: {self.current_question['correct_answer']}")


if __name__ == "__main__":
    dpg.create_context()
    app = LearningApp()
    dpg.create_viewport(title="Application d'Apprentissage", width=900, height=900)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
