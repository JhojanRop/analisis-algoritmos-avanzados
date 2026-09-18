import bisect

from utils.decorators import measure_time


@measure_time
def nested_intersection(a: list[int], b: list[int]) -> list[int]:
    intersection = []
    for i in a:
        for j in b:
            if i == j:
                intersection.append(j)

    return intersection


@measure_time
def binary_search_intersection(a: list[int], b: list[int]) -> list[int]:
    b_sorted = sorted(b)
    intersection = []

    for x in a:
        i = bisect.bisect_left(b_sorted, x)

        if i < len(b_sorted) and b_sorted[i] == x:
            intersection.append(x)

    return intersection


@measure_time
def hash_intersection(a: list[int], b: list[int]) -> list[int]:
    b_hash = set(b)
    intersection = []

    for x in a:
        if x in b_hash:
            intersection.append(x)

    return intersection
