from random import uniform


def transfer_list_in_str(list_in: list) -> str:
   temp_list=[]
   for i in list_in:
     rub,k=str(f"{i:.2f}").split(".")
     k=k.zfill(2)
     temp_list.append(str(rub)+' руб '+str(k)+' коп ')
   str_out=''.join(temp_list)
   return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)

def sort_prices(list_in: list) -> list:

 list_in.sort()
 return list_in


list_id =id (my_list)
print(list_id, '-первый раз выводим id списка')

result_2 = sort_prices(my_list)

list_id1 =id (my_list)
print(list_id1, '-второй раз выводим id списка')
print(result_2)

def sort_price_adv(list_in: list) -> list:

    list_out = sorted(list_in, reverse=True)
    return list_out


result_3 = sort_price_adv(my_list)
print(result_3)



def check_five_max_elements(list_in: list) -> list:
    list_in.sort()
    list_out = list_in[ :5 ]
    return list_out


result_4 = check_five_max_elements(my_list)
print(result_4)