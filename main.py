# объявление функции
def is_pangram(text):
    return len(set(text.lower())) == 27
    

# считываем данные
text = 'The jay pig fox zebra and my wolves quack'

# вызываем функцию
print(is_pangram(text))