
import pandas as pd

# s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
# print(s)



# data = {'Name': ['Анна', 'Борис'], 'Age': [25, 30]}
# df = pd.DataFrame(data)
# print(df)

data = {
    'Name': ['Анна', 'Борис', 'Ирина'],
    'Age': [25, 30, 28],
    'City': ['Москва', 'СПб', 'Казань']
}

df = pd.DataFrame(data)


print(df)
# print(df.head())         # первые строки
print(df.describe())     # статистика по Age
# print(df['Age'].mean())  # средний возраст

from numpy import random as np

arr = np.array([1, 2, 3, 4])
np.random.shuffle(arr)
print(arr)