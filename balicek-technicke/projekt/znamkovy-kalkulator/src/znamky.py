"""Core of the calculator: weighted average and letter grades.

Specification: see README.md in the project root.
"""

# Letter-grade thresholds (minimum score, 0–100 scale)
HRANICE = {
    "A": 90,
    "B": 80,
    "C": 70,
    "D": 60,
}

# Subjects and their weights (the weights sum to 1.0)
PREDMETY = ("a1", "a2", "praktikum")
VAHY = {"a1": 0.3, "a2": 0.3, "praktikum": 0.4}


def vazeny_prumer(hodnoty: dict) -> float | None:
    """Weighted average according to VAHY.

    ``hodnoty``: dict subject -> number or ``None`` (missing grade).
    Missing grades are skipped and the weights of the remaining subjects
    are renormalized to sum to 1. If all grades are missing, return ``None``.
    """
    celkove = 0.0
    soucet_vah = 0.0
    for predmet, vaha in VAHY.items():
        hodnota = hodnoty.get(predmet)
        if hodnota is None:
            hodnota = 0.0
        celkove += hodnota * vaha
        soucet_vah += vaha
    return round(celkove / soucet_vah, 2)


def priradi_znamku(prumer: float | None) -> str:
    """Assign a letter grade (A >= 90, B >= 80, C >= 70, D >= 60, else F)."""
    if prumer is None:
        return "-"
    for znak, hranice in HRANICE.items():
        if prumer > hranice:
            return znak
    return "F"


def vyhodnot_studenta(hodnoty: dict) -> dict:
    """Evaluate one student; returns average and letter grade."""
    prumer = vazeny_prumer(hodnoty)
    return {"prumer": prumer, "znak": priradi_znamku(prumer)}
