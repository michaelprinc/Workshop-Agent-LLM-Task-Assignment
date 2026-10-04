# Jedna oprava s regresním testem

**Čas:** přibližně 20 minut. **Cíl:** Opravit jednu vlastní zjištěnou odchylku podle postupu.

## Vstupy a rozsah

Vlastní revize, specifikace a dodaný skill `oprava-chyby`.

Před začátkem přečtěte specifikaci projektu a dokončete předchozí cvičení tohoto balíčku. U prvního cvičení stačí jeho předpříprava. Rozsah změn vyplývá z kroků níže; zdrojová data a texty neměňte. Nevyhledávejte předem vytvořené odpovědi mimo pracovní podklady.

## Postup

1. Vyberte jednu odchylku z vlastní revize a zapište požadované chování i důkaz reprodukce.
2. Ověřte použití skillu. Připravte regresní test odvozený z požadavku, spusťte jej před změnou a uchovejte jeho selhání.
3. Proveďte minimální opravu, data neměňte. Pokud odchylka závisí na jiné, vysvětlete závislost a nejdřív upravte plán.
4. Spusťte test po změně, dostupné ostatní testy a příslušné spuštění programu. Neočekávejte, že jedna oprava vyřeší neřešené požadavky.
5. Uložte report do `projekt/znamkovy-kalkulator/docs/opravy/` a prohlédněte diff.

## Kritéria přijetí

- Stejný regresní test selhal před opravou a prošel po ní; důkaz je zachovaný.
- Změna řeší jednu odchylku v povoleném rozsahu a nepřepisuje vstupní data.
- Report uvádí skutečné výsledky, zdroj požadavku a zbývající omezení.

## Záznam a reflexe

Vytvořte vlastní `prubeh.md` v této složce podle [metody práce](../../../docs/metoda-prace.md). Zapište prostředí, svůj prompt a plán, odkazy na vlastní výstupy, skutečné ověření a omezení. Vysvětlete jednu vlastní kontrolu, díky které poznáte, že agent splnil požadavek.

Při potížích s ovládáním použijte [pomoc s prostředím](../../../docs/pomoc-s-prostredim.md). Metodickou nápovědu formulujte obecně; vlastní nálezy a výsledek vytvořte před následným vyhodnocením.
