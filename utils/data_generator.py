import random


def generate_disjunctive_data(n: int) -> tuple[list[int], list[int]]:
    a = list(range(n))
    b = list(range(n, n * 2))

    random.shuffle(a)
    random.shuffle(b)

    return a, b
