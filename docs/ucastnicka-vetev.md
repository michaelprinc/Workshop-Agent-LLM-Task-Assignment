# Vlastní větev a odevzdání

## Získání podkladů

Máte-li právo zapisovat do tohoto repozitáře, naklonujte jej a vytvořte vlastní větev. Ostatní účastníci si nejprve vytvoří fork tohoto účastnického repozitáře a klonují jej, nebo použijí ZIP a vlastní lokální Git. Forkujte tento podklad, ne jiný projekt s hotovými odpověďmi.

```bash
git clone https://github.com/michaelprinc/Workshop-Agent-LLM-Task-Assignement.git
cd Workshop-Agent-LLM-Task-Assignement
git switch -c ucastnik/moje-prezdivka
```

Při práci z forku nahraďte adresu svou adresou. Přezdívku zvolte bez osobních údajů. Příkazy spouštějte v kořenu celého repozitáře; pro chat otevírejte složku konkrétního balíčku.

## Záznam postupu

- Začněte z čistého main a nepřenášejte vyřešené soubory z jiného pracovního projektu.
- Před změnou zkontrolujte `git status`; po práci prohlédněte `git diff`.
- Pro každý dokončený krok vytvořte commit s konkrétním popisem. Přidávejte jen příslušné soubory, nikoli klíče a dočasné soubory.
- Máte-li vzdálené úložiště, odešlete větev příkazem `git push -u origin ucastnik/moje-prezdivka`.
- Odevzdejte odkaz na svou větev a SHA dokončeného commitu. Bez vzdáleného úložiště předložte svůj pracovní projekt a záznam commitů.

Výsledky účastníků se neslučují do výchozího main. Veřejné účastnické větve jsou viditelné ostatním; dokud pracujete samostatně, neprocházejte jejich výsledky. Pokud potřebujete oddělené odevzdání, použijte vlastní soukromý repozitář a přístup pro lektora.

## Opakování

Pro nový pokus začněte v novém adresáři z čistého main, bez starších výstupů, a použijte nový chat. Samotné přepnutí větve nepřipraví novou konverzaci a může ponechat nesledované soubory. Rozpracovaný pokus nejdřív bezpečně uložte; k návratu nepoužívejte hromadné mazání ani reset bez kontroly.
