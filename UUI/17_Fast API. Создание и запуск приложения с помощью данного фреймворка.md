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

### ✅ Шаг 5: Тестирование

Открой ссылку, которую выдаст `ngrok`, и:

* Перейди по адресу `https://<ваш-url>/docs` — это автоматически сгенерированная Swagger-документация!
* Примеры запросов:
  * `GET /` — главная
  * `GET /hello/Иван`
  * `POST /sum` с JSON:
    ```json
    {
      "a": 5,
      "b": 10
    }
    ```

---
