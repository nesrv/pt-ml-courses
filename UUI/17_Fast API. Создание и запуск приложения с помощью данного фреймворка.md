Отлично! Ниже —  **полноценный интерактивный урок по FastAPI** , который ты можешь  **запустить в Google Colab** . Он включает установку, создание приложения, запуск сервера и тестирование с помощью `ngrok`.

---

## 🚀 Урок: FastAPI в Google Colab

### ✅ Шаг 1: Установка FastAPI и Uvicorn + Ngrok

```python
!pip install fastapi uvicorn nest-asyncio pyngrok
```

---

### ✅ Шаг 2: Импорт библиотек и запуск среды

```python
from fastapi import FastAPI
import nest_asyncio
from pyngrok import ngrok
import uvicorn

# Разрешаем повторный запуск uvicorn внутри Colab
nest_asyncio.apply()

# Создание приложения FastAPI
app = FastAPI()
```

---

### ✅ Шаг 3: Создание маршрутов (эндпоинтов)

```python
@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в FastAPI на Google Colab!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Привет, {name}!"}

@app.post("/sum")
def calculate_sum(numbers: dict):
    total = numbers.get("a", 0) + numbers.get("b", 0)
    return {"sum": total}
```

---

### ✅ Шаг 4: Запуск сервера через ngrok

```python
# Пробрасываем порт через ngrok
public_url = ngrok.connect(8000)
print(f"🚀 Ваше приложение доступно по адресу: {public_url}")

# Запуск Uvicorn
uvicorn.run(app, host="0.0.0.0", port=8000)
```

---

Ошибка, которую ты видишь:


### ✅ Решение:

#### 1. **Зарегистрируйся на ngrok**

Если у тебя ещё нет аккаунта:

🔗 [https://dashboard.ngrok.com/signup](https://dashboard.ngrok.com/signup)

#### 2. **Получи свой `authtoken`**

После регистрации и входа:

🔗 [https://dashboard.ngrok.com/get-started/your-authtoken](https://dashboard.ngrok.com/get-started/your-authtoken)

Ты увидишь токен вида:

```
ngrok config add-authtoken 2O7abcDqwerty123456...
```

#### 3. **Установи токен в систему**

Один из следующих способов:

##### 📌 Способ A: Через командную строку (один раз)

```bash
ngrok config add-authtoken <твой_токен>
```

##### 📌 Способ B: В коде Python (например, в Google Colab)

```python
from pyngrok import ngrok, conf

conf.get_default().auth_token = "<твой_токен>"
public_url = ngrok.connect(8000)
print(f"🚀 Ваше приложение доступно по адресу: {public_url}")
```

---

### 🎯 Пример полного кода (с FastAPI и ngrok)

```python
from fastapi import FastAPI
from pyngrok import ngrok, conf
import uvicorn

# Настройка токена для ngrok
conf.get_default().auth_token = "2O7abcDqwerty123456..."  # ← вставь свой токен сюда

# Инициализация приложения
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Привет от FastAPI!"}

# Пробрасываем порт через ngrok
public_url = ngrok.connect(8000)
print(f"🚀 Ваше приложение доступно по адресу: {public_url}")

# Запуск FastAPI через uvicorn
uvicorn.run(app, host="0.0.0.0", port=8000)
```

.





---

## 🛒 Задание: Создание API интернет-магазина с FastAPI

### **Цель:**

Реализовать сервер FastAPI, который:

* предоставляет список товаров,
* позволяет получать товар по ID,
* добавлять новый товар,
* удалять товар,
* обновлять его цену или название.

---

### ✅ Структура товара

Каждый товар — это словарь с полями:

```json
{
  "id": 1,
  "name": "Кроссовки Nike",
  "price": 12999.0,
  "in_stock": true
}
```

---

### 🧩 Требуемые эндпоинты:

1. `GET /products`
   — возвращает список всех товаров.

2. `GET /products/{product_id}`
   — возвращает товар по ID.

3. `POST /products`
   — добавляет новый товар (передаётся JSON).

4. `PUT /products/{product_id}`
   — обновляет название или цену товара.

5. `DELETE /products/{product_id}`
   — удаляет товар по ID.

---




### 📦 Пример реализации (с решениями)

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from pyngrok import ngrok, conf
import uvicorn

conf.get_default().auth_token = "YOUR_NGROK_TOKEN"

app = FastAPI()

# Модель товара
class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

# Имитация базы данных
products = [
    Product(id=1, name="Кроссовки Nike", price=12999),
    Product(id=2, name="Футболка Adidas", price=3499),
    Product(id=3, name="Куртка Puma", price=8999),
]

# Получить все товары
@app.get("/products", response_model=List[Product])
def get_products():
    return products

# Получить товар по ID
@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Товар не найден")

# Добавить товар
@app.post("/products", response_model=Product)
def create_product(product: Product):
    products.append(product)
    return product

# Обновить товар
@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, updated: Product):
    for idx, product in enumerate(products):
        if product.id == product_id:
            products[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Товар не найден")

# Удалить товар
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for idx, product in enumerate(products):
        if product.id == product_id:
            products.pop(idx)
            return {"detail": "Товар удалён"}
    raise HTTPException(status_code=404, detail="Товар не найден")

# Подключаем ngrok
public_url = ngrok.connect(8000)
print(f"🚀 Ваше приложение доступно по адресу: {public_url}")

# Запуск
uvicorn.run(app, host="0.0.0.0", port=8000)
```

---

### 💡 Идеи для расширения:

* Добавить фильтрацию товаров по наличию.
* Реализовать поиск по имени (`/products/search?query=nike`).
* Добавить отдельный эндпоинт для изменения только `in_stock` статуса.
* Валидация уникальности `id`.

