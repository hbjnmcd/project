from tkinter import *
from tkinter import Menu
from tkinter.ttk import Combobox
import math


class Task:

    def __init__(self):
        self.task_name = ''
        self.calc_type = None # Тип вычислений
        self.left_limit = None
        self.right_limit = None
        self.var_number = None # Количество переменных в подинтегральной функции
        self.step_type = None # Тип шага. 0 - постоянный шаг, 1 - переменный шаг
        self.step_number = None # Количество разбиений с постоянным шагом
        self.accuracy = None # Точность вычислений
        self.function_str = ''
        self.var_x = 'x'
        self.var_y = 'y'

    def set_function_str(self, st):
        self.function_str = st

    def calc_function_x(self, x):
        f = self.function_str.replace(self.var_x, str(x))
        return eval(f)

    # calculate functions with constant step

    def left_rectangle_const_step(self):
        h = (self.right_limit - self.left_limit) / self.step_number
        x = self.left_limit
        y = 0
        while x <= (self.right_limit - h):
            y += self.calc_function_x(x)
            x += h
        y *= h
        print(y)

    def right_rectangle_const_step(self):
        h = (self.right_limit - self.left_limit) / self.step_number
        x = self.left_limit + h
        y = 0
        while x <= self.right_limit:
            y += self.calc_function_x(x)
            x += h
        y *= h
        print(y)

    def trapeze_const_step(self):
        h = (self.right_limit - self.left_limit) / self.step_number
        x = self.left_limit + h
        y0 = self.calc_function_x(self.left_limit)
        y_max = self.calc_function_x(self.right_limit)
        summa = 0
        while x <= (self.right_limit - h):
            summa += self.calc_function_x(x)
            x += h
        y = h * (((y0 + y_max)/2) + summa)
        print(y)

    def parabola_const_step(self):
        h = (self.right_limit - self.left_limit) / (2 * self.step_number)
        x = self.left_limit + h
        y0 = self.calc_function_x(self.left_limit)
        y_max = self.calc_function_x(self.right_limit)
        s1 = 0
        while x <= (self.right_limit - h):
            s1 += self.calc_function_x(x)
            x += 2 * h
        s2 = 0
        x = self.left_limit + 2 * h
        while x <= (self.right_limit - 2 * h):
            s2 += self.calc_function_x(x)
            x += 2 * h
        y = (h/3) * (y0 + 4 * s1 + 2 * s2 + y_max)
        print(y)

    # calculate functions with variable step

    def first_algorithm(self):
        h = (self.right_limit - self.left_limit) / self.step_number



    def main_window(self):

        def clicked():
            val = task_combo.get()
            print(val)
            self.task_name = val

        window = Tk()
        window.title("Вычисления")
        window.geometry('400x250')

        step = 0
        if step == 0:
            task_combo = Combobox(window)
            task_combo['values'] = ("Численное интегрирование", "Иные задачи")
            task_combo.current(1)  # установите вариант по умолчанию
            task_combo.grid(column=2, row=1)
            btn = Button(window, text="Далее", command=clicked)
            btn.grid(column=4, row=2)

        window.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    task = Task()
    task.set_function_str('')
    task.left_rectangle_const_step()
    #task.main_window()
