#Victoria Buckner
#CS 120 01
#Program Assignment 02, Chapter 07
#This program will have the user input the test
#answers, check if they are correct, then determine
#if the student passed the test. Finally, it will
#display the result of the test, how many questions
#the student got correct, how many questions the
#student got incorrect, and what questions were
#answered incorrectly.

def main():
    correctAnswers = ["B", "D", "A", "A", "C", "A", "B",
                      "A", "C", "D", "B", "C", "D", "A",
                      "D", "C", "C", "B", "D", "A"]
    studentAnswers = []
    incorrectQuestions = []

    print("Enter the answers for the 20 questions: ")
    for i in range(20):
        answer = input(f"Question {i + 1}: ").strip().upper()
        while answer not in ["A", "B", "C", "D"]:
            print("Invalid input. Please enter A, B, C, or D.")
            answer = input(f"Question {i + 1}: ").strip().upper()
        studentAnswers.append(answer)

    correctCount = 0
    for i in range(20):
        if studentAnswers[i] == correctAnswers[i]:
            correctCount += 1
        else:
            incorrectQuestions.append(i + 1)

    if correctCount >= 15:
        print("Result: Passed")
    else:
        print("Result: Failed")

    print(f"Total correct answers: {correctCount}")
    print(f"Total incorrect answers: {20 - correctCount}")
    if incorrectQuestions:
        print("Incorrect Questions: ", incorrectQuestions)
    else:
        print("There were no incorrect questions!")
        
if __name__ == "__main__":
    main()
