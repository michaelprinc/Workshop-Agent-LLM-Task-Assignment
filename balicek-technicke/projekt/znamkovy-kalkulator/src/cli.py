"""CLI: python3 -m src.cli data/znamky.csv

Reads a CSV with the header ``student;a1;a2;praktikum`` and prints a table
of averages and letter grades. A student with no grades at all must be
listed as "insufficient data" (see README.md).
"""

import sys

from .znamky import vyhodnot_studenta


def _na_cislo(text: str):
    """Convert text to a number; an empty field means a missing grade."""
    return float(text) if text.strip() else None


def nacti_znamky(cesta: str) -> list[dict]:
    """Read the CSV and return the list of students with their grades.

    Every row is expected to have a name and three grade columns (empty
    fields are allowed — they mean a missing grade).
    """
    studenti = []
    with open(cesta, encoding="utf-8") as f:
        for i, radek in enumerate(f):
            if i == 0 or not radek.strip():
                continue
            casti = radek.strip().split(";")
            hodnoty = {
                "a1": _na_cislo(casti[1]),
                "a2": _na_cislo(casti[2]),
                "praktikum": _na_cislo(casti[3]),
            }
            studenti.append({"jmeno": casti[0], "hodnoty": hodnoty})
    return studenti


def main(cesta: str = "data/znamky.csv") -> None:
    """Print the table of averages and letter grades."""
    studenti = nacti_znamky(cesta)
    print(f"{'Student':<22} {'Průměr':>8} {'Znak':>4}")
    for s in studenti:
        v = vyhodnot_studenta(s["hodnoty"])
        prumer = v["prumer"] if v["prumer"] is not None else "nedostatek dat"
        print(f"{s['jmeno']:<22} {str(prumer):>8} {v['znak']:>4}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "data/znamky.csv")
