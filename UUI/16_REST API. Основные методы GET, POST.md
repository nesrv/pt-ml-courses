REST API ( **Representational State Transfer** ) — это архитектурный стиль для взаимодействия с веб-сервисами через протокол  **HTTP** . REST API использует стандартные **HTTP-методы** для работы с ресурсами (данными), такими как  **GET** ,  **POST** ,  **PUT** , **DELETE** и др.

---

## 📌 Основные методы REST API

### 🔹 1. **GET** — получение данных (Чтение)

* **Назначение** : получить информацию с сервера.
* **Безопасен** : не изменяет данные.
* **Пример запроса** :

```http
  GET /users/1 HTTP/1.1
  Host: example.com
```

* **Пример ответа (JSON)** :

```json
  {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com"
  }
```

---

### 🔹 2. **POST** — создание ресурса

* **Назначение** : отправка данных на сервер для создания нового объекта.
* **Тело запроса (body)** содержит данные в формате JSON (чаще всего).
* **Пример запроса** :

```http
  POST /users HTTP/1.1
  Host: example.com
  Content-Type: application/json

  {
    "name": "Bob",
    "email": "bob@example.com"
  }
```

* **Пример ответа** :

```json
  {
    "id": 2,
    "name": "Bob",
    "email": "bob@example.com"
  }
```

---

## 🧪 Пример на Python (с библиотекой `requests`)

```python
import requests

# GET-запрос
response = requests.get('https://jsonplaceholder.typicode.com/users/1')
print(response.json())

# POST-запрос
new_user = {
    "name": "Charlie",
    "email": "charlie@example.com"
}
response = requests.post('https://jsonplaceholder.typicode.com/users', json=new_user)
print(response.status_code)
print(response.json())
```

---

## 📋 Сравнение GET и POST

| Характеристика    | GET                                          | POST                                                             |
| ------------------------------- | -------------------------------------------- | ---------------------------------------------------------------- |
| Действие                | Получение данных              | Отправка/создание данных                   |
| Тело запроса         | Отсутствует                       | Есть (например, JSON)                                |
| Кэшируется            | Да                                         | Обычно нет                                              |
| Идемпотентность  | ✅ (одинаковый результат) | ❌ (может создать несколько записей) |
| Используется для | Запросов и поиска             | Отправки форм, регистрации и т. д.     |

---

Хочешь — могу также рассказать про методы  **PUT** ,  **PATCH** , **DELETE** или показать, как написать простой REST API на Flask или FastAPI.
