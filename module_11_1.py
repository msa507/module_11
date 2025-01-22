# позволяет работать с HTTP-запросами
import requests

res = requests.get('https://urban-university.ru')# Создаём переменную, сохраним код состояния запрашиваемой страницы
print(res)# Выводим код состояния
# print(res.content)# Информация в виде байтов
# print(res.text)# Информация в виде строк
# print(res.headers)# информация о сервере, датe, кодировкe и так далее

query = {'q': 'Методика', 'order': 'Python-разработчик', 'addres' : 'адрес'}
req = requests.get('https://urban-university.ru', params=query)
print(req.url)

# для работы с данными (аналитика, статистика, data sci)
import pandas as pd

city = {'Город': ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург'],
        'Год основания': [1147, 1703, 1893, 1723],
        'Население': [11.9, 4.9, 1.5, 1.4]}
df = pd.DataFrame(city) #превращаем в словарь
print(df)
df1 = pd.read_csv('data.csv')
print(df1.head())# вывод 5 (по умолчанию) первых строк
df2 = df.dtypes#типы данных
df3 = df.describe()#оценка данных(отклонения, макс, мин и пр.), только для чисел
df4 = df.sort_values('Год основания', ascending=False)
print(f'Типы данных\n{df2}\n Оценка данных\n{df3}\n Сортировка данных\n{df4}')

#поддержка больших многомерных массивов и матриц,
#вместе с большой библиотекой высокоуровневых математических функций для операций с этими массивами

import numpy as np

a = np.array([1, 2, 3])#создание массивов
print(a)
print(type(a))
b = np.zeros((3, 5))#массив с нулевыми значениями
print(b)

def f1(i, j):
    return 3 * i + j

print(np.fromfunction(f1, (3, 4)))#применяет ф-цию ко всем индексам
print(np.fromfunction(f1, (3, 3)))