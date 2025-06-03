
## 🧩 REST API на Python с использованием Fake Store API

### 📦 Требования:

* Python 3.7+
* Установить библиотеку:

```bash
pip install requests
```

---

### 🎯 Цель:

Научиться делать `GET`, `POST`, `PUT`, `DELETE` запросы к REST API с помощью Python.

---

## 🔧 Подключение

```python
import requests

BASE_URL = "https://fakestoreapi.com"
```

---

## 1️⃣ Получение списка товаров (GET)

```python
response = requests.get(f"{BASE_URL}/products")
products = response.json()

for product in products:
    print(f"{product['id']}: {product['title']} - ${product['price']}")
```

📌 **Задание**:

* Получи все товары
* Выведи только те, у которых цена выше \$100


```py
import requests

BASE_URL = "https://fakestoreapi.com"

# Получаем все товары
response = requests.get(f"{BASE_URL}/products")
products = response.json()

# Фильтруем товары с ценой > 100
expensive_products = [p for p in products if p['price'] > 100]

# Выводим отфильтрованные товары
for product in expensive_products:
    print(f"{product['title']} — ${product['price']}")

```
---

## 2️⃣ Получение товара по ID (GET)

```python
product_id = 3
response = requests.get(f"{BASE_URL}/products/{product_id}")
product = response.json()

print(f"Название: {product['title']}")
print(f"Цена: {product['price']}")
print(f"Описание: {product['description']}")
```

---

## 3️⃣ Создание заказа (POST)

```python
payload = {
    "userId": 5,
    "date": "2020-02-03",
    "products": [
        {"productId": 1, "quantity": 2},
        {"productId": 2, "quantity": 1}
    ]
}

response = requests.post(f"{BASE_URL}/carts", json=payload)
print("Ответ сервера:", response.status_code)
print("Созданный заказ:", response.json())
```

📌 **Задание**:

* Измени дату и товары
* Создай новый заказ

---

## 4️⃣ Обновление товара (PUT)

```python
product_id = 7
updated_data = {
    "title": "Новый заголовок товара",
    "price": 19.99,
    "description": "Обновлённое описание",
    "image": "https://i.pravatar.cc",
    "category": "electronics"
}

response = requests.put(f"{BASE_URL}/products/{product_id}", json=updated_data)
print("Ответ:", response.status_code)
print("Новые данные:", response.json())
```

📌 **Задание**:

* Попробуй изменить `category` на `"jewelery"` и проверь, что изменилось

---

## 5️⃣ Удаление товара (DELETE)

```python
product_id = 10
response = requests.delete(f"{BASE_URL}/products/{product_id}")
print("Статус удаления:", response.status_code)
print("Удалённый товар:", response.json())
```

📌 **Задание**:

* Удали любой товар по ID

---


