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
print("Исходный массив:", arr.get_massive())

print(arr.minAndMax())
sorted_array = arr.sortArray()
print("Отсортированный массив:", sorted_array)
print("Сумма элементов массива:", arr.sumArray())

arr + 7  
print("Массив после добавления 7:", arr.get_massive())

arr * 2 
print("Массив после умножения на 2:", arr.get_massive())

arr.cinArray([10, 20, 30, 40, 50, 60])
print("Массив после вызова cinArray:", arr.get_massive())
from abc import ABC, abstractmethod
from typing import List

# Абстрактный базовый класс
class AbstractArray(ABC):
    def __init__(self, length: int = 0):
        self._length = length  # Приватное поле для длины массива
        self._massive: List[int] = [0] * length  # Приватный массив
    
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

    # Метод для работы с массивом
    def get_massive(self) -> List[int]:
        return self._massive

    def set_massive(self, values: List[int]) -> None:
        if len(values) == self._length:
            self._massive = values
        else:
            raise ValueError(f"Количество элементов ({len(values)}) не соответствует текущей длине массива ({self._length})")

# Класс TArray реализует абстрактный класс
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
        # Перегрузка оператора сложения
        self._length += 1
        self._massive.append(other)

    def __mul__(self, other: int) -> None:
        # Перегрузка оператора умножения
        self._massive = [x * other for x in self._massive]

# Класс для работы с многими массивами (композиция)
class MultiArray:
    def __init__(self, arrays: List[TArray]):
        self.arrays = arrays  # Композиция: храним несколько массивов
    
    def print_all_arrays(self) -> None:
        for arr in self.arrays:
            arr.printArray()
    
    def total_sum(self) -> int:
        return sum(arr.sumArray() for arr in self.arrays)

# Пример использования:

# Создание нескольких объектов TArray
arr1 = TArray(6)
arr1.set_massive([3, 1, 4, 1, 5, 9])

arr2 = TArray(4)
arr2.set_massive([2, 7, 1, 8])

# Использование композиции: создаем объект MultiArray
multi_arr = MultiArray([arr1, arr2])

# Печать всех массивов
multi_arr.print_all_arrays()

# Получение общей суммы всех массивов
print(f"Общая сумма всех массивов: {multi_arr.total_sum()}")

# Пример перегрузки операторов
arr1 + 10  # Добавляем 10 в arr1
print("Массив после добавления 10 в arr1:")
arr1.printArray()

arr2 * 2  # Умножаем все элементы arr2 на 2
print("Массив после умножения arr2 на 2:")
arr2.printArray()

