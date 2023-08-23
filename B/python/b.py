# https://contest.yandex.ru/contest/36783/problems/B/

# B. Card Counter
# Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод
# Все языки	0.25 секунд	256Mb	стандартный ввод или input.txt	стандартный вывод или output.txt
# Node.js 14.15.5	1 секунда	256Mb
# Python 3.7.3	1 секунда	256Mb
# OpenJDK Java 11	0.5 секунд	256Mb
# C# (MS .NET 6.0 + ASP)	1 секунда	256Mb
# OpenJDK Java 15	0.5 секунд	256Mb
# C# (MS .NET 5.0 + ASP)	1 секунда	256Mb
# На стол в ряд выложены карточки, на каждой карточке написано натуральное число. За один ход разрешается взять карточку либо с левого, либо с правого конца ряда. Всего можно сделать
# k
#  ходов. Итоговый счет равен сумме чисел на выбранных карточках. Определите, какой максимальный счет можно получить по итогам игры.
# Вы можете воспользоваться заготовками кода для данной задачи из репозитория курса

def get_card_count(n, k, cards) -> int:
    anser_l = [0] * (k + 1)
    anser_r = [0] * (k + 1)

    for i in range(0, k):
        anser_l[i + 1] = anser_l[i + 1] + anser_l[i] + cards[i]
        anser_r[k - i - 1] = anser_r[k - i - 1] + anser_r[k - i] + cards[n - i - 1]

    return max([sum(x) for x in zip(anser_l, anser_r)])


n = int(input())
k = int(input())
cards = list(map(int, input().split()))
# n = 7
# k = 4
# cards = [1, 1, 9, 2, 2, 2, 6]

print(get_card_count(n, k, cards))
