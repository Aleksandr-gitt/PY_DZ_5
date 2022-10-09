# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные
# хранятся в отдельных текстовых файлах.
# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'
# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ
import os

def proverka (name_file):
    while os.path.exists(name_file) == False:
        print('Bad name!!!')
        name_file = input('Enter the name of the file with the text: ')
    return name_file


def record(file, file2):
    with open(file) as text:
        lines = sum(1 for line in text)
        text.seek(0)
        for lin in range(lines):
            stroka = str(text.readline().strip())
            i = 0
            ls = []
            count = 1
            while i < len(stroka) - 1:
                if stroka[i] == stroka[i + 1]:
                    count += 1
                else:
                    ls.append(str(count) + stroka[i])
                    count = 1
                i += 1
            ls.append(str(count) + stroka[-1])
            with open(file2, 'a') as code:
                code.seek(0)
                code.write(f"{''.join(ls)}\n")
        return 'OK'


def decode(file3):
    with open(file3) as decode:
        lines = sum(1 for line in decode)
        decode.seek(0)
        for lin in range(lines):
            data = decode.readline().strip()
            new_str = []
            for i in data:
                new_str.append(i)
            m, n, dec_str = 0, 1, ''
            while m < len(new_str)-1:
                dec_str += str(new_str[n] * int(new_str[m]))
                m += 2
                n += 2
            print(dec_str)


file = input('Enter the name of the file with the text: ')
file = proverka(file)
file2 = input('Enter the file name to record: ')
file2 = proverka(file2)
print(record(file,file2))
file3 = input('Enter the name of the file to decode: ')
file3 = proverka(file3)
decode(file3)
