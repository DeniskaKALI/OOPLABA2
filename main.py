from abc import ABC, abstractmethod
from typing import List

class AbstractArray(ABC):
    def __init__(self, length: int = 0):
        self._length = length
        self._massive: List[int] = [0] * length

    @abstractmethod
    def printArray(self) -> None:
        pass

    @abstractmethod
    def minAndMax(self) -> str:
        pass

    @abstractmethod
    def sortArray(self) -> List[int]:
        pass

    @abstractmethod
    def sumArray(self) -> int:
        pass

    def get_massive(self) -> List[int]:
        return self._massive

    def set_massive(self, values: List[int]) -> None:
        if len(values) == self._length:
            self._massive = values
        

class TArray(AbstractArray):
    def __init__(self, length: int = 0):
        super().__init__(length)

    def printArray(self) -> None:
        print("Массив:", self.get_massive())

    def minAndMax(self) -> str:
        return f"Максимальный элемент: {max(self._massive)}, Минимальный элемент: {min(self._massive)}"

    def sortArray(self) -> List[int]:
        return sorted(self._massive)

    def sumArray(self) -> int:
        return sum(self._massive)

    def __add__(self, other: int) -> None:
        self._length += 1
        self._massive.append(other)

    def __mul__(self, other: int) -> None:
        self._massive = [x * other for x in self._massive]


class MultiArray:
    def __init__(self, arrays: List[TArray]):
        self.arrays = arrays

    def print_all_arrays(self) -> None:
        for arr in self.arrays:
            arr.printArray()

    def total_sum(self) -> int:
        return sum(arr.sumArray() for arr in self.arrays)


# Пример использования
arr = TArray(6)  
arr.cinArray([3, 1, 4, 1, 5, 9])  
print("Исходный массив:", arr.massive)  

# Результат работы: Исходный массив: [3, 1, 4, 1, 5, 9]

# Пример использования метода minAndMax
print(arr.minAndMax())
# Результат: Максимальный элемент: 9, Минимальный элемент: 1

# Пример использования метода sortArray
sorted_array = arr.sortArray()
print("Отсортированный массив:", sorted_array)
# Результат: Отсортированный массив: [1, 1, 3, 4, 5, 9]

# Пример использования метода sumArray
print("Сумма элементов массива:", arr.sumArray())
# Результат: Сумма элементов массива: 23

# Пример использования метода __add__ (добавление элемента в массив)
arr + 7  
print("Массив после добавления 7:", arr.massive)
# Результат: Массив после добавления 7: [3, 1, 4, 1, 5, 9, 7]

# Пример использования метода __mul__ (умножение всех элементов массива на 2)
arr * 2 
print("Массив после умножения на 2:", arr.massive)
# Результат: Массив после умножения на 2: [6, 2, 8, 2, 10, 18, 14]

# Пример использования метода cinArray с передачей нового списка значений
arr.cinArray([10, 20, 30, 40, 50, 60])  
print("Массив после вызова cinArray:", arr.massive)
# Результат: Массив после вызова cinArray: [10, 20, 30, 40, 50, 60]
from abc import ABC, abstractmethod
from typing import List

class AbstractArray(ABC):
    def __init__(self, length: int = 0):
        self._length = length
        self._massive: List[int] = [0] * length

    @abstractmethod
    def printArray(self) -> None:
        pass

    @abstractmethod
    def minAndMax(self) -> str:
        pass

    @abstractmethod
    def sortArray(self) -> List[int]:
        pass

    @abstractmethod
    def sumArray(self) -> int:
        pass

    def get_massive(self) -> List[int]:
        return self._massive

    def set_massive(self, values: List[int]) -> None:
        if len(values) == self._length:
            self._massive = values
        

class TArray(AbstractArray):
    def __init__(self, length: int = 0):
        super().__init__(length)

    def printArray(self) -> None:
        print("Массив:", self.get_massive())

    def minAndMax(self) -> str:
        return f"Максимальный элемент: {max(self._massive)}, Минимальный элемент: {min(self._massive)}"

    def sortArray(self) -> List[int]:
        return sorted(self._massive)

    def sumArray(self) -> int:
        return sum(self._massive)

    def __add__(self, other: int) -> None:
        self._length += 1
        self._massive.append(other)

    def __mul__(self, other: int) -> None:
        self._massive = [x * other for x in self._massive]


class MultiArray:
    def __init__(self, arrays: List[TArray]):
        self.arrays = arrays

    def print_all_arrays(self) -> None:
        for arr in self.arrays:
            arr.printArray()

    def total_sum(self) -> int:
        return sum(arr.sumArray() for arr in self.arrays)


# Пример использования
arr = TArray(6)  
arr.cinArray([3, 1, 4, 1, 5, 9])  
print("Исходный массив:", arr.massive)  

# Результат работы: Исходный массив: [3, 1, 4, 1, 5, 9]

# Пример использования метода minAndMax
print(arr.minAndMax())
# Результат: Максимальный элемент: 9, Минимальный элемент: 1

# Пример использования метода sortArray
sorted_array = arr.sortArray()
print("Отсортированный массив:", sorted_array)
# Результат: Отсортированный массив: [1, 1, 3, 4, 5, 9]

# Пример использования метода sumArray
print("Сумма элементов массива:", arr.sumArray())
# Результат: Сумма элементов массива: 23

# Пример использования метода __add__ (добавление элемента в массив)
arr + 7  
print("Массив после добавления 7:", arr.massive)
# Результат: Массив после добавления 7: [3, 1, 4, 1, 5, 9, 7]

# Пример использования метода __mul__ (умножение всех элементов массива на 2)
arr * 2 
print("Массив после умножения на 2:", arr.massive)
# Результат: Массив после умножения на 2: [6, 2, 8, 2, 10, 18, 14]

# Пример использования метода cinArray с передачей нового списка значений
arr.cinArray([10, 20, 30, 40, 50, 60])  
print("Массив после вызова cinArray:", arr.massive)
# Результат: Массив после вызова cinArray: [10, 20, 30, 40, 50, 60]
