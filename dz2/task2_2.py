def convert(list_in: list) -> str:
 str_out=[]
 for i in list_in:
     temp_list =[]
     if i.isdigit():
         temp_list.append(i.zfill(2))
         str_out.append(''.join(temp_list))
     elif i[0] in '+-':
         temp_list.append(i.zfill(3))
         str_out.append(''.join(temp_list))

     else:
         temp_list.append(i)
         str_out.append(''.join(temp_list))

 return str_out



my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert(my_list)
print(*result)
