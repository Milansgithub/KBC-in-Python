questions = [
    "What is the capital of France?",
    "What is 2 + 2?",
    "What is the largest planet in our solar system?",
    "Who wrote 'Romeo and Juliet'?"
]

answers = [
    "1",
    "2",
    "2",
    "3"
]

options = [
    ["1. Paris", "2. London", "3. Berlin", "4. Rome"],
    ["1. 3", "2. 4", "3. 5", "4. 6"],
    ["1. Mars", "2. Jupiter", "3. Saturn", "4. Earth"],
    ["1. Charles Dickens", "2. Jane Austen", "3. William Shakespeare", "4. Emily Bronte"]
]

for i in range(len(questions)):
    print(questions[i])
    for option in options[i]:
        print(option)
    
    user_answer = input("Your answer (enter the option number): ")
    if user_answer == answers[i]:
        print("Correct!")
    else:
        print("Wrong answer. The correct answer is:", options[i][int(answers[i]) - 1])
        break
else:
    print("Congratulations! You answered all questions correctly.")
