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

    @abstractmethod
    def cinArray(self, values: List[int]) -> None:
        pass
    
    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass
    
    def get_massive(self) -> List[int]:
        return self._massive

    def set_massive(self, values: List[int]) -> None:
        if len(values) == self._length:
            self._massive = values
        else:
            raise ValueError(f"Количество элементов ({len(values)}) не соответствует текущей длине массива ({self._length})")
    
    


class TArray(AbstractArray):
    def __init__(self, length: int = 0):
        super().__init__(length)

    def printArray(self) -> None:
        print("Массив:", self.get_massive())

    def cinArray(self, values: List[int]) -> None:
        if len(values) == self._length:  
            self._massive = values

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

    def __call__(self, *args, **kwargs):
        
        if args:
            if len(args) == 1 and isinstance(args[0], list):
                self.cinArray(args[0])
        else:
            return self.get_massive()

class MultiArray:
    def __init__(self, arrays: List[TArray]):
        self.arrays = arrays

    def print_all_arrays(self) -> None:
        for arr in self.arrays:
            arr.printArray()

    def total_sum(self) -> int:
        return sum(arr.sumArray() for arr in self.arrays)

# Пример использования

# Создаем экземпляр TArray с длиной 6
arr = TArray(6)
# Заполняем массив значениями [3, 1, 4, 1, 5, 9]
arr.cinArray([3, 1, 4, 1, 5, 9])

# Выводим исходный массив
print("Исходный массив:", arr.get_massive())
# Результат:
# Исходный массив: [3, 1, 4, 1, 5, 9]

# Выводим минимальный и максимальный элементы массива
print(arr.minAndMax())
# Результат:
# Максимальный элемент: 9, Минимальный элемент: 1

# Выводим отсортированную версию массива
print("Отсортированный массив:", arr.sortArray())
# Результат:
# Отсортированный массив: [1, 1, 3, 4, 5, 9]

# Выводим сумму элементов массива
print("Сумма элементов массива:", arr.sumArray())
# Результат:
# Сумма элементов массива: 23

# Демонстрируем перегрузку оператора +
# Добавляем элемент 7 к массиву
arr + 7
print("Массив после добавления 7:", arr.get_massive())
# Результат:
# Массив после добавления 7: [3, 1, 4, 1, 5, 9, 7]

# Демонстрируем перегрузку оператора *
# Умножаем каждый элемент массива на 2
arr * 2
print("Массив после умножения на 2:", arr.get_massive())
# Результат:
# Массив после умножения на 2: [6, 2, 8, 2, 10, 18, 14] Работает
