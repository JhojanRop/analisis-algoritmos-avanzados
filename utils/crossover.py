from collections.abc import Iterable
from statistics import median

import pandas as pd

from algorithms import binary_search_intersection, nested_intersection
from utils.data_generator import generate_disjunctive_data


def build_crossover_df(
    sizes: Iterable[int] = range(1, 100), repetitions: int = 7
) -> pd.DataFrame:
    rows = []

    for n in sizes:
        nested_times = []
        binary_times = []

        for _ in range(repetitions):
            a, b = generate_disjunctive_data(n)

            _, nested_time = nested_intersection(a, b)
            _, binary_time = binary_search_intersection(a, b)

            nested_times.append(nested_time)
            binary_times.append(binary_time)

        rows.append(
            {
                "size": n,
                "tiempo anidado": median(nested_times),
                "tiempo busqueda binaria": median(binary_times),
            }
        )

    return pd.DataFrame(rows)
