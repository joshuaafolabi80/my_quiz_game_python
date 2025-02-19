print("Welcome to my game quiz")
response = input("Are you ready to answer questions and win prizes? yes/no ").lower()
if response != "yes":
    print("Maybe some other time! Goodbye!")
    quit()
print("Answer the following questions!")

questions = [("What is the full meaning of CPU?",["A) Central processing unit","B) Centre processing unit","C) Corporate processing unit","D) Command processing unit"],"A"),("Which planet is reffered to as the red planet?",["A) Jupiter","B) Mercury","C) Mars","D) Earth"],"C"),("Who betrayed Jesus?",["A) John","B) Matthew","C) Philip","D) Peter"],"D"),("Who was the earthly father of Jesus?",["A) Barnabas","B) David","C) Joseph","D) Melchizedek"],"C")]

score = 0
total_questions = len(questions)
marks_per_questions = 25

for question, options, correct_answer in questions:
    print("\n" + question)
    for option in options:
        print(option)
    user_answer = input("Select the correct option: ").upper()

    if user_answer == correct_answer:
        print("Correct!")
        score += marks_per_questions
    else:
        correct_index = ord(correct_answer) - ord("A")
        print(f"Incorrect! The correct option is: {correct_answer} - {options[correct_index][3:]}")

print("\n Quiz completed")
print(f"Your total score is: {score}/{total_questions*marks_per_questions}")

if score == total_questions*marks_per_questions:
    print("Perfect! You are a genius!")
elif score >= (0.7*total_questions*marks_per_questions):
    print("Welldone! You performed excellently!")
elif score >= (0.5*total_questions*marks_per_questions):
    print("Good effort! Keep practicing!")
else:
    print("Better result next time! Don't give up!")