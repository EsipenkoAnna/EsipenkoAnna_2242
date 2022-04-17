from gettext import find
import requests


def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""

    inquiry = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    inquiry_text = inquiry.text
    start_index = inquiry_text.find(code)
    if start_index != -1:
        inquiry_text = inquiry_text[start_index:]
        end_index = inquiry_text.find('</Value>')
        inquiry_text = inquiry_text[:end_index]
        inquiry_text = inquiry_text.replace(',','.').split('>')
        result_value = inquiry_text[-1]
    else:
        result_value = "None"

    return result_value


print(currency_rates("USD"))
print(currency_rates("noname"))
print(currency_rates("USD"))
