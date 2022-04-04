
def thesaurus(*args) -> dict:
    dict_out = {}  # результирующий словарь значени

    for i in args:
     key=i[0]
     if key not in dict_out:
         dict_out[key]=[]
         dict_out[key].append(i)
     else:
        dict_out[key].append(i)
    #сортировка
    for key in sorted(dict_out):
        print (key)
    return dict_out


print(thesaurus("Иван", "Мария", "Петр", "Илья"))