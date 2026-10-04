# Průzkum spokojenosti — specifikace

Fiktivní průzkum. CSV a poznámky jsou v `podklady/`; dokumenty patří do `dokumenty/`. Skript `skripty/spocitej-odpovedi.py` je dodaná výpočetní pomůcka, kterou máte použít a ověřit.

- CSV má středníkový oddělovač. Hodnocení je na stupnici 1–5; prázdné hodnocení se nesmí dosadit jako nula.
- Celkový počet odpovědí zahrnuje všechny řádky odpovědí. Počty a průměry hodnocení počítejte pouze z vyplněných hodnocení; u každého ukazatele uveďte jeho rozsah.
- Celkový průměr odvozujte z jednotlivých platných hodnocení, ne z neváženého průměru kategorií.
- Prázdné hodnoty, nejasnosti a údaje z poznámek označte odděleně. Nepřevádějte poznámku vlastníka na ověřený výsledek průzkumu.
- Report má shrnutí, zjištění, tabulku se zdroji, návrhy dalšího postupu a omezení. Doporučení jasně označte jako návrhy.
- Zdrojové podklady zachovejte. Čísla ověřujte skriptem i vybraným nezávislým výpočtem.

Skript spustíte ověřeným interpreterem příkazem `python skripty/spocitej-odpovedi.py` z této složky. Nevytváří výstupní soubory.
