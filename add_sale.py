import sys


sale_list = sys.argv[1]

with open('bakery.csv', 'a+', encoding='utf-8') as f:
   f.write(sale_list + '\n')



