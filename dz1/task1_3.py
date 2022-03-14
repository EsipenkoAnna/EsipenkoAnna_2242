for numb in range (1, 101):

 if numb%10 == 1 and numb!=11:
    choise = f'{numb} Процент'
 elif (5>numb>=2 or 5>numb%10>=2) and numb not in range(12,15):
    choise = f'{numb} Процента'
 else:
    choise = f'{numb} Процентов'
 print(choise)