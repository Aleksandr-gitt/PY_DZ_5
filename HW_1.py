# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# В тексте используется разделитель пробел.
#
# in  Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
# in  Number of words: -1
# out The data is incorrect
import random

words = int(input('Введите кол-во рандомных слов: '))
while words < 1:
    print("The data is incorrect!!!")
    words = int(input('Введите кол-во рандомных слов: '))
else:
    word_l = ['а', 'б', 'в']
    # control_word = 'абв'
    control_word = word_l[0] + word_l[1] + word_l[2]
    text = ''
    for i in range(words):
        text += ''.join(random.sample(word_l, 3)) + ' '
    print(text)
    qwerty = text.split()
    # print(qwerty)
    while control_word in qwerty:
        qwerty.remove(control_word)
    print(' '.join(qwerty))


