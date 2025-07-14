questions = (
    "How many elements are in the periodic table?: ",
    "Which animal lays the largest eggs?: ",
    "What is the most abundant gas in Earth's atmosphere?: ",
    "How many bones are in the human body?: ",
    "Which planet in the solar system is the hottest?: "
)

options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
    ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. Mercury", "B. Venus", "C. Mars", "D. Jupiter")
)

answers = ("C", "D", "A", "A", "B")

guesses = []
score = 0

for i in range(len(questions)):
    print("-------------------------")
    print(questions[i])
    for option in options[i]:
        print(option)
    guess = input("Enter (A, B, C, or D): ").upper()
    guesses.append(guess)
    if guess == answers[i]:
        print("CORRECT!")
        score += 1
    else:
        print("WRONG!")
        print(f"Correct answer: {answers[i]}")

print("-------------------------")
print("         RESULTS         ")
print("-------------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

print(f"Your score: {score}/{len(questions)}")