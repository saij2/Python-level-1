print("Sashi LLM:")

######### Questions ########
question1 = "What is Sashi's favorite country?"
question2 = "What is Sashi's favorite subject?"
question3 = "What is Sashi's favorite color?"
question4 = "What is Sashi's favorite hobby?"
question5 = "What is Sashi's favorite dessert?"
question6 = "What is Sashi's dream vacation country?"
question7 = "What is Sashi's favorite book genre?"
question8 = "What is Sashi's favorite drink?"
question9 = "What is Sashi's favorite holiday?"
question10 = "What is Sashi's favorite music genre?"

######### Answers ########
answer1 = "Switzerland"
answer2 = "Literature"
answer3 = "Blue"
answer4 = "Crocheting"
answer5 = "Cake"
answer6 = "Switzerland"
answer7 = "Literature"
answer8 = "Coffee"
answer9 = "Halloween"
answer10 = "R&B"

while True:
    prompt = input("Prompt: ")

    if prompt.lower().replace(" ", "") in question1.lower().replace(" ", "").replace("'", "").replace("?", ""):
        print(answer1)
    elif prompt.lower().replace(" ", "") in question2.lower().replace(" ", "").replace("'", "").replace("?", "").replace("'", "").replace("?", ""):
        print(answer2)
    elif prompt.lower().replace(" ", "") in question3.lower().replace(" ", "").replace("'", "").replace("?", "").replace("'", "").replace("?", ""):
        print(answer3)
    elif prompt.lower().replace(" ", "") in question4.lower().replace(" ", "").replace("'", "").replace("?", "").replace("'", "").replace("?", ""):
        print(answer4)
    elif prompt.lower().replace(" ", "") in question5.lower().replace(" ", "").replace("'", "").replace("?", "").replace("'", "").replace("?", ""):
        print(answer5)
    elif prompt.lower().replace(" ", "") in question6.lower().replace(" ", "").replace("'", "").replace("?", "").replace("'", "").replace("?", ""):
        print(answer6)
    elif prompt.lower().replace(" ", "") in question7.lower().replace(" ", "").replace("'", "").replace("?", "").replace("'", "").replace("?", ""):
        print(answer7)
    elif prompt.lower().replace(" ", "") in question8.lower().replace(" ", "").replace("'", "").replace("?", ""):
        print(answer8)
    elif prompt.lower().replace(" ", "") in question9.lower().replace(" ", "").replace("'", "").replace("?", ""):
        print(answer9)
    elif prompt.lower().replace(" ", "") in question10.lower().replace(" ", "").replace("'", "").replace("?", ""):
        print(answer10)
    else:
        print("Sorry I couldn't Answer")
