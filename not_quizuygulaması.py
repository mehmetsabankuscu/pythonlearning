 #quesstion
class Question:
    def __init__(self,text,choices,answer):
         self.text= text
         self.choices=choices
         self.answer=answer


    def checkAnswer(self, answer):
        return self.answer == answer

# q1 = Question("en iyi programlama dili nedir?", ["C#","python","javascript","java"],"python")
# q2 = Question("en popüler programlama dili nedir?", ["python","C#","javascript","java"],"python")
# q3 = Question("en kazandıran programlama dili nedir?", ["C#","javascript","python","java"],"python")
# liste = [q1,q2,q3]
  
# print(q1.checkAnswer("python"))
# print(q2.checkAnswer("C#"))

class Quiz:
    def __init__(self,question):
        self.question = question
        self.score = 0
        self.questionIndex = 0

q1 = Question("en iyi programlama dili nedir?", ["C#","python","javascript","java"],"python")
q2 = Question("en popüler programlama dili nedir?", ["python","C#","javascript","java"],"python")
q3 = Question("en kazandıran programlama dili nedir?", ["C#","javascript","python","java"],"python")
question = [q1,q2,q3]

quiz = Quiz(question)
