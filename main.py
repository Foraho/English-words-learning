""""
Правки:
- сделать так что бы в переводе могло быть несколько ошибок
- сделать так что бы допускалось несколько грамматических ошибок
- сделать так что бы можно узнать правильный ответ на прошлый вопрос
- в конце выводить кол-во затраченного времени, ошибок и правильный ответов
"""



import openpyxl
import random

name_file = '3.23.xlsx'
workbook = openpyxl.load_workbook(name_file) # Открываем файл Excel
sheet = workbook['Sheet1'] # Выбираем нужный лист
words_counter = sheet.max_row # Кол-во строк в документе
words = {}

remove_xa0 = lambda s: s.replace('\xa0', '') # удаление пробелом в кодировке ASCII
for i in range(1, words_counter + 1):
    eng_word = remove_xa0(sheet.cell(row=i, column=1).value).lower() # чтение первого столбца
    rus_word = remove_xa0(sheet.cell(row=i, column=2).value).lower() # чтение второго столбца
    words[eng_word] = rus_word # запись обеих значений в словарь

# print(words)

def Check_Knowleague_Hunan(words):
    random_words = words
    while len(random_words) > 0:
        random_key = random.choice(list(words.keys()))
        random_value = words[random_key]
        answer = input(random_key + '- ')
        if answer == random_value:
            print('Верно!')
            del random_words[random_key]
        elif answer == '123':
            print('Ответ: ', random_value)
        else:
            print('Не верно((')
        print(len(random_words))

Check_Knowleague_Hunan(words)