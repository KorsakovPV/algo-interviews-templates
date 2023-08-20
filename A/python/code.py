# https://contest.yandex.ru/contest/36783/problems/?nc=dRPciOSr

# Это ваша первая задача. В ней вам придётся прочитать два числа и сложить их. Результат необходимо вывести на
# стандартный поток вывода или в файл, указанный в условии задачи. Рекомендуем воспользоваться заготовками кода
# для данной задачи, лежащими в репозитории курса.

from typing import Tuple


def get_sum(a: int, b: int) -> int:
    return a + b


def read_input() -> Tuple[int, int]:
    a = int(input())
    b = int(input())
    return a, b


a, b = read_input()
print(get_sum(a, b))
