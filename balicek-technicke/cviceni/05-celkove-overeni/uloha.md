# Celkové ověření a vlastní postup

**Čas:** přibližně 25 minut. **Cíl:** Dokončit shodu s požadavky a nezávisle ověřit celý výstup.

## Vstupy a rozsah

Specifikace, vlastní nálezy, testy a pracovní projekt.

Před začátkem přečtěte specifikaci projektu a dokončete předchozí cvičení tohoto balíčku. U prvního cvičení stačí jeho předpříprava. Rozsah změn vyplývá z kroků níže; zdrojová data a texty neměňte. Nevyhledávejte předem vytvořené odpovědi mimo pracovní podklady.

## Postup

1. Zkontrolujte zbývající požadavky a odchylky. Potřebné opravy provádějte samostatně s testem, záznamem a diffem.
2. Spusťte celou sadu testů a program na dodaných datech. Očekávanou tabulku odvoďte nezávisle z požadavků a vstupů, ne z výstupu programu.
3. Vytvořte vlastní skill `kontrola-tabulky` se zdrojem očekávání, postupem porovnání a pravidly zachování dat. Ověřte jeho načtení a použití.
4. Napište `projekt/znamkovy-kalkulator/docs/revize-zaverecna.md`: změny, důkazy, stav požadavků a testů, otázky a omezení.

## Kritéria přijetí

- Výstup je porovnán proti nezávisle odvozenému očekávání; rozdíly jsou vyřešené nebo výslovně označené.
- Testy nejsou smazané ani přeskočené kvůli obcházení požadavků; jejich počet odpovídá vlastním testovacím případům.
- Vlastní skill a závěrečný report jsou ověřené, data zůstala zachovaná.

## Záznam a reflexe

Vytvořte vlastní `prubeh.md` v této složce podle [metody práce](../../../docs/metoda-prace.md). Zapište prostředí, svůj prompt a plán, odkazy na vlastní výstupy, skutečné ověření a omezení. Vysvětlete jednu vlastní kontrolu, díky které poznáte, že agent splnil požadavek.

Při potížích s ovládáním použijte [pomoc s prostředím](../../../docs/pomoc-s-prostredim.md). Metodickou nápovědu formulujte obecně; vlastní nálezy a výsledek vytvořte před následným vyhodnocením.
