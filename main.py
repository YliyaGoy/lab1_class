class Matrix:
    # в питоне нет указателя. В Python отсутствуют явные указатели, как в языках программирования C++ или C. Вместо этого, в Python используются ссылки на объекты.
    def __init__(self, rows=1, cols=1):
        self.rows = rows  # Инициализация количества строк
        self.cols = cols  # Инициализация количества столбцов
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]  # Создание матрицы с нулевыми значениями

    def __del__(self): # Деструктор
        self.data = None #освобождение памяти путем установки data в None

    def get_element(self, i, j): # Значение элемента
        return self.data[i][j]  #Возвращение значения элемента (i, j)

    def get_element_address(self, i, j): # Адрес жлемента
        return id(self.data[i][j])  #Возвращение адреса элемента (i, j)

    def print_matrix(self): #Печать матрицы
        for row in self.data: # по строке
            print(" ".join(str(elem) for elem in row))

    def add(self, other): # Сложение
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Размеры матриц должны совпадать")  # Проверка размеров для сложения
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]  # Сложение матриц
        return result

    def subtract(self, other):# Вычитание
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Размеры матриц должны совпадать!")  # Проверка размеров для вычитания
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]  # Вычитание матриц
        return result

    def multiply(self, other): # Умножение
        if self.cols != other.rows:
            raise ValueError("Проблема в размерах матриц!")  # Проверка размеров для умножения
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]  # Умножение матриц
        return result

    def multiply_by_scalar(self, scalar): # Умножение на скаляр
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] * scalar  # Умножение матрицы на число
        return result


# Создание матриц
matrix1 = Matrix(2, 2)
matrix1.data = [[1, 2], [3, 4]]

matrix2 = Matrix(2, 2)
matrix2.data = [[5, 6], [7, 8]]
# Работа с классом
result_sum = matrix1.add(matrix2)  # Сложение матриц
result_subtract = matrix1.subtract(matrix2)  # Вычитание матриц
result_multiply = matrix1.multiply(matrix2)  # Умножение матриц
result_scalar = matrix1.multiply_by_scalar(2)  # Умножение матрицы на число


# Проверка работы класса
print("Матрица 1")
matrix1.print_matrix()
print("Матрица 2")
matrix2.print_matrix()

print("\nПроверка вывода значения элемента и адреса:" )
print("\nЗначение:", matrix1.get_element(0,0))
print("\nАдрес:", matrix1.get_element_address(0,0))


print("\nВывод сложения матриц:")
result_sum.print_matrix()
print("Вывод вычитания матриц:")
result_subtract.print_matrix()
print("Вывод умножения матриц:")
result_multiply.print_matrix()
print("Вывод умножения матрицы на скаляр(число):")
result_scalar.print_matrix()

# Использование деструктора
del matrix1
# Проверка того, что матрица была успешно удалена, не находит ее после деструктора
#print("\nЗначение:", matrix1.get_element(0,0))
