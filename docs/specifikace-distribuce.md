# Specifikace účastnické distribuce

## Účel

Podklad pro nácvik dovedností uživatelů s agentními nástroji ve VS Code. Účastník odvozuje výsledek ze zadání, specifikace a vstupů a ověřuje práci agenta vlastními důkazy.

## Požadavky

- R1: Distribuce obsahuje přípravu, pět projektových balíčků a celkem 26 zadání.
- R2: Zadání uvádí cíl, vstupy, povolené zásahy, výstup a kritéria přijetí. Neuvádí konkrétní diagnózu, opravený kód ani tabulku výsledků pro dodaná data.
- R3: Specifikace chování, struktura výstupu a obecná metoda jsou dostupné. Účastník musí mít dost informací k samostatnému řešení.
- R4: Referenční řešení, interní poznámky autora k řešení cvičení a hotové výstupy účastníků nejsou součástí distribuce ani její počáteční historie.
- R5: Dodané zdrojové texty, CSV a výchozí Python projekty zůstávají zachovány. Výjimkou jsou průvodci projektů, které definují požadované chování bez popisu nálezů.
- R6: Předem dodané role a postupy jsou učební pomůcky. Agent nebo skill, který má účastník vytvořit, není předem dodaný.
- R7: Změna probíhá podle specifikace: požadavky → plán → vlastní práce → důkaz ověření → záznam. U opravy musí regresní test selhat před změnou a projít po ní.
- R8: Výsledky každého účastníka se ukládají v jeho vlastní větvi nebo kopii repozitáře. Účastnické výsledky se neslučují do výchozího main.
- R9: Omezení nástrojů, pokyny pro roli a izolace prostředí se vysvětlují samostatně. Dostupný terminál umožňuje i zápis; textová pravidla nejsou sandbox.
- R10: Automatická kontrola ověřuje strukturu, odkazy a konfigurace. Kontrola obsahu člověkem rozhoduje, zda text neprozrazuje odpovědi. Automatická kontrola nevydává osvědčení správnosti výstupů účastníka.

## Přijetí nové verze

1. Spustit `python tools/validate_materials.py` z kořene repozitáře.
2. Ručně projít všechny změněné učební texty, názvy a popisy rolí. Odstranit nápovědy odhalující konkrétní nálezy v dodaném projektu.
3. Ověřit startovní data a kód a zkontrolovat, že výstupní adresáře obsahují pouze průvodní soubory.
4. Před publikací zkontrolovat Git historii a dostupné větve.

## Kontrola prostředí před workshopem

Na počítači účastníka otevřít vybraný balíček v novém okně VS Code a ověřit načtení jeho pokynů, rolí, skills a skutečně dostupných nástrojů. Automatická kontrola distribuce tento krok nenahrazuje; závisí na konkrétní instalaci, účtu a zvoleném harnessu.

Veřejně dostupné materiály mimo tento repozitář nelze samotnou větví skrýt. Při samostatné práci se hotové odpovědi nevyhledávají a do chatu se nepřikládají starší vyřešené pokusy.
