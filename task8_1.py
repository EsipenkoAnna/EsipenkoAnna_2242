import re

def email_parse(email_address: str) -> dict:
  pattern = re.compile(r'(?P<username>\w+)@(?P<domain>\w+\.\w{2,3})') # Проверяем что email валидный
  result = pattern.findall(email_address)

  # Провереям, если почта не прошла проверку, выдаем ошибку
  if result == []:
    raise ValueError(f'wrong email: {email_address}')
  else:
    res2 = pattern.finditer(email_address)
    for element in res2:
      return element.groupdict()

if __name__ == '__main__':
  email_parse('someone@geekbrains.ru')
  email_parse('someone@geekbrains..ru')