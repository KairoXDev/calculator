from tkinter import *
from tkinter import ttk
import calculator as c

# Изначальные значения переменных
oper = ""
first = 0
second = 0
result = 0

# Функция для выполнения вычислений
def calc():
    global result, second  # Указываем, что будем использовать глобальную переменную result
    second = float(entry.get())     # Получаем второе число из ввода и преобразуем его в float
    # Выполняем операцию в зависимости от значения переменной oper
    if oper == "+":
        result = c.add(first, second)
    elif oper == "-":
        result = c.subtract(first, second)
    elif oper == "*":
        result = c.multiply(first, second)
    elif oper == "/":
        result = c.divide(first, second)
    entry.delete(0, END)    # Очищаем поле ввода
    entry.insert(0, str(result))    # Вставляем результат в поле ввода

# Функция для добавления числа в поле ввода
def enter_number(number):
    entry.insert(END, number)

# Функция для очистки поля ввода
def clear_entry():
    entry.delete(0, END)

# Функция для установки выбранной операции
def set_operation(operation):
    global first    # Указываем, что будем использовать глобальную переменную first
    global oper     # Указываем, что будем использовать глобальную переменную oper
    first = float(entry.get())  # Сохраняем первое число и преобразуем его в float
    oper = operation    # Устанавливаем выбранную операцию
    entry.delete(0, END)    # Очищаем поле ввода

# Функция для проверки и фильтрации ввода
def validate_entry():
    e = entry.get()      # Получаем текст из поля ввода
    txt = "".join(b for b in e if b in "0123456789.-")  # Оставляем только цифры, точку и минус
    if e != txt:
        entry.delete(0, END)    # Очищаем поле ввода
        entry.insert(0, txt)    # Вставляем отфильтрованный текст

# Создание главного окна
window = Tk()
window.title("Калькулятор")     # Устанавливаем заголовок окна
window.geometry("305x150+600+300")  # Выравнивание по центру моего пк

# Создание поля ввода
entry = ttk.Entry()
entry.grid(row=0, column=0, columnspan=4, sticky="ew")
entry.bind("<KeyRelease>", lambda event: validate_entry())  # Привязываем функцию проверки к событию нажатия клавиши

# Создание кнопок калькулятора
ttk.Button(text="1", command=lambda: enter_number("1")).grid(row=1, column=0)
ttk.Button(text="2", command=lambda: enter_number("2")).grid(row=1, column=1)
ttk.Button(text="3", command=lambda: enter_number("3")).grid(row=1, column=2)
ttk.Button(text="4", command=lambda: enter_number("4")).grid(row=2, column=0)
ttk.Button(text="5", command=lambda: enter_number("5")).grid(row=2, column=1)
ttk.Button(text="6", command=lambda: enter_number("6")).grid(row=2, column=2)
ttk.Button(text="7", command=lambda: enter_number("7")).grid(row=3, column=0)
ttk.Button(text="8", command=lambda: enter_number("8")).grid(row=3, column=1)
ttk.Button(text="9", command=lambda: enter_number("9")).grid(row=3, column=2)
ttk.Button(text="0", command=lambda: enter_number("0")).grid(row=4, column=0)
ttk.Button(text=".", command=lambda: enter_number(".")).grid(row=4, column=1)

ttk.Button(text="C", command=clear_entry).grid(row=5, column=0, columnspan=4, sticky="ew")
ttk.Button(text="=", command=calc).grid(row=4, column=2)
ttk.Button(text="+", command=lambda: set_operation("+")).grid(row=1, column=3)
ttk.Button(text="-", command=lambda: set_operation("-")).grid(row=2, column=3)
ttk.Button(text="*", command=lambda: set_operation("*")).grid(row=3, column=3)
ttk.Button(text="/", command=lambda: set_operation("/")).grid(row=4, column=3)

# Запуск основного цикла обработки событий
window.mainloop()