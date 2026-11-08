#Victoria Buckner
#CS 120 01
#Assignment 2 Chapter 5
#This program will give the user random numbers
#to add together and let them try to answer. After
#they have answered it will tell them if their guess 
#was correct or incorrect and give them the right answer.

import random

def main():
    num1 = random.randint(0,999)
    num2 = random.randint(0,999)
    correctAnswer = num1 + num2
    print(f"{num1}\n+{num2}")

    try:
        userAnswer = int(input("What is your answer?"))
        if userAnswer == correctAnswer:
            print("Congratulations! Your answer is correct.")
        else:
            print(f"Incorrect. The correct answer is {correctAnswer}.")
    except ValueError:
        print("Please enter a valid number.")
main()
