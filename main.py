from math import floor
from  openpyxl import load_workbook, utils
from random import choice
from time import time


name_file = '3.23.xlsx'
 # Обработчик ошибок
try: workbook = load_workbook(name_file)
except FileNotFoundError: print(f"Файл {name_file} не найден."); input(); exit()
except utils.exceptions.InvalidFileException: print("Файл некорректен или поврежден."); input(); exit()

sheet = workbook['Sheet1'] # Выбираем нужный лист
words_counter = sheet.max_row # Кол-во строк в документе
words = {} # Хранение слов

remove_xa0 = lambda s: s.replace('\xa0', '') # удаление пробелом в кодировке ASCII
for i in range(1, words_counter + 1):
    eng_word = remove_xa0(sheet.cell(row=i, column=1).value).lower() # чтение первого столбца
    rus_word = remove_xa0(sheet.cell(row=i, column=2).value).lower() # чтение второго столбца
    words[eng_word] = rus_word # запись обеих значений в словарь

# print(words) # Удаляйте дальнейший код если не хотите использовать консоль а хотите что-то своё

def check_value(answer, random_value): # Проверка на правильность ответа
    if answer in random_value.lower() and len(answer) != 0: return True
    else: return False


def Check_Knowleague_Hunan(words): # Консольный ввод/вывод
    start_time = time() # старт секундомера
    last_value, random_value, fail_counter = '','',0
    random_words = words # клон словаря со значениями в котором после успешного ответа удаляется слово
    while len(random_words) > 0: # Пока в клоне словаря со значениями есть значения(по мере успешных ответов их кол-во уменьшается)
        last_value = random_value # запоминание прошлого правильного ответа для подсказки
        random_key = choice(list(words.keys())) # берёт случайный ключ
        random_value = words[random_key] # по случайному ключу берём значение
        answer = input(f'{random_key} - ') # получаем ответ пользователя
        if check_value(answer, random_value): # если ответ верный удаляем данное слово
            print('Верно!')
            del random_words[random_key]
        elif answer == '1':
            print(f'Ответ: {random_value}')
        elif answer == '2':
            print(f'Ответ на прошлый вопрос: {last_value}')
        else:
            print('Не верно((')
            fail_counter+=1
        print(f'Слов осталось: {len(random_words)}') # счётчик остатка слов
    elapsed_time = time() - start_time # подсчёт затраченного времени
    print(f'Поздавляю! Вы успешно ответили на все слова!! На это вам понадобилось {floor(elapsed_time)} секунд')
    print(f'Число неудачных ответов: {fail_counter}')

print("Введите 1 для текущего ответа и 2 для прошлого ответа")
# print("\033[1;32m\033[40mВведите 1 для текущего ответа и 2 для прошлого ответа\033[0m") # вывод красивого сообщения которое работает только в IDE
Check_Knowleague_Hunan(words) # работа консоли