# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# # Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count, cycle
from typing import Generator, List

def random(start: int, iterations: int = 25) -> Generator:
    for i in range(start, start + iterations):
        yield i

def cycled(input_list: List, iterations: int = 25) -> Generator:
    cycler = cycle(input_list)
    for _ in range(0, iterations):
        yield next(cycler)

print(list(random(1, 10)))
print(list(cycled([1, 10], 7)))
