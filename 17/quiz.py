
class Quiz:
    def __init__(self,data) -> None:
        self.data = data
        self.points = 0
        self.quests = 0
    def quiz(self):
        for question in self.data:
            answer = str(input(f"{question.question}. (True/False): "))
            if answer == question.answer:
                print("You're right!!!")
                self.points += 1
                self.quests += 1
                print(f"Your current score is: {self.points}/{self.quests}\n")
            else:
                print ("That's wrong")
                self.quests += 1
                print(f"Your current score is: {self.points}/{self.quests}\n")
        print("You've completed the quiz")
        print(f"Your final score was: {self.points}/{self.quests}")