answers = {
    "как дела": "Отлично, а у тебя?!", 
    "что делаешь": "Программирую.",
    "привет": "Привет!",
    "пока":"Еще увидимся!"}
def hello_user():
    while True:
        answer = input("Как дела? ")
        if answer.lower() == 'хорошо':
            break
def get_answer(question, answers):
    return answers.get(question)

def ask_user(answers):
    while True:
        user_input = input("Скажи что нибудь: ").lower()
        answer = get_answer(user_input, answers)
        print(answer)

        if user_input == 'пока':
            break
# hello_user()
ask_user()