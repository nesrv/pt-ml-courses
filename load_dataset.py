import pandas as pd

# Загрузка CSV файла в DataFrame
file_path = 'UUI/fake_orders.csv'
df = pd.read_csv(file_path)

# Вывод информации о датасете
print("Размер датасета:", df.shape)
print("\nПервые 5 строк:")
print(df.head())

print("\nИнформация о датасете:")
print(df.info())

print("\nСтатистика по числовым столбцам:")
print(df.describe())