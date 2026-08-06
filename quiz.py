questions = ("How many people in aisamtech? :", 
            "how many ikan goreng in the pool? :", 
            "what is cat?: ",
            "what is love?: ",
            "is it okay to fall in love with the opposite version of you?: ")
options = (("A. 90", "B. 20", "C. 5", "D. 100"),
          ("A. 3", "B. 7", "C. 0", "D. 999"),
          ("A. animal", "B. food", "C. car", "D. plant"),
          ("A. baby dont hurt me", "B. chemical", "C. money", "D. idk"),
          ("A. yes", "B. no", "C. maybe", "D. absolutely"))

answers = ("C", "D", "A", "B", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------")
    print(question)
    for option in options [question_num]:
        print(option)

    guess = input("Pilihan ganda ya bang: ").upper()
    guesses.append(guess)

    if guess == answers[question_num]: 
        score += 1
        print("CORRECT")
    else:
        print("incorrect")

    question_num = question_num + 1


print("__________")
print("Your result is: ")
print("__________")

print("answers:", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guess:", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"your score is {score}")