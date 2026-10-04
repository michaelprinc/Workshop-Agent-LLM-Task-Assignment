# Testy požadavků

**Čas:** přibližně 20 minut. **Cíl:** Vytvořit testy nezávisle na aktuální implementaci.

## Vstupy a rozsah

Specifikace, vlastní revize a dodaný agent `tester`.

Před začátkem přečtěte specifikaci projektu a dokončete předchozí cvičení tohoto balíčku. U prvního cvičení stačí jeho předpříprava. Rozsah změn vyplývá z kroků níže; zdrojová data a texty neměňte. Nevyhledávejte předem vytvořené odpovědi mimo pracovní podklady.

## Postup

1. Sami sestavte seznam požadavků a jejich testovatelných případů. U hranic zvolte hodnoty z obou stran; u vstupů zvažte podporované varianty.
2. Ověřte nástroje testera a požádejte o testy do `projekt/znamkovy-kalkulator/tests/`. Očekávání musí odvodit z požadavků a vysvětlit je.
3. Spusťte `python -m pytest tests/ -v` z kořene projektu. Projděte skutečná selhání; rozlište problém testu, kódu a nejasnost specifikace.
4. Vyberte další odchylku, připravte malou opravu v hlavní roli a doložte stav před a po. Testy neupravujte pouze kvůli zelenému výsledku.

## Kritéria přijetí

- Očekávané hodnoty mají zdroj ve specifikaci a testy nejsou kopií výstupu programu.
- Tester neměnil produkční kód; jeho rozsah zápisu byl ověřen diffem.
- Oprava má průkazný test a zbývající selhání jsou vysvětlená, nikoli skrytá.

## Záznam a reflexe

Vytvořte vlastní `prubeh.md` v této složce podle [metody práce](../../../docs/metoda-prace.md). Zapište prostředí, svůj prompt a plán, odkazy na vlastní výstupy, skutečné ověření a omezení. Vysvětlete jednu vlastní kontrolu, díky které poznáte, že agent splnil požadavek.

Při potížích s ovládáním použijte [pomoc s prostředím](../../../docs/pomoc-s-prostredim.md). Metodickou nápovědu formulujte obecně; vlastní nálezy a výsledek vytvořte před následným vyhodnocením.
