Отлично! Ниже — полностью готовый **урок в формате Google Colab** для  **Модуля 2: Обучение с учителем. Задача классификации** , с объяснением теории и практическими блоками кода.

---

# 🧠 Модуль 2. Обучение с учителем. Задача классификации

---

## 🔹 1. Понятие нейронной сети

```markdown
🧠 Нейронная сеть — это математическая модель, вдохновлённая устройством мозга. Она состоит из "искусственных нейронов", которые принимают входы, умножают их на веса и применяют активационную функцию.

Нейронная сеть может:
- Классифицировать данные
- Предсказывать значения
- Находить сложные закономерности
```

---

## 🔹 2. Персептрон

### Определение

```markdown
Персептрон — простейшая нейронная сеть (один нейрон) для **линейной бинарной классификации**.
```

### Реализация и обучение

```python
# Импорт необходимых библиотек
from sklearn.linear_model import Perceptron                  # Модель персептрона (линейный классификатор)
from sklearn.datasets import make_classification            # Функция для генерации искусственного набора данных
from sklearn.model_selection import train_test_split        # Функция для разделения выборки на обучающую и тестовую
from sklearn.metrics import accuracy_score                  # Функция для оценки точности модели
import matplotlib.pyplot as plt                             # Библиотека для построения графиков

# Шаг 1. Генерация искусственного набора данных
X, y = make_classification(
    n_samples=200,         # количество объектов (строк) — 200
    n_features=2,          # всего 2 признака (колонки), чтобы удобно было визуализировать
    n_informative=2,       # оба признака действительно влияют на результат (нет "мусорных")
    n_classes=2,           # бинарная классификация (два класса: 0 и 1)
    random_state=1         # фиксируем генератор случайных чисел для повторяемости результата
)

# Шаг 2. Разделение данных на обучающую и тестовую выборку
X_train, X_test, y_train, y_test = train_test_split(
    X, y,                  # все данные (X — признаки, y — классы)
    test_size=0.3,         # 30% данных пойдут на тест, 70% — на обучение
    random_state=42        # снова фиксируем случайность, чтобы результат был воспроизводимым
)

# Шаг 3. Создание и обучение модели персептрона
clf = Perceptron()         # создаём объект модели (без параметров — используются значения по умолчанию)
clf.fit(X_train, y_train)  # обучаем модель на обучающих данных

# Шаг 4. Предсказание и оценка модели
y_pred = clf.predict(X_test)                   # предсказываем метки классов для тестовой выборки
accuracy = accuracy_score(y_test, y_pred)      # сравниваем предсказания с реальными метками
print("Точность на тесте:", accuracy)          # выводим результат в виде доли правильно предсказанных объектов

```

---

## 🔹 3. Адаптивный линейный нейрон (Adaline)

```markdown
Adaline = Adaptive Linear Neuron  
В отличие от персептрона, Adaline использует непрерывную функцию ошибки и градиентный спуск.
```

### Реализация (с нуля):

```python
class AdalineGD:
    def __init__(self, eta=0.01, n_iter=50):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1])
        self.cost_ = []

        for _ in range(self.n_iter):
            net_input = self.net_input(X)
            output = self.activation(net_input)
            errors = y - output
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            cost = (errors**2).sum() / 2.0
            self.cost_.append(cost)
        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def activation(self, X):
        return X

    def predict(self, X):
        return np.where(self.activation(self.net_input(X)) >= 0.0, 1, -1)
```

---

## 🔹 4. Метод градиентного спуска

```markdown
Градиентный спуск — метод оптимизации.  
Мы минимизируем функцию ошибки, двигаясь по направлению её наибольшего уменьшения (градиенту).

Adaline использует этот метод для корректировки весов.
```

---

## 🔹 5. Стохастический градиентный спуск (SGD) в Adaline

```markdown
SGD обновляет веса **на каждом примере**, а не по всей выборке. Это быстрее при больших объёмах данных.
```

```python
from sklearn.linear_model import SGDClassifier

sgd = SGDClassifier(loss='perceptron', learning_rate='constant', eta0=0.01, max_iter=1000)
sgd.fit(X_train, y_train)
print("SGD точность:", sgd.score(X_test, y_test))
```

---

## 🔹 6. Динамическое обучение на больших данных

```markdown
В библиотеке scikit-learn SGDClassifier умеет подгружать данные частями из потоков (например, из файлов или API).

Это полезно при:
- Потоковой обработке данных
- Работе с данными, которые не помещаются в память
```

---

## 🔹 7. Практика с реальным набором Scikit-Learn

```python
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler

# Загрузка и нормализация
data = load_breast_cancer()
X, y = data.data, data.target

X = StandardScaler().fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# SGDClassifier с логистической регрессией
model = SGDClassifier(loss="log_loss", max_iter=1000, tol=1e-3)
model.fit(X_train, y_train)

print("Точность на тесте:", model.score(X_test, y_test))
```

---

## ✅ Выводы

| Модель         | Применение                                   |
| -------------------- | ------------------------------------------------------ |
| Персептрон | Линейная классификация            |
| Adaline              | Использует градиентный спуск |
| SGD                  | Быстрое обучение на потоках    |

---

## 📌 Что дальше?

👉 Перейдём к **Модулю 3: Нейронные сети в Keras и TensorFlow**

Хочешь — подготовлю `*.ipynb`-версию этой тетради, PDF-методичку, или интерактивные задания. Скажи, какой формат удобнее!
