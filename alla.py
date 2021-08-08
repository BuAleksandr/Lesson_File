from pprint import pprint
import os


file_4 = os.path.join(os.getcwd(), '4.txt')

result = []
docs = ['1.txt', '2.txt', '3.txt']

for i in docs:
    dict = {}
    with open(i, 'r', encoding="utf-8") as file:
        dict['Имя файла'] = i
        lines = file.readlines()
        dict['Количество строк'] = len(lines)
        dict['Содержимое файла'] = lines
        result.append(dict)

    result.sort(key=lambda x: x['Количество строк'])
    pprint(result)

with open('4.txt', 'w', encoding="utf-8") as f:
    for line in result:
        f.write(f"{line['Имя файла']}\n")
        f.write(f"{str(line['Количество строк'])}\n")
        for i in line['Содержимое файла']:
            f.write(i)
            f.write(f"\n")

    print('Текст записан в файл 4.txt')