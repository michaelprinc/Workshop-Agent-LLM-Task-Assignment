# -*- coding: utf-8 -*-
"""Spočítá souhrn odpovědí z vytazky.csv (průzkum spokojenosti, duben 2026).

Použití (z adresáře projekt/pruzkum-spokojenosti/):
    python skripty/spocitej-odpovedi.py

Skript JEN ČTE data a VYPÍŠE souhrn — žádný soubor nemění.
"""

import csv
from pathlib import Path

# Adresář projektu (dva úrovně nad touto složkou skripty/)
PROJEKT = Path(__file__).resolve().parent.parent
CSV_SOUBOR = PROJEKT / "podklady" / "vytazky.csv"


def main() -> None:
    if not CSV_SOUBOR.exists():
        raise SystemExit(f"Nenalezen soubor: {CSV_SOUBOR}")

    celkem = 0
    bez_hodnoceni = 0
    kategorie: dict[str, list[int]] = {}

    with open(CSV_SOUBOR, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            celkem += 1
            kat = (row.get("kategorie") or "").strip()
            hod = (row.get("hodnoceni") or "").strip()
            if not hod:
                bez_hodnoceni += 1
                continue
            kategorie.setdefault(kat, []).append(int(hod))

    print(f"Celkem odpovědí: {celkem}")
    print(f"Odpovědi bez hodnocení: {bez_hodnoceni}")
    print()
    print("Podle kategorie (jen odpovědi s hodnocením):")
    print(f"{'Kategorie':<12} {'Počet':<6} {'Průměr':<8}")
    for kat in sorted(kategorie):
        hodnoty = kategorie[kat]
        prumer = sum(hodnoty) / len(hodnoty)
        print(f"{kat:<12} {len(hodnoty):<6} {prumer:.2f}")

    vsechny = [h for v in kategorie.values() for h in v]
    if vsechny:
        print()
        print(f"Celkový průměr (všechny odpovědi s hodnocením): "
              f"{sum(vsechny) / len(vsechny):.2f}")


if __name__ == "__main__":
    main()
