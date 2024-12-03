"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# your code starts here:
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
            file.write(f"Your final score is {score}/{len(self.questions)}")


paper = Exam()
readfile = open('data.txt', 'r')
paper.exam = [line.split('=') for line in [line.strip() for line in readfile.readlines()]]
paper.questions = [x[0] for x in paper.exam]
paper.answers = [x[1] for x in paper.exam]
readfile.close()
writefile = open ('data2.txt', 'w')
paper.doExam(writefile)
writefile.close()