## 🛒 Анализ данных из Fake Store API с использованием pandas

### 🔧 Этап 1: Получение данных

```python
import requests
import pandas as pd

# Получаем данные с API
url = "https://fakestoreapi.com/products"
response = requests.get(url)
products = response.json()

# Преобразуем в DataFrame
df = pd.DataFrame(products)
print(df.head())
```

---

### 📊 Этап 2: Первичный анализ данных

#### Сколько всего товаров?

```python
print(f"Всего товаров: {len(df)}")
```

#### Сколько уникальных категорий?

```python
print(f"Уникальные категории: {df['category'].nunique()}")
print(df['category'].unique())
```

#### Самый дорогой товар

```python
most_expensive = df.loc[df['price'].idxmax()]
print("Самый дорогой товар:")
print(most_expensive[['title', 'price']])
```

#### Самый дешёвый товар

```python
cheapest = df.loc[df['price'].idxmin()]
print("Самый дешёвый товар:")
print(cheapest[['title', 'price']])
```

#### Средняя цена по категориям

```python
avg_price_per_category = df.groupby("category")["price"].mean()
print("Средняя цена по категориям:")
print(avg_price_per_category)
```

#### 📈 Визуализация количества товаров по категориям

```python
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 5))
sns.countplot(data=df, y='category', order=df['category'].value_counts().index)
plt.title("Количество товаров по категориям")
plt.xlabel("Количество")
plt.ylabel("Категория")
plt.tight_layout()
plt.show()
```

---

### 🧠 Этап 3: Дополнительные задачи

#### Средний рейтинг по категориям

```python
# rating — это словарь внутри каждой строки
df['rating_rate'] = df['rating'].apply(lambda x: x['rate'])
avg_rating_per_category = df.groupby('category')['rating_rate'].mean()
print("Средний рейтинг по категориям:")
print(avg_rating_per_category)
```

#### Топ-3 товара с наивысшим рейтингом

```python
top_rated = df.sort_values(by='rating_rate', ascending=False).head(3)
print("Топ-3 товара по рейтингу:")
print(top_rated[['title', 'rating_rate']])
```

#### Перевод цен в рубли (курс 1 USD = 90 RUB)

```python
df['price_rub'] = df['price'] * 90
print(df[['title', 'price', 'price_rub']].head())
```

---

### ✅ Результат

Ты получаешь:

* Рабочее соединение с API
* Готовый `DataFrame` с товарами
* Анализ с выводами
* Визуализацию по категориям
* Дополнительные полезные метрики

---

