import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
#формируем список состящий из фраз. Каждая фраза содержит по три слова, которые случайным образом берутся из списоков nouns, adverbs и adjectives
    list_out = []

    for i in range(count):
     list_out.extend([random.choice(nouns)+" "+random.choice(adverbs)+" "+random.choice(adjectives)])
    return list_out


print(get_jokes(6))

def get_jokes_adv(count: int, Double: bool) -> list:
#Если выставлен флаг Double как False, то после того как слово было использовано, оно будет удалено из списка
  list_out_1 = []
  for a in range(count):
     if Double==False:
      nouns_w = random.choice(nouns)
      adverbs_w = random.choice(adverbs)
      adjectives_w = random.choice(adjectives)
      list_out_1.extend([nouns_w+" "+adverbs_w+" "+adjectives_w])
      nouns.remove(nouns_w)
      adverbs.remove(adverbs_w)
      adjectives.remove(adjectives_w)

     else:
      list_out_1.extend([random.choice(nouns) + " " + random.choice(adverbs) + " " + random.choice(adjectives)])
  return list_out_1

print(get_jokes_adv(2,False))
print(nouns, adverbs, adjectives) #проверяем, что элементы удалены