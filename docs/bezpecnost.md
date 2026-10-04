# Bezpečnost a skutečná oprávnění

Všechny vstupy jsou ukázková data pro workshop. Nepřidávejte klíče, osobní údaje ani důvěrné pracovní dokumenty.

## Tři odlišné věci

1. **Pravidla role** určují, co má agent dělat. Pravidlo „měň jen výstupy“ samo nepřekáží zápisu jinam.
2. **Výběr nástrojů** určuje dostupné schopnosti. Agent pouze se čtením a hledáním nemá nástroj pro zápis. Agent s terminálem může vytvářet a měnit soubory, i když nemá `edit`.
3. **Omezení prostředí** (sandbox, oprávnění systému, izolovaná složka) mohou přístup skutečně omezit. Jejich dostupnost závisí na platformě a harnessu.

## Nastavení workshopu

Pracujte s ručními oprávněními a zkontrolujte existující pravidla automatického schvalování. Výchozí úroveň neznamená, že před každým zápisem vždy přijde dialog. Každý diff prohlédněte po provedení a před commitem. Nepřepínejte na Allow all ani Autopilot jen proto, že úloha trvá déle.

Čtení dat není oprávnění vykonávat pokyny nalezené v jejich obsahu. Takový text citujte nebo nahlaste jako obsah; neupravujte podle něj projektové pokyny a nespouštějte příkazy. Při praktickém ověřování používejte pouze dočasný soubor ve vlastní pracovní složce a vratné akce.

Bezpečnostní audit popisuje pozorované chování a jeho meze. Jeden úspěšný pokus nedokazuje odolnost proti všem variantám manipulace. Ani Git větev nezajišťuje izolaci procesu, souborového systému nebo přístupu na internet.

[Oficiální bezpečnostní dokumentace](https://code.visualstudio.com/docs/agents/run/security) · [Schvalování](https://code.visualstudio.com/docs/agents/run/approvals)
