"""
This is a code-along tutorial and is not my own work, but does contain very minimal modification.
All credit goes to Bro Code.

"""

questions = ("How many elements are in the periodic table?: ",
            "Which animal lays the largest eggs?: ",
            "How many bones are in the human body?: ",
            "What is the most abundant gas in Earth's atmosphere?: ",
            "Which plant in the solar system is the hottest?: ", 
            "How many days are in a leap year?: ", 
            "Where was the first example of paper money used?: ",
            "Which of the following languages has the longest alphabet?: "
            )

options = (("A. 116", "B. 117", "C. 118", "D. 119"), 
             ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"), 
             ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"), 
             ("A. 206", "B. 207", "C. 208", "D. 209"), 
             ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"), 
             ("A. 369", "B. 365", "C. 366", "D. 367"),
             ("A. USA", "B. Turkey", "C. Greece", "D. China"),
             ("A. English", "B. Russian", "C. Arabic", "D. Greek")
             )

answers = ("C", "D", "A", "A", "B", "C" ,"D", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
  print("-" * 30)
  print(question)
  for option in options[question_num]:
    print(option)

  guess = input("Enter (A, B, C, D): ").upper().strip()
  guesses.append(guess)

  if guess == answers[question_num]:
    score += 1
    print("Correct!")
  else:
    print("Incorrect.")
    print(f"{answers[question_num]} is the correct answer.")

  question_num += 1

print("-" * 30)
print("          Results          ")
print("-" * 30)

print("Answers: ", end="")
for answer in answers:
  print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
  print(guess, end=" ")
print()

totalscore = int(score / len(questions) * 100)
print(f"Your score is: {totalscore}% ({score} / {len(questions)})")