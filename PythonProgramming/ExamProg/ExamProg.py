"""
Demonstrates:
File Reading/Writing
List Comprehension
"""

class Exam:
    def __init__(self):
        self.exam = []
        self.questions = []
        self.answers = []

    def getQandA(self, file):
        self.exam = [line.split('=') for line in [line.strip() for line in readfile.readlines()]]
        self.questions = [x[0] for x in paper.exam]
        self.answers = [x[1] for x in paper.exam]

    def doExam(self, file):
        score = 0
        for counter, question in enumerate(self.questions):
            ans = input (f"{question}=")
            if ans == self.answers[counter]:
                score = score + 1
        else:
            file.write(f"Your final score is {score}/{len(self.questions)}.")

paper = Exam()
with open('questions.txt', 'r') as readfile:
    paper.getQandA(readfile)

with open('results.txt', 'w') as writefile:
    paper.doExam(writefile)