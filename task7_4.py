import os

folder = 'my_project'
work_directory = os.path.join(os.getcwd(), folder)
walk_gen = os.walk(work_directory)

list_1 = []
for folder, dir, files in walk_gen:
    for name in files:
        list_1.append(os.path.getsize(os.path.join(folder, name)))

list_100 = [el for el in list_1 if el < 100]
list_1000 = [el for el in list_1 if el > 100 and el < 1000]
list_10000 = [el for el in list_1 if el > 1000 and el < 10000]
list_100000 = [el for el in list_1 if el > 10000 and el < 100000]

my_dict = {100: len(list_100), 1000: len(list_1000), 10000: len(list_10000), 100000: len(list_100000)}

for keys, items in my_dict.items():  # использую цикл для вывода информации в столбик "ключ:значение"
    print(f'{keys}:{items}')