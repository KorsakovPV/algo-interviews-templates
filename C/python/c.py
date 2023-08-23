# https://contest.yandex.ru/contest/36783/problems/C/
from collections import defaultdict
import random


# C. Статус 200

def get_number_of_good_pairs(numbers) -> int:
    count = defaultdict(int)

    for number in numbers:
        count[number % 200] += 1

    c = 0

    for value in count.values():
        c += int(0.5 * value * (value - 1))

    return c

def get_number_of_good_pairs2(numbers) -> int:
    count = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i]-numbers[j]) % 200 == 0:
                print((numbers[i], i), (numbers[j],j), abs(numbers[i]-numbers[j]))
                count += 1
    return count



# n = int(input())
# numbers = list(map(int, input().split()))
# n = int(input())
# numbers = list(map(int, '203 404 204 200 403'.split()))
# # numbers = list(map(int, '1000000'.split()))
numbers = [563, 379, 779, 936, 731, 805, 579]
print(get_number_of_good_pairs(numbers))

# while True:
#     numbers = [random.randint(0, 1000) for r in range(random.randint(0, 10))]
#     if get_number_of_good_pairs(numbers) != get_number_of_good_pairs2(numbers):
#         print(numbers, get_number_of_good_pairs(numbers), get_number_of_good_pairs2(numbers))
#         break
#     print()

