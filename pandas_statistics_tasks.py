import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка CSV файла в DataFrame
file_path = 'UUI/fake_orders.csv'
df = pd.read_csv(file_path)

# Задание 1: Базовая статистика
print("Задание 1: Базовая статистика")
print("Среднее значение по числовым столбцам:")
print(df.mean(numeric_only=True))
print("\nМедиана по числовым столбцам:")
print(df.median(numeric_only=True))
print("\nСтандартное отклонение:")
print(df.std(numeric_only=True))

# Задание 2: Корреляционный анализ
print("\nЗадание 2: Корреляционный анализ")
numeric_df = df.select_dtypes(include=['number'])
correlation = numeric_df.corr()
print("Корреляционная матрица:")
print(correlation)

# Задание 3: Группировка и агрегация
print("\nЗадание 3: Группировка и агрегация")
# Предполагаем, что в датасете есть категориальные столбцы
# Замените 'category_column' на реальное имя столбца из вашего датасета
try:
    # Пробуем найти категориальные столбцы
    categorical_columns = df.select_dtypes(include=['object']).columns
    if len(categorical_columns) > 0:
        category_column = categorical_columns[0]
        print(f"Статистика по группам в столбце '{category_column}':")
        print(df.groupby(category_column).agg({
            # Замените эти столбцы на числовые столбцы из вашего датасета
            df.select_dtypes(include=['number']).columns[0]: ['mean', 'median', 'std', 'count']
        }))
    else:
        print("В датасете не найдены категориальные столбцы для группировки")
except Exception as e:
    print(f"Ошибка при выполнении группировки: {e}")

# Задание 4: Квантили и процентили
print("\nЗадание 4: Квантили и процентили")
numeric_columns = df.select_dtypes(include=['number']).columns
if len(numeric_columns) > 0:
    num_column = numeric_columns[0]
    print(f"Квантили для столбца '{num_column}':")
    print(df[num_column].quantile([0.1, 0.25, 0.5, 0.75, 0.9]))

# Задание 5: Выбросы (Outliers)
print("\nЗадание 5: Выбросы (Outliers)")
if len(numeric_columns) > 0:
    num_column = numeric_columns[0]
    Q1 = df[num_column].quantile(0.25)
    Q3 = df[num_column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[num_column] < lower_bound) | (df[num_column] > upper_bound)]
    print(f"Количество выбросов в столбце '{num_column}': {len(outliers)}")
    if len(outliers) > 0:
        print("Примеры выбросов:")
        print(outliers.head())

# Задание 6: Проверка на нормальность распределения
print("\nЗадание 6: Проверка на нормальность распределения")
if len(numeric_columns) > 0:
    num_column = numeric_columns[0]
    print(f"Статистика для столбца '{num_column}':")
    print(f"Асимметрия (Skewness): {df[num_column].skew()}")
    print(f"Эксцесс (Kurtosis): {df[num_column].kurt()}")
    
# Задание 7: Заполнение пропущенных значений
print("\nЗадание 7: Заполнение пропущенных значений")
print(f"Количество пропущенных значений по столбцам:")
print(df.isna().sum())
print("\nЗаполнение пропущенных значений средним:")
df_filled = df.fillna(df.mean(numeric_only=True))
print(f"Количество пропущенных значений после заполнения:")
print(df_filled.isna().sum())