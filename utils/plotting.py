import matplotlib.pyplot as plt


def benchmark_plot(sizes: list[int], times: dict[str, list[float]]):
    _, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 7), sharex=True)

    labels = {
        "nested": "O(N²) - Anidada",
        "binary": "O(N log N) - Busqueda Binaria",
        "hash": "O(N) - Intersección Hash",
    }
    markers = {"nested": "o", "binary": "s", "hash": "^"}

    for ax in (ax1, ax2):
        for key in times:  # noqa: PLC0206
            ax.plot(
                sizes,
                times[key],
                marker=markers[key],
                markersize=7,
                linewidth=2,
                label=labels[key],
            )

            for x, y in zip(sizes, times[key]):
                ax.annotate(
                    f"{y:.2g}",
                    (x, y),
                    textcoords="offset points",
                    xytext=(0, 8),
                    ha="center",
                    fontsize=8,
                )

        ax.set_xscale("log")
        ax.set_ylabel("Tiempo de ejecución (s)", fontsize=11)
        ax.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.7)
        ax.legend(fontsize=10)

    ax1.set_yscale("log")
    ax1.set_title(
        "Comparación de algoritmos — Escala Logarítmica", fontsize=13, fontweight="bold"
    )

    ax2.set_title(
        "Comparación de algoritmos — Escala Lineal", fontsize=13, fontweight="bold"
    )
    ax2.set_xlabel("Tamaño de entrada (N)", fontsize=12)

    plt.tight_layout()
    plt.show()
