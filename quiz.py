class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions = [
    Question("What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n", "a"),
    Question("What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n", "c"),
    Question("What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n", "b"),
    Question("What color are oranges?\n(a) Orange\n(b) Red\n(c) Blue\n\n", "a"),
    Question("What color are grapes?\n(a) Orange\n(b) Red\n(c) Purple\n\n", "c"),
    Question("What color are lemons?\n(a) Yellow\n(b) Red\n(c) Blue\n\n", "a"),
    Question("What color are limes?\n(a) Orange\n(b) Green\n(c) Blue\n\n", "b"),
    Question("What color are peaches?\n(a) Orange\n(b) Red\n(c) Blue\n\n", "a"),
    Question("What color are plums?\n(a) Orange\n(b) Red\n(c) Purple\n\n", "c"),
    Question("What color are cherries?\n(a) Orange\n(b) Red\n(c) Blue\n\n", "b"),
    Question("What color are blueberries?\n(a) Orange\n(b) Red\n(c) Blue\n\n", "c"),
    Question("What color are raspberries?\n(a) Orange\n(b) Red\n(c) Blue\n\n", "b"),
    Question("What color are blackberries?\n(a) Orange\n(b) Red\n(c) Purple\n\n", "c"),
    Question("What color are watermelons?\n(a) Orange\n(b) Red\n(c) Green\n\n", "c")
]

def run_quiz(questions):
    score = 0  # initialization of the variable score
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1  # incrementing the score if the answer is correct
    print("You got", score, "out of", len(questions), "correct")

run_quiz(questions)