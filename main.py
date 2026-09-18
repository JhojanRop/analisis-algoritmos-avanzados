import pandas as pd

from algorithms import (
    binary_search_intersection,
    hash_intersection,
    nested_intersection,
)
from utils.crossover import build_crossover_df
from utils.data_generator import generate_disjunctive_data
from utils.plotting import benchmark_plot


def main():
    sizes = [2, 3, 4, 5]

    rows = []

    for n in sizes:
        a, b = generate_disjunctive_data(10**n)

        _, nested_time = nested_intersection(a, b)
        _, binary_time = binary_search_intersection(a, b)
        _, hash_time = hash_intersection(a, b)

        rows.append(
            {
                "size": 10**n,
                "tiempo anidado": nested_time,
                "tiempo busqueda binaria": binary_time,
                "tiempo hash": hash_time,
            }
        )

    benchmark_df = pd.DataFrame(rows)
    print("\nResultados del benchmark:")
    print(
        benchmark_df.to_string(index=False, float_format=lambda value: f"{value:.9f}")
    )

    benchmark_plot(
        benchmark_df["size"].tolist(),
        {
            "nested": benchmark_df["tiempo anidado"].tolist(),
            "binary": benchmark_df["tiempo busqueda binaria"].tolist(),
            "hash": benchmark_df["tiempo hash"].tolist(),
        },
    )


def crossover():
    df = build_crossover_df(range(1, 100))
    binary_faster = (df["tiempo busqueda binaria"] < df["tiempo anidado"]).tolist()
    crossover_index = next(
        (
            index
            for index in range(len(binary_faster) - 2)
            if all(binary_faster[index : index + 3])
        ),
        None,
    )

    if crossover_index is None:
        print("No se encontró un N* en el rango evaluado.")
        return

    crossover_size = int(df.iloc[crossover_index]["size"])
    print(f"N* aproximado: {crossover_size}")
    print(
        df[df["size"] == crossover_size].to_string(
            index=False, float_format=lambda value: f"{value:.9f}"
        )
    )


if __name__ == "__main__":
    crossover()
    main()
