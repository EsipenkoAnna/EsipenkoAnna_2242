def num_translate(value: str) -> str:
    if value.istitle() == True:
     nums_in_russ_cap_letter = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Give': 'Пять','Six': 'Шесть', 'Seven': 'Семь', 'Eight': 'Восемь', 'Nine': 'Девять', 'Ten': 'Десять'}
     str_out = nums_in_russ_cap_letter.get(value)
    else:
     nums_in_russ_small_letter = {'one': 'один', 'two':'два', 'three': 'три', 'four': 'четыре', 'five':'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine':'девять', 'ten':'десять' }
     str_out = nums_in_russ_small_letter.get(value)
    return str_out

print(num_translate("one"))
print(num_translate("Eight"))

