# -*- coding: utf-8 -*-
"""Spočítá souhrn prodeje z vytazky-04.csv a vyjmenuje chyby exportu.

Použití (z adresáře projekt/kvetinart-vytazky/):
    python skripty/spocitej-prodej.py

Skript JEN ČTE data a VYPÍŠE souhrn — žádný soubor nemění.
Záměrně NEopravuje chyby (duplikáty, chybějící sumy) — ty patří do reportu
a jejich řešení je rozhodnutí vlastníka.
"""

import csv
from collections import Counter
from pathlib import Path

PROJEKT = Path(__file__).resolve().parent.parent
CSV_SOUBOR = PROJEKT / "podklady" / "vytazky-04.csv"
STAVY_VYSTUPNI = {"vydáno", "zrušeno", "vráceno"}


def main() -> None:
    if not CSV_SOUBOR.exists():
        raise SystemExit(f"Nenalezen soubor: {CSV_SOUBOR}")

    with open(CSV_SOUBOR, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter=";"))

    # --- 1) Chyby exportu ---------------------------------------------
    print("== CHYBY EXPORTU ==")
    videne = Counter()
    for i, r in enumerate(rows, start=2):  # řádek 1 = hlavička
        obj = (r.get("objednavka") or "").strip()
        videne[obj] += 1
    for obj, n in sorted(videne.items()):
        if n > 1:
            print(f"duplicitní objednávka {obj} ({n}×)")

    for i, r in enumerate(rows, start=2):
        obj = (r.get("objednavka") or "").strip()
        s = (r.get("sum_kc") or "").strip()
        if not s:
            print(f"řádek {i} (obj. {obj}): chybí sum_kc")
        elif int(s) < 0:
            print(f"řádek {i} (obj. {obj}): záporná suma {s} Kč (vrácení)")

    for i, r in enumerate(rows, start=2):
        stav = (r.get("stav") or "").strip()
        if stav not in STAVY_VYSTUPNI:
            obj = (r.get("objednavka") or "").strip()
            print(f"řádek {i} (obj. {obj}): neznámý stav „{stav}“")

    # --- 2) Souhrn prodeje (jen stav=vydáno, s vyplněnou sumou) --------
    # Každou objednávku započítáme jednou — první výskyt; duplicitní řádky
    # zůstávají vidět v sekci „CHYBY EXPORTU“, ale nesčítají se podruhé.
    print()
    print("== SOUHRN PRODEJE (stav=vydáno, s vyplněnou sumou; "
          "každá objednávka jednou) ==")
    pocty: dict[str, int] = {}
    sumy: dict[str, int] = {}
    zapocitane = set()
    for r in rows:
        obj = (r.get("objednavka") or "").strip()
        if obj in zapocitane:
            continue
        zapocitane.add(obj)
        if (r.get("stav") or "").strip() != "vydáno":
            continue
        s = (r.get("sum_kc") or "").strip()
        if not s:
            continue
        kat = (r.get("kategorie") or "").strip()
        pocty[kat] = pocty.get(kat, 0) + 1
        sumy[kat] = sumy.get(kat, 0) + int(s)

    for kat in sorted(sumy):
        print(f"{kat}: {pocty[kat]} položek, celkem {sumy[kat]} Kč")
    print(f"CELKEM: {sum(pocty.values())} položek, "
          f"{sum(sumy.values())} Kč")


if __name__ == "__main__":
    main()
