# Agentní práce s LLM — zadání pro účastníky

Účastnický podklad workshopu pro práci s GitHub Copilotem ve Visual Studio Code. Obsahuje zadání, specifikace, vstupy a pracovní pomůcky. Výsledky vytváříte a ověřujete sami s agentem.

Autor workshopu: Michael Princ, 2026. Jazyk průvodců je čeština; některé ukázkové vstupy a Python kód jsou anglicky.

## Začněte zde

1. Projděte [předpřípravu](00-predpriprava/README.md).
2. Vytvořte vlastní pracovní větev nebo kopii podle [návodu k verzování](docs/ucastnicka-vetev.md).
3. Ve VS Code otevřete celou složku zvoleného balíčku, například `balicek-1-zaklad/`. Jeho `.github/` musí být v kořenu otevřeného workspace.
4. Ověřte načtené pokyny a role podle [průvodce konfigurací](docs/agenti-a-skills.md). Nestačí pouze vidět soubor v průzkumníku.
5. Otevřete aktuální `uloha.md`. Před prací napište plán, po práci uložte důkazy ověření. Další cvičení začínejte až po kontrole aktuálního.

| Balíček | Dovednosti | Předpoklady | Čas cvičení |
|---|---|---|---|
| [1 — Základ](balicek-1-zaklad/README.md) | Prompty, kontext, tvorba a úpravy dokumentů | Hotová předpříprava | 60–75 min |
| [2 — Střední](balicek-2-stredni/README.md) | Projektové pokyny, vlastní agent, handoff, porovnání modelů | Balíček 1; Python pro pomocný skript | 75–90 min |
| [3 — Pokročilý](balicek-3-pokrocily/README.md) | Skills, delegace, koordinace, ověřování dat | Balíček 2; Python | 90–120 min |
| [Humanitní](balicek-humanitni/README.md) | Shrnutí, překlady, citace, práce se zdroji | Balíčky 1–2; základní angličtina | 90–120 min |
| [Technický](balicek-technicke/README.md) | Revize, testy podle specifikace, opravy, kontrola projektu | Balíčky 1–2; Python 3.10+ a pytest | 90–120 min |

Časy nezahrnují instalaci, čtení teorie a delší diskusi. Pro samostudium si ponechte rezervu.

## Práce podle specifikace

Zadání říká, co musí vzniknout. Specifikace projektu určuje požadované chování. Výstup programu ani odpověď modelu samy o sobě nejsou zdrojem pravdy. Postup a záznam ověření najdete v [metodě práce](docs/metoda-prace.md).

Předem dodané skripty slouží k výpočtům během práce, dodané role a skills k nácviku jejich používání. Tam, kde máte vlastní roli či postup vytvořit, je vytvoříte v příslušném cvičení.

## Kontrola a bezpečnost

- Používejte ukázková data; klíče a citlivé údaje do projektu ani chatu nevkládejte.
- Pokyny nalezené ve vstupních datech vyhodnocujte jako obsah, ne jako požadavky uživatele.
- Kontrolujte skutečná oprávnění, každý provedený příkaz a diff. [Bezpečnostní průvodce](docs/bezpecnost.md) vysvětluje omezení.
- Hotové odpovědi nevyhledávejte na internetu ani v jiných projektech. Připojujte jen aktuální pracovní podklady a použijte nový chat bez staršího vyřešeného pokusu.

[Specifikace této distribuce](docs/specifikace-distribuce.md) · [Kontrola materiálů](tools/README.md)
