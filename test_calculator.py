import calculator as c
import pytest

# Тестирование функции сложения
def test_add():
    # Проверяем правильность сложения чисел
    assert c.add(10, 5) == 15
    assert c.add(-1, 1) == 0
    assert c.add(-2, -2) == -4

    # Проверяем, что функция выбрасывает исключение TypeError при неверных типах данных
    with pytest.raises(TypeError):
        c.add("text", 5)

    with pytest.raises(TypeError):
        c.add(5, "4")

# Тестирование функции вычитания
def test_subtract():
    # Проверяем правильность вычитания чисел
    assert c.subtract(10, 5) == 5
    assert c.subtract(-1, 1) == -2
    assert c.subtract(-10, -10) == 0

    # Проверяем, что функция выбрасывает исключение TypeError при неверных типах данных
    with pytest.raises(TypeError):
        c.subtract("text", 5)

    with pytest.raises(TypeError):
        c.subtract(5, "4")

# Тестирование функции умножения
def test_multiply():
    # Проверяем правильность умножения чисел
    assert c.multiply(2, 2) == 4
    assert c.multiply(-2, 2) == -4
    assert c.multiply(-1, -5) == 5

# Тестирование функции деления
def test_divide():
    # Проверяем правильность деления чисел
    assert c.divide(10, 2) == 5
    assert c.divide(-10, 2) == -5
    assert c.divide(-10, -2) == 5

    # Проверяем, что функция выбрасывает исключение TypeError при неверных типах данных
    with pytest.raises(TypeError):
        c.divide("text", 5)

    with pytest.raises(TypeError):
        c.divide(5, "4")

    # Проверяем, что функция выбрасывает исключение ZeroDivisionError при делении на ноль
    with pytest.raises(ZeroDivisionError):
        c.divide(10, 0)

# Запуск тестов
test_add()
test_subtract()
test_multiply()
test_divide()

print("Тесты пройдены успешно!")

