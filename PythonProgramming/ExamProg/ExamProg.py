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

    def doExam(self, file):
        score = 0
        for counter, question in enumerate(self.questions):
            ans = input (f"{question}=")
            if ans == self.answers[counter]:
                score = score + 1
        else:
            file.write(f"Your final score is {score}/{len(self.questions)}.")2


paper = Exam()
readfile = open('questions.txt', 'r')
paper.exam = [line.split('=') for line in [line.strip() for line in readfile.readlines()]]
paper.questions = [x[0] for x in paper.exam]
paper.answers = [x[1] for x in paper.exam]
readfile.close()
writefile = open ('results.txt', 'w')
paper.doExam(writefile)
writefile.close()