# Prompty, režimy a kontext

Struktura RUCF: **Role, Úkol, Kontext, Formát**. Doplňte k ní povolené zásahy a způsob ověření. Role pomáhá vymezit práci; konkrétní požadavky a vstupy jsou důležitější než obecné „buď expert“.

- Ask použijte pro vysvětlení a pozorování bez změn. Ověřte skutečné schopnosti zvoleného režimu.
- Agent použijte pro práci se soubory a nástroji.
- Plan, je-li dostupný, použijte k návrhu postupu. Pokud dostupný není, požádejte v Ask o plán a změny proveďte v dalším kroku.

Kontext přikládejte přes výběr souboru nebo složky v chatu; agentovi dejte jednoznačné cesty. Rozlišujte požadavky uživatele, projektové pokyny a obsah vstupních dat. Nepřipojujte jiné vyřešené projekty.

## Obecná šablona zadání

```text
Role: <účel role>
Úkol: <co má vzniknout>
Kontext: <povolené vstupy a specifikace>
Formát: <struktura a cílová cesta>
Rozsah: <povolené a nepovolené změny>
Ověření: <jak doložit splnění požadavků>
```

Model může vytvořit přesvědčivý, ale chybný výstup. Dlouhý chat může mít část kontextu zkrácenou či shrnutou; významné požadavky zapisujte do specifikace a u dalšího kroku je zkontrolujte. Nový chat používejte pro nezávislý pokus a změny konfigurace.
