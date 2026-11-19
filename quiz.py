question = "what is the capital of cambodia ?"
correct = "Phnom penh "
answer = input(question + ": ")
if answer.strip().lower() == correct.strip().lower():
    print("Correct!")
else :
    print("wrong")
    print("The right answer is :" , correct)