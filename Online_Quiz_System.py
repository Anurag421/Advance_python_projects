'''6. Online Quiz System
Problem Statement: Develop a quiz system where users can attempt multiple-choice questions and get scores.
Steps:
Create Question and Quiz classes, with attributes like question text, options, and correct answer.
Add methods for displaying questions, checking answers, and calculating the score.
Implement a timer or limit attempts per question.'''

import time

class QuizSystem:
    def __init__(self, questions, answers, correct_option):
        self.questions = questions
        self.answers = answers
        self.correcct_option = correct_option

    
    def display_question(self):
        '''Discplay the question and options.'''
        print(self.questions)
        for i, answers in enumerate(self.answers, 1):
            print(f'{i}. {answers}')
    
    def check_answer(self, user_answer):
        '''check if the user's answer is correct.'''
        return user_answer == self.correcct_option
    
class Quiz:
    def __init__(self, time_limit = 60):
        self.question = []
        self.score = 0
        self.time_limit = time_limit
    
    def add_question(self, questions, answers, correct_option):
        '''Add a new question in the quiz.'''
        new_question = QuizSystem(questions, answers, correct_option)
        self.question.append(new_question)

    def start_quiz(self):
        '''Start the quiz! You have limit of one minute to answer this question.'''
        print('Welcome to the quiz ! You have a time lmit of ', self.time_limit, "Seconds")
        start_time = time.time()

        for question in self.question:
            question.display_question()

            ##check for time limit 
            if time.time() - start_time > self.time_limit:
                print("\nTime's up!")
                break

            try:
                user_answer = int(input("Enter the option number: "))
                if user_answer < 1 or user_answer > len(question.answers):
                    print("Invalid option. Please enter the valid option.")
                    continue

            except ValueError:
                print('Invalid input, please enter a number.')
                continue 

            if question.check_answer(user_answer):
                print("Correct!")
                self.score+=1
            else:
                print("Incorrect.")

        self.show_score()

    def show_score(self):
        '''Display the user's final score.'''
        print(f"\nYour final score is : {self.score}/{len(self.question)}")

quiz = Quiz(time_limit = 30) 
2
# Adding questions to the quiz
quiz.add_question(
    "What is the capital of France?",
    ["Berlin", "Paris", "Rome", "Madrid"],
    2
)
quiz.add_question(
    "What is the largest planet in our solar system?",
    ["Earth", "Jupiter", "Mars", "Venus"],
    2
)
quiz.add_question(
    "What is 5 multiplied by 6?",
    ["30", "20", "25", "40"],
    1
)

# Start the quiz
quiz.start_quiz()
