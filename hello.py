def hello_user():
    while True:
        answer = input("Как дела? ")
        if answer.lower() == 'хорошо':
            break

def ask_user():
    answers = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую"}
    question = input("Пользователь: ")
    if question in answers.keys():
        print(f"Программа: {answers[question]}")
# hello_user()
ask_user()