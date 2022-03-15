from random import *

positive = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да", 
"Можешь быть уверен в этом"]
maybe = ["Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", 
"Знаки говорят - да", "Да"]
neutral = ["Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", 
"Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять"]
negative = ["Даже не думай", "Мой ответ - нет", "По моим данным - нет", 
"Перспективы не очень хорошие", "Весьма сомнительно"]
answers = [positive, maybe, neutral, negative]

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Прежде, чем задавать вопрос - представься. Как тебя зовут? ')
print(f"Привет, {name}")

while True:
    input('Задавай свой вопрос: ')
    print(choice(answers)[choice(range(len(answers)))])
    complite = input('У тебя еще остались вопросы? (да/нет): ').lower()
    if complite == "да":
        continue
    else:
        print('Возвращайся если возникнут вопросы!')
        break
